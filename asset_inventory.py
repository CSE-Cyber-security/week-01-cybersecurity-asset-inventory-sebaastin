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
