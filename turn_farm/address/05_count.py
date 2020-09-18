import json, re
dic = json.loads(open('road_nm_addr_code.json').read())
jo = json.loads(open('academy_sigun_road_nm.json').read())

exception_cnt = 0
for i in range(len(jo)):
    r = jo[i]
    road_nm = re.sub('[0-9]{1,10}번길', '', r['road_nm'])
    r['road_nm'] = road_nm
    try:
        # print(road_nm)
        addr_code = dic[r['si']][r['gungu']][road_nm]
        # print(i, r, addr_code)
    except Exception as e:
        print('---{}---'.format(i), e,r)
        exception_cnt += 1

print('exceptions:',exception_cnt)


