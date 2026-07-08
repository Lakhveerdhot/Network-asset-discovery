from flask import Flask, render_template, request, redirect, url_for
from database.database_manager import DatabaseManager
from database.repositories.device_repository import DeviceRepository
from database.repositories.port_repository import PortRepository
from database.repositories.banner_repository import BannerRepository
from database.repositories.change_repository import ChangeRepository
from database.repositories.scan_repository import ScanRepository
from pathlib import Path
from config.config import BASE_DIR
from flask import send_file
from datetime import datetime, timedelta
from config.config import SCAN_INTERVAL_MINUTES
from database.repositories.scheduler_repository import SchedulerRepository
from database.repositories.settings_repository import SettingsRepository

app = Flask(__name__)


@app.route("/")
def index():

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    scan_repo = ScanRepository(db)

    devices = device_repo.get_all()

    device_filter = request.args.get(
        "device",
        ""
    )

    trust_filter = request.args.get(
        "trust",
        ""
    )

    vendor_filter = request.args.get(
        "vendor",
        ""
    )

    os_filter = request.args.get(
        "os",
        ""
    )

    if device_filter:

        devices = [

            device

            for device in devices

            if device["device_type"] == device_filter

        ]

    if trust_filter:

        devices = [

            device

            for device in devices

            if device["trust_status"] == trust_filter

        ]

    if vendor_filter:

        devices = [

            device

            for device in devices

            if device["vendor"] == vendor_filter

        ]

    if os_filter:

        devices = [

            device

            for device in devices

            if device["operating_system"] == os_filter

        ]

    total_devices = len(devices)

    trusted_devices = sum(

        1

        for device in devices

        if device["trust_status"] == "Trusted"

    )

    unknown_devices = sum(

        1

        for device in devices

        if device["trust_status"] == "Unknown"

    )

    untrusted_devices = sum(

        1

        for device in devices

        if device["trust_status"] == "Untrusted"

    )

    recent_scans = scan_repo.recent_scans()

    device_types = sorted(

        {

            device["device_type"]

            for device in device_repo.get_all()

        }

    )

    vendors = sorted(

        {

            device["vendor"]

            for device in device_repo.get_all()

        }

    )

    operating_systems = sorted(

        {

            device["operating_system"]

            for device in device_repo.get_all()

        }

    )

    response = render_template(

        "index.html",

        devices=devices,

        total_devices=total_devices,

        trusted_devices=trusted_devices,

        unknown_devices=unknown_devices,

        untrusted_devices=untrusted_devices,

        recent_scans=recent_scans,

        device_types=device_types,

        vendors=vendors,

        operating_systems=operating_systems,

        selected_device=device_filter,

        selected_trust=trust_filter,

        selected_vendor=vendor_filter,

        selected_os=os_filter

    )

    db.close()

    return response

@app.route("/device/<mac>")
def device(mac):

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    port_repo = PortRepository(db)

    banner_repo = BannerRepository(db)

    change_repo = ChangeRepository(db)

    device = device_repo.get(mac)

    ports = port_repo.get(mac)

    banners = banner_repo.get_by_mac(mac)

    changes = change_repo.get_by_mac(mac)

    response = render_template(

        "device_details.html",

        device=device,

        ports=ports,

        banners=banners,

        changes=changes

    )

    db.close()

    return response

@app.route("/device/<mac>/trust")
def trust_device(mac):

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    device_repo.trust(mac)

    db.close()

    return redirect(
        url_for("index")
    )


@app.route("/device/<mac>/untrust")
def untrust_device(mac):

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    device_repo.untrust(mac)

    db.close()

    return redirect(
        url_for("index")
    )


@app.route("/device/<mac>/delete")
def delete_device(mac):

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    port_repo = PortRepository(db)

    banner_repo = BannerRepository(db)

    change_repo = ChangeRepository(db)

    port_repo.delete(mac)

    banner_repo.delete(mac)

    change_repo.delete(mac)

    device_repo.delete(mac)

    db.close()

    return redirect(
        url_for("index")
    )


