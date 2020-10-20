from libs.AddressManager import AddressManager
am = AddressManager()

# 대상이 있어야 함.
# turn_farm_fminf.json 에서
def get_bank_infos(filename):
    bank_nms = [
        '농협','신한','국민','우리','경남','기업','대구','저축',
        '광주','KB','부산','NH','전북','제주','하나','스탠다드차타드'
    ]
    target_keys = am.get_distinct_keys()
    bank_infos = []
    with open(filename ,encoding='cp949') as f:
        ls = f.readlines()
        for l in ls:
            # l = ['4217012700001410019027172', '4217059000', '묵호동', '25708', '', '', '', '하늘과파도소리펜션', '0']
            spl = l.replace('\n','').split('|')
            if spl[1] != '' and spl[7] != '' and int(spl[1]) in target_keys:
                if '은행' in spl[7]:
                    is_contain = False
                    for bank_nm in bank_nms:
                        if bank_nm in spl[7]:
                            bank_infos.append({'add_code':spl[1], 'nm':spl[7]})
                            break
            else:
                # print('e', spl)
                pass
    return bank_infos

file_li = am.get_file_list('add_info/*.txt')
print(file_li)
res = []
for filename in file_li:
    l = get_bank_infos(filename)
    res += l
# am.save_list_to_excel(res, 'bank_info.xlsx')
am.export_list_to_json_file(res, 'bank_cnt.json')


