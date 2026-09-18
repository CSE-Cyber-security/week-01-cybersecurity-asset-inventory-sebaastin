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
    add_asset()