@app.route("/assets")
def assets():

    db = DatabaseManager()

    device_repo = DeviceRepository(db)

    devices = device_repo.get_all()

    device_filter = request.args.get("device", "")
    trust_filter = request.args.get("trust", "")
    vendor_filter = request.args.get("vendor", "")
    os_filter = request.args.get("os", "")

    if device_filter:

        devices = [

            d

            for d in devices

            if d["device_type"] == device_filter

        ]

    if trust_filter:

        devices = [

            d

            for d in devices

            if d["trust_status"] == trust_filter

        ]

    if vendor_filter:

        devices = [

            d

            for d in devices

            if d["vendor"] == vendor_filter

        ]

    if os_filter:

        devices = [

            d

            for d in devices

            if d["operating_system"] == os_filter

        ]

    response = render_template(

        "assets.html",

        devices=devices,

        device_types=sorted(
            {
                d["device_type"]
                for d in device_repo.get_all()
            }
        ),

        vendors=sorted(
            {
                d["vendor"]
                for d in device_repo.get_all()
            }
        ),

        operating_systems=sorted(
            {
                d["operating_system"]
                for d in device_repo.get_all()
            }
        ),

        selected_device=device_filter,

        selected_trust=trust_filter,

        selected_vendor=vendor_filter,

        selected_os=os_filter

    )

    db.close()

    return response


@app.route("/reports")
def reports():

    report_dir = BASE_DIR / "generated-reports"

    reports = []

    if report_dir.exists():

        reports = sorted(

            report_dir.glob("*.txt"),

            reverse=True

        )

    return render_template(

        "reports.html",

        reports=reports

    )


@app.route("/reports/download/<filename>")
def download_report(filename):

    report = BASE_DIR / "generated-reports" / filename

    return send_file(

        report,

        as_attachment=True

    )


@app.route("/reports/view/<filename>")
def view_report(filename):

    report = BASE_DIR / "generated-reports" / filename

    with open(

        report,

        encoding="utf-8"

    ) as file:

        content = file.read()

    return render_template(

        "view_report.html",

        filename=filename,

        content=content

    )


@app.route("/reports/delete/<filename>")
def delete_report(filename):

    report = BASE_DIR / "generated-reports" / filename

    if report.exists():

        report.unlink()

    return redirect(

        url_for("reports")

    )

@app.route("/scheduler")
def scheduler():

    db = DatabaseManager()

    scan_repo = ScanRepository(db)

    scheduler_repo = SchedulerRepository(db)

    latest_scan = scan_repo.latest_scan()

    scheduler_enabled = scheduler_repo.is_enabled()

    scheduler_status = (
        "Running"
        if scheduler_enabled
        else
        "Paused"
    )

    scan_interval = scheduler_repo.interval()

    last_scan = "Never"

    next_scan = "Unknown"

    last_enabled = scheduler_repo.last_enabled()

    if latest_scan:

        last_scan = latest_scan["scan_time"]

    if last_enabled:

        enabled_time = datetime.strptime(

            last_enabled,

            "%Y-%m-%d %H:%M:%S"

        )

        next_scan = (

            enabled_time +

            timedelta(minutes=scan_interval)

        ).strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    else:

        next_scan = "Unknown"

    response = render_template(

        "scheduler.html",

        scheduler_status=scheduler_status,

        scheduler_enabled=scheduler_enabled,

        last_scan=last_scan,

        next_scan=next_scan,

        scan_interval=scan_interval

    )

    db.close()

    return response

@app.route("/scheduler/enable")
def enable_scheduler():

    db = DatabaseManager()

    scheduler_repo = SchedulerRepository(db)

    scheduler_repo.enable()

    db.close()

    return redirect(
        url_for("scheduler")
    )


@app.route("/scheduler/disable")
def disable_scheduler():

    db = DatabaseManager()

    scheduler_repo = SchedulerRepository(db)

    scheduler_repo.disable()

    db.close()

    return redirect(
        url_for("scheduler")
    )

@app.route(
    "/settings",
    methods=["GET", "POST"]
)
def settings():

    db = DatabaseManager()

    settings_repo = SettingsRepository(db)

    if request.method == "POST":

        settings_repo.update(

            target_network=request.form["target_network"],

            scan_timeout=int(

                request.form["scan_timeout"]

            ),

            port_scan_timeout=float(

                request.form["port_scan_timeout"]

            ),

            common_threads=int(

                request.form["common_threads"]

            ),

            banner_enabled=1 if request.form.get(

                "banner_enabled"

            ) else 0,

            os_enabled=1 if request.form.get(

                "os_enabled"

            ) else 0,

            vendor_enabled=1 if request.form.get(

                "vendor_enabled"

            ) else 0,

            report_txt=1 if request.form.get(

                "report_txt"

            ) else 0,

            report_csv=1 if request.form.get(

                "report_csv"

            ) else 0,

            report_pdf=1 if request.form.get(

                "report_pdf"

            ) else 0

        )

        db.close()

        return redirect(

            url_for("settings")

        )

    settings = settings_repo.get()

    response = render_template(

        "settings.html",

        settings=settings

    )

    db.close()

    return response



if __name__ == "__main__":

    app.run(
        debug=True
    )