assets = []

asset = {
    "id": "A101",
    "name": "HR-PC-01",
    "type": "Workstation",
    "ip": "192.168.1.10",
    "os": "Windows 11",
    "department": "HR",
    "risk": "Medium",
    "status": "Secure"
}

assets.append(asset)

print("CYBERSECURITY ASSET INVENTORY")
print("============================")

print("Asset ID :", asset["id"])
print("Asset Name :", asset["name"])
print("Asset Type :", asset["type"])
print("IP Address :", asset["ip"])
print("OS :", asset["os"])
print("Department :", asset["department"])
print("Risk Level :", asset["risk"])
print("Status :", asset["status"])
def add_asset():
    asset = {
        "id": input("Asset ID: "),
        "name": input("Asset Name: "),
        "type": input("Asset Type: "),
        "ip": input("IP Address: "),
        "os": input("Operating System: "),
        "department": input("Department: "),
        "risk": input("Risk Level: "),
        "status": input("Security Status: ")
    }

    assets.append(asset)
    print("Asset added successfully!")
def display_assets():
    print("\nCYBERSECURITY ASSET INVENTORY")

    for asset in assets:
        print("----------------------------")
        print("Asset ID :", asset["id"])
        print("Asset Name :", asset["name"])
        print("Asset Type :", asset["type"])
        print("IP Address :", asset["ip"])
        print("OS :", asset["os"])
        print("Department :", asset["department"])
        print("Risk Level :", asset["risk"])
        print("Status :", asset["status"])
def search_asset():
    search_id = input("Enter Asset ID to search: ")

    for asset in assets:
        if asset["id"] == search_id:
            print("Asset Found!")
            print("Asset ID :", asset["id"])
            print("Asset Name :", asset["name"])
            print("Asset Type :", asset["type"])
            print("IP Address :", asset["ip"])
            print("OS :", asset["os"])
            print("Department :", asset["department"])
            print("Risk Level :", asset["risk"])
            print("Status :", asset["status"])
            return

    print("Asset not found!")
    def update_asset():
    update_id = input("Enter Asset ID to update: ")

    for asset in assets:
        if asset["id"] == update_id:
            asset["ip"] = input("Enter new IP Address: ")
            asset["os"] = input("Enter new Operating System: ")
            asset["risk"] = input("Enter new Risk Level: ")
            asset["status"] = input("Enter new Security Status: ")

            print("Asset updated successfully!")
            return

    print("Asset not found!")
    def delete_asset():
    delete_id = input("Enter Asset ID to delete: ")

    for asset in assets:
        if asset["id"] == delete_id:
            assets.remove(asset)
            print("Asset deleted successfully!")
            return

    print("Asset not found!")
    while True:
    print("\n1. Add Asset")
    print("2. Display Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_asset()
    elif choice == "2":
        display_assets()
    elif choice == "3":
        search_asset()
    elif choice == "4":
        update_asset()
    elif choice == "5":
        delete_asset()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
