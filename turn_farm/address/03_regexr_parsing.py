import re, json
ll = open('학원주소.txt', encoding='utf-8').readlines()

regex = '((([가-힣]+(\d{1,5}|\d{1,5}(,|.)\d{1,5}|)+(동|가|리))(^구|)((\d{1,5}(~|-)\d{1,5}|\d{1,5})(가|리|)|))([ ](산(\d{1,5}(~|-)\d{1,5}|\d{1,5}))|)|(([가-힣]|(\d{1,5}(~|-)\d{1,5})|\d{1,5})+(로|길)))'

sigungu_road_nm  = []
else_cnt = 0
for l in ll[1:]:
    gr = re.search(regex, l)
    spl = l.split(' ')
    if gr != None and len(spl) > 2:
        gr0 = gr.group(0)
        jo = {'si':spl[0], 'gungu':spl[1], 'road_nm':gr.group(0)}
        # print(jo)
        if gr.group(0).find('동') > 0:
            jo['road_nm'] = spl[2]
        # print(l, jo, spl[2], gr0)
        sigungu_road_nm.append(jo)
    else:
       else_cnt += 1

print(len(sigungu_road_nm), len(ll), else_cnt)
open('academy_sigun_road_nm.json', 'w+').write(json.dumps(sigungu_road_nm))