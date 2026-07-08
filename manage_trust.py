from database.database_manager import DatabaseManager

db = DatabaseManager()

print()

print("=" * 70)

print("DEVICE TRUST MANAGER")

print("=" * 70)

devices = db.get_all_devices()

for device in devices:

    print(

        f"{device['id']:<3}"

        f"{device['hostname']:<25}"

        f"{device['mac']:<20}"

        f"{device['trust_status']}"

    )

print()

choice = input(

    "Enter Device ID : "

)

status = input(

    "Trust (T) or Untrust (U) : "

).upper()

device = None

for row in devices:

    if row["id"] == int(choice):

        device = row

        break

if device:

    if status == "T":

        db.trust_device(

            device["mac"]

        )

        print()

        print("Device Trusted Successfully.")

    elif status == "U":

        db.untrust_device(

            device["mac"]

        )

        print()

        print("Device Untrusted Successfully.")

db.close()