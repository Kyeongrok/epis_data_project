from libs.AddressManager import AddressManager
am = AddressManager()

l = am.get_file_list('crawl_result/*.json')

result = []
for nm in l:
    spl = nm.replace('crawl_result\\', '').replace('.json', '').split('_')
    jo = am.json_from_json_file_nm(nm)
    for r in jo:
        law_code = r['addr_code']
        adm_code = am.convert_to_adm_code_from_law_code(law_code)
        r['addr_code'] = adm_code
        result.append(r)

am.save_list_to_excel(result, 'real_eastate_rent_fee.xlsx')
am.export_list_to_json_file(result, 'real_eastate_rent_fee.json')
