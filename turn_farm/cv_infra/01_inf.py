import pandas as pd
import csv, json
from libs.AddressManager import AddressManager

flloc = 'C:/Users/ocean/Desktop/(200916) 데이터 수집 목록/6. 편의위락시설정보/07_24_05_P.csv'
law_adm_cd_dic = json.loads(open('road_nm_addr_code.json').read())
sido_eup_men_amd_cd_dic = json.loads(open('../address/eup_men_dong_addr_cd.json').read())
am = AddressManager()

s = set([line.replace('\n', '')for line in open('gun.txt', 'r', encoding='utf-8').readlines()])
#'번호	개방서비스명	개방서비스ID	개방자치단체코드	관리번호	인허가일자	인허가취소일자	영업상태구분코드	영업상태명	상세영업상태코드	상세영업상태명	폐업일자	휴업시작일자	휴업종료일자	재개업일자	소재지전화	소재지면적	소재지우편번호	소재지전체주소	도로명전체주소	도로명우편번호	사업장명	최종수정시점	데이터갱신구분	데이터갱신일자	업태구분명	좌표정보(X)	좌표정보(Y)	위생업태명	남성종사자수	여성종사자수	영업장주변구분명	등급구분명	급수시설구분명	총종업원수	본사종업원수	공장사무직종업원수	공장판매직종업원수	공장생산직종업원수	건물소유구분명	보증액	월세액	다중이용업소여부	시설총규모	전통업소지정번호	전통업소주된음식	홈페이지'
def fn():
    t_addr = []
    t = []
    err_cnt  = 0
    with open(flloc, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            spl = row[18].split(' ')
            if len(spl) > 1 and row[10] != '폐업' and spl[1] in s:
                try:
                    adm_cd = sido_eup_men_amd_cd_dic[spl[0]][spl[1]][spl[2]]
                    t_addr.append(str(adm_cd)+'\n')
                    jl = {'addr':row[10], 'cate':row[25], 'add_code':adm_cd}
                    print(jl)
                    t.append(jl)
                except Exception as e:
                    err_cnt += 1
                    # print(e, row)

    print('{} {}'.format(len(t_addr), err_cnt))
    f = open('adm_cds.txt', 'w+')
    f.writelines(t_addr)
    f.close()

    pd.DataFrame(t).to_excel('d.xlsx')
    with open('ddd.csv', 'w+', newline='') as f:
        f.write(json.dumps(t))

fn()



