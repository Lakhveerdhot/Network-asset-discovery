from scanner.trust_manager import TrustManager

manager = TrustManager()

print()

print("=" * 60)

print("TRUST TEST")

print("=" * 60)

mac = input("Enter MAC Address : ")

print()

print(

    manager.get_status(mac)

)

manager.close()