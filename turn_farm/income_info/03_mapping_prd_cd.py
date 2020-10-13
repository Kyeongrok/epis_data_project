from libs.AddressManager import AddressManager
am = AddressManager()

d = am.read_json('income_info.json')
d_prd_cd = am.read_json('prd_cd.json')
d_prd_cd_2 = am.read_json('prd_cd_2.json')
d_prd_cd_old = am.read_json('prd_cd_old.json')
print(len(d), len(d_prd_cd))

err = set()
# print(d_prd_cd)
r = []
for item in d:
    prd_nm = item['작목명']

    items = []
    if d_prd_cd.get(prd_nm) == None:
        if d_prd_cd.get('{}(일반)'.format(prd_nm)) != None:
            # 없으면(일반)을 붙여서 간다
            items = d_prd_cd['{}(일반)'.format(prd_nm)]
        else:
            # 이것도 없으면
            if d_prd_cd_2.get(prd_nm) != None:
                items = d_prd_cd_2[prd_nm]
            else:
                # 구품종명 에서 찾는다.
                if d_prd_cd_old.get(prd_nm) != None:
                    items = d_prd_cd_old[prd_nm]
                else:
                    err.add(prd_nm)
                    print('prd_old에도 없음:', prd_nm)
    else:
        items = d_prd_cd[prd_nm]

    if items != None and items != []:
        item['INCOME_DTA_CODE'] = items[0][1]
        item['PRDLST_CODE_WHSAL'] = items[0][1]
        item['PRDLST_CODE_ENTRPRS'] = items[0][3]
        r.append(item)

am.save_list_to_excel(r, 'incom_info_complete.xlsx')
am.export_list_to_json_file(r, 'incom_info_complete.json')