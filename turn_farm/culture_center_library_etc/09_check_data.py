from libs.AddressManager import AddressManager
am = AddressManager()


# 문화의집 + 지역문화재단 + 생활문화센터 = 문화의집
# 국립도서관 + 공공도서관 = 도서관
# 박물관 + 미술관 = 박물관
# 지방문화원 + 문예회관 = 지방문화원 수
jo = am.json_from_json_file_nm('2019전국문화기반시설.json')
d = {}
for j in jo:
    print(j)
    if d.get(j['adm_code']) == None:
        d[j['adm_code']] = {'CLTUR_HOUSE_CO':0, 'LBRRY_CO':0, 'MUSEUM_CO':0, 'LCLTY_CLTUR_HOUSE_CO':0}
    if j['type'] == '문화의집' or j['type'] == '지역문화재단' or j['type'] == '생활문화센터':
        d[j['adm_code']]['CLTUR_HOUSE_CO']  += 1
    elif j['type'] == '국립도서관' or j['type'] == '공공도서관':
        d[j['adm_code']]['LBRRY_CO']  += 1
    elif j['type'] == '박물관' or j['type'] == '미술관':
        d[j['adm_code']]['MUSEUM_CO']  += 1
    elif j['type'] == '지방문화원' or j['type'] == '문예회관':
        d[j['adm_code']]['LCLTY_CLTUR_HOUSE_CO']  += 1

print(d)
am.export_list_to_json_file(d, 'culture_museum_library_cnt.json')

