import json
import pandas as pd
# turn farm
jo = json.loads(open('turn_farm_2019_with_family_infos.json').read())

df = pd.read_excel('동별_문화의집_도서관_지방문화원_etc.xlsx')
df = df.set_index('id')
df.to_json('culture_etc_cnt.json', orient='index')

# 문화시설 개수
jo_culture_cnt = json.loads(open('culture_etc_cnt.json').read())

# print(jo_culture_cnt)
res = []
for r in jo:
    # print(jo_culture_cnt[str(r['add_code'])])
    r['CLTUR_AVG_CO'] = 0
    if jo_culture_cnt.get(str(r['add_code'])) !=  None:
        add_cd = str(r['add_code'])
        # print(jo_culture_cnt[str(r['add_code'])])
        jjjo = jo_culture_cnt[add_cd]
        # print(jjj
        r['CLTUR_AVG_CO'] = jjjo['number']
    else:
        print('else:', r['add_code'])
    res.append(r)



print(len(jo))
# print(res)
print(len(res))
df = pd.DataFrame(res)
df = df.drop(columns=['p3.age', 'p3.sex', 'p4.age', 'p4.sex','p5.age', 'p5.sex','p6.age', 'p6.sex','p7.age', 'p7.sex','p8.age', 'p8.sex','p9.age', 'p9.sex','p10.age', 'p10.sex', 'p3.rela', 'p4.rela', 'p5.rela', 'p6.rela', 'p7.rela', 'p8.rela', 'p9.rela', 'p10.rela'])
open('tf_fm_acc_cult.json', 'w+').write(json.dumps(res))
df.to_excel('turn_fm_2019_w_fi_acc_cult.xlsx')

