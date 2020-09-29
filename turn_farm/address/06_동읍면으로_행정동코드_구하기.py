import csv, json
'''
시도, 시군구, 읍면동으로 행정동코드 구하는 map만들기
'''
dic = {}
with open('../../2019 인구이동통계 코드집_공공용.csv', encoding='utf-8') as f:
    s = csv.reader(f)
    for r in s:
        print(r[0], r[1], r[2], r[3])
        if not dic.get(r[1]):
            dic[r[1]] = {}
        if not dic.get(r[1]).get(r[2]):
            dic[r[1]][r[2]] = {}
        if not dic.get(r[1]).get(r[2]).get(r[3]):
            dic[r[1]][r[2]][r[3]] = r[0]

open('eup_men_dong_addr_cd.json', 'w+').write(json.dumps(dic))