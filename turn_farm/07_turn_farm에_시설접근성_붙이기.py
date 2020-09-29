import pandas as pd
import json

jo = json.loads(open('turn_farm_2019_with_family_infos.json').read())
jo_acc = json.load(open('2017_infra_accsibility_add_code.json', encoding='utf-8'))

# {'광역교통시설': 35.3743873463, '교육시설': 4.6618367244, '의료시설': 4.5740853767, '판매시설': 8.6472664357, '총합계': 13.7386782921}
res = []
for r in jo:
    r['TRNSPORT_AVG_ACCES_POSBLTY'] = 0
    r['EDC_AVG_ACCES_POSBLTY'] = 0
    r['HSPTL_AVG_ACCES_POSBLTY'] = 0
    r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = 0

    if jo_acc.get(str(r['add_code'])) != None:
        try:
            acc = jo_acc[str(r['add_code'])]
            r['TRNSPORT_AVG_ACCES_POSBLTY'] = acc['광역교통시설']
            r['EDC_AVG_ACCES_POSBLTY'] = acc['교육시설']
            r['HSPTL_AVG_ACCES_POSBLTY'] = acc['의료시설']
            r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = acc['판매시설']
            res.append(r)
        except Exception as e:
            print(e, r)
    else:
        print(r['add_code'], '가 jo_acc에 없음')

print(res[0])

open('tf_family_acc.json', 'w+').write(json.dumps(res))
pd.DataFrame(res).to_excel('mmmm.xlsx')
