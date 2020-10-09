from libs.AddressManager import AddressManager

am = AddressManager()

li = am.read_csv_file_into_list('2017시설접근성_add_code.csv')

d = {}

print(len(li))

for item in li[1:]:
    # print(item[5], item[7], item[8])
    if d.get(item[8]) == None:
        d[item[8]] = {'광역교통시설':[], '교육시설':[], '의료시설':[], '판매시설':[]}
    try:
        print(item[8], item[5], item[7])
        d[item[8]][item[5]].append(float(item[7].replace('>', '')))
    except Exception as e:
        d[item[8]][item[5]].append(0)

am.export_list_to_json_file(d, '2017_infra_accessibility.json')
