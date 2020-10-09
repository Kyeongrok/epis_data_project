from libs.AddressManager import AddressManager
am = AddressManager()

l = am.get_file_list('crawl_result/*.json')

result = []
for nm in l:
    spl = nm.replace('crawl_result\\', '').replace('.json', '').split('_')
    jo = am.json_from_json_file_nm(nm)
    result += jo

am.export_list_to_json_file(result, 'real_eastate_rent_fee.json')
