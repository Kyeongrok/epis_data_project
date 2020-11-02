from libs.AddressManager import AddressManager

am = AddressManager()

jo = am.json_from_json_file_nm('sido.json')
for r in jo:
    print(r)