"""
Display Utilities
"""


def print_banner():

    print("=" * 70)

    print(
        "NETWORK ASSET DISCOVERY PLATFORM".center(70)
    )

    print(
        "Professional Network Asset Discovery Tool".center(70)
    )

    print("=" * 70)


def display_results(hosts):

    print()

    for host in hosts:

        print("=" * 70)

        print(
            f"{'IP Address':<18}: {host.ip}"
        )

        print(
            f"{'MAC Address':<18}: {host.mac}"
        )

        print()

        print("=" * 25)

        print("DEVICE PROFILE")

        print("=" * 25)

        print(
            f"{'Vendor':<18}: {host.profile['vendor']}"
        )

        print(
            f"{'Hostname':<18}: {host.profile['hostname']}"
        )

        print(
            f"{'Source':<18}: {host.profile['hostname_source']}"
        )

        print(
            f"{'Device Type':<18}: {host.profile['device_type']}"
        )

        print(
            f"{'Status':<18}: {host.profile['status']}"
        )

        print(
            f"{'Trust Status':<18}: {host.trust_status}"
        )

        print(
            f"{'Operating System':<18}: "
            f"{host.profile['operating_system']}"
        )

        if host.profile["confidence"] > 0:

            print(
                f"{'Confidence':<18}: "
                f"{host.profile['confidence']}%"
            )

        else:

            print(
                f"{'Confidence':<18}: N/A"
            )

        print()

        print(

            f"{'PORT':<10}"

            f"{'SERVICE':<20}"

            f"{'BANNER'}"

        )

        print("-" * 70)

        if host.open_ports:

            for port in host.open_ports:

                service = host.services.get(

                    port,

                    "UNKNOWN"

                )

                banner = host.banners.get(

                    port,

                    "N/A"

                )

                print(

                    f"{port:<10}"

                    f"{service:<20}"

                    f"{banner}"

                )

        else:

            print(

                "No Open Ports Found"

            )

        print()