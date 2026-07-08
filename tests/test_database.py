from database.database_manager import DatabaseManager

db = DatabaseManager()

devices = db.get_all_devices()

print()

print("=" * 90)

print("NETWORK ASSET INVENTORY")

print("=" * 90)

print()

print(
    f"{'ID':<5}"
    f"{'IP':<18}"
    f"{'MAC':<20}"
    f"{'TYPE':<18}"
    f"{'HOSTNAME'}"
)

print("-" * 90)

for device in devices:

    print(

        f"{device['id']:<5}"

        f"{device['ip']:<18}"

        f"{device['mac']:<20}"

        f"{device['device_type']:<18}"

        f"{device['hostname']}"

    )

print()

print("=" * 90)

print(

    f"Total Devices : {db.total_devices()}"

)

print("=" * 90)

db.close()