from services.oui_lookup import OUILookup

lookup = OUILookup()

print(
    lookup.lookup(
        "84:28:D6:19:0B:91"
    )
)