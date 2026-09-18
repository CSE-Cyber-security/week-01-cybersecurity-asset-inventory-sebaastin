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
    asset_id = input("Asset ID: ")
    asset_name = input("Asset Name: ")

    while True:
        asset_type = input("Asset Type: ")

        if asset_type in asset_types:
            break

        print("Invalid Asset Type!")
        print("Choose: Workstation, Server, Router, Switch, Application")

    ip_address = input("IP Address: ")
    operating_system = input("Operating System: ")
    department = input("Department: ")

    while True:
        risk_level = input("Risk Level: ")

        if risk_level in risk_levels:
            break

        print("Invalid Risk Level!")
        print("Choose: Low, Medium, High, Critical")

    while True:
        security_status = input("Security Status: ")

        if security_status in security_statuses:
            break

        print("Invalid Security Status!")
        print("Choose: Secure, Warning, Vulnerable")

    asset = {
        "id": asset_id,
        "name": asset_name,
        "type": asset_type,
        "ip": ip_address,
        "os": operating_system,
        "department": department,
        "risk": risk_level,
        "status": security_status
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

            while True:
                new_risk = input("Enter new Risk Level: ")

                if new_risk in risk_levels:
                    asset["risk"] = new_risk
                    break

                print("Invalid Risk Level!")
                print("Choose: Low, Medium, High, Critical")

            while True:
                new_status = input("Enter new Security Status: ")

                if new_status in security_statuses:
                    asset["status"] = new_status
                    break

                print("Invalid Security Status!")
                print("Choose: Secure, Warning, Vulnerable")

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
