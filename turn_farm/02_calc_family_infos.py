import json

'''
parents : 부모 부양 여부
child : 
teenager

'''

def calc_info(lis, fr ,to):
    cnt = 0
    for n in lis:
        if n != None and fr <= n < to:
            cnt += 1
    return cnt

jo = json.loads(open('./turn_farm_2.json').read())

dd = []
for item in jo:
    item['toddler'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],0, 4)
    item['kinder'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],4, 8)
    item['elem'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],8, 14)
    item['middle'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],14, 17)
    item['high'] = calc_info([item['p1.age'], item['p2.age'], item[ 'p3.age'], item['p4.age'], item['p5.age'], item['p6.age'], item['p7.age'], item['p8.age'], item['p9.age'], item['p10.age']],17, 20)
    dd.append(item)

open('./turn_farm_with_family_info.json', 'w+').write(json.dumps(dd))