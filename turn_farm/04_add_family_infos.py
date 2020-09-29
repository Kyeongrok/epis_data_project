
from libs.familyInfoGetter import calc_info
from libs.familyInfoGetter import calc_parent
from libs.familyInfoGetter import calc_age_c
import json

jo = json.loads(open('turn_farm_2019.json').read())

dd = []
for item in jo:
    item['toddler'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],0, 4)
    item['kinder'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],4, 8)
    item['elem'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],8, 14)
    item['middle'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],14, 17)
    item['high'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],17, 20)
    item['parent'] = calc_parent([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']])
    item['child'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],0, 8)
    item['teenager'] = 1 if calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],14, 20) > 0 else 0
    item['age_c'] = calc_age_c(item['p1.age'])
    dd.append(item)



open('./turn_farm_2019_with_family_infos.json', 'w+').write(json.dumps(dd))


