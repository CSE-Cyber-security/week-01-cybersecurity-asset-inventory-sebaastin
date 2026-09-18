assets = []
asset_types = ["Workstation", "Server", "Router", "Switch", "Application"]
risk_levels = ["Low", "Medium", "High", "Critical"]
security_statuses = ["Secure", "Warning", "Vulnerable"]

# Sample Asset
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


# Add Asset
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


# Display Assets
def display_assets():
    print("\n===== CYBERSECURITY ASSET INVENTORY =====")

    if not assets:
        print("No assets available.")
        return

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


# Search Asset
def search_asset():
    search_id = input("Enter Asset ID to search: ")

    for asset in assets:
        if asset["id"] == search_id:
            print("\nAsset Found!")
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


# Update Asset
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


# Delete Asset
def delete_asset():
    delete_id = input("Enter Asset ID to delete: ")

    for asset in assets:
        if asset["id"] == delete_id:
            assets.remove(asset)
            print("Asset deleted successfully!")
            return

    print("Asset not found!")


# Show Statistics
def show_statistics():
    total = len(assets)
    critical = 0
    high = 0
    medium = 0
    vulnerable = 0

    for asset in assets:
        if asset["risk"] == "Critical":
            critical += 1
        elif asset["risk"] == "High":
            high += 1
        elif asset["risk"] == "Medium":
            medium += 1

        if asset["status"] == "Vulnerable":
            vulnerable += 1

    print("\n===== ASSET STATISTICS =====")
    print("Total Assets :", total)
    print("Critical Assets :", critical)
    print("High Risk Assets :", high)
    print("Medium Risk Assets :", medium)
    print("Vulnerable Assets :", vulnerable)


# Main Menu
while True:
    print("\n===== ASSET INVENTORY MENU =====")
    print("1. Add Asset")
    print("2. Display Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Show Statistics")
    print("7. Exit")

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
        show_statistics()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
