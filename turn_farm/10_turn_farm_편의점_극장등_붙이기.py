import json
import pandas as pd
# turn farm
jo = json.loads(open('tf_fm_acc_cult.json').read())

#
jo_cv_inf_cnt = json.loads(open('./cv_infra/cv_inf_cnt_idx.json').read())

# print(jo_cv_inf_cnt)
res = []
for r in jo:
    # print(jo_cv_inf_cnt[str(r['add_code'])])
    r['CNVNC_AVG_CO'] = 0

    if jo_cv_inf_cnt.get(str(r['add_code'])) !=  None:
        add_cd = str(r['add_code'])
        # print(jo_cv_inf_cnt[str(r['add_code'])])
        jjjo = jo_cv_inf_cnt[add_cd]
        # print(jjj
        r['CNVNC_AVG_CO'] = jjjo['number'] / 18
    else:
        print('else:', r['add_code'])
    res.append(r)

print(len(jo))
# print(res)
print(len(res))
df = pd.DataFrame(res)
df = df.drop(columns=['p3.age', 'p3.sex', 'p4.age', 'p4.sex','p5.age', 'p5.sex','p6.age', 'p6.sex','p7.age', 'p7.sex','p8.age', 'p8.sex','p9.age', 'p9.sex','p10.age', 'p10.sex', 'p3.rela', 'p4.rela', 'p5.rela', 'p6.rela', 'p7.rela', 'p8.rela', 'p9.rela', 'p10.rela'])
open('t_fm_2019_acc_cult_cv.json', 'w+').write(json.dumps(res))
df.to_excel('t_fm_2019_w_fi_acc_cult_cv.xlsx')

