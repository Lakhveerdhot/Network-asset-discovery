from services.rule_loader import RuleLoader

loader = RuleLoader()

print()

print("=" * 60)

print("RULE DATABASE")

print("=" * 60)

print()

print("Hostname Rules :", len(loader.hostname_rules))

print("Vendor Rules   :", len(loader.vendor_rules))

print("OS Rules       :", len(loader.os_rules))

print("Port Rules     :", len(loader.port_rules))

print("Service Rules  :", len(loader.service_rules))

print("Banner Rules   :", len(loader.banner_rules))

print("Aliases        :", len(loader.device_aliases))

print()

print("=" * 60)

print("SAMPLE DATA")

print("=" * 60)

print()

print(loader.hostname_rules)

print()

print(loader.vendor_rules)

print()

print(loader.port_rules)

print()

print(loader.service_rules)

print()

print(loader.banner_rules)

print()

print(loader.device_aliases)