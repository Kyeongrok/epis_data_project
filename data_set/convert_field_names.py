import json
with open('C:/datas_for_elastic_search/bds_safe_restaurant5.json', encoding='utf-8') as f:
    ls = f.readlines()

    nop = []
    err_str = []
    err_cnt = 0
    for l in ls:
        try:
            '''
            {'_index': 'bds_safe_restaurant5',
             '_type': '_doc', '_id': 'qT3RSnYBIz0ZKG34oo4E',
              '_score': 1.0, '_source': {'@timestamp': '2020-12-10T04:03:40.548Z', 
              '시군구명': '포항시', 
              '안심식당지정일': '2020-11-13', '사업장명': '뚝배기식당', '도로명주소': '경상북도 포항시 남구 포스코대로 393-1', 
              '업종': '일반음식점', '위도': 36.015523964,
               '업종상세': '한식', '대표자명': '최애숙',
                '경도': 129.366141971, 'filename': 'bds_safe_restaurant5', 'sido': '경상북도', 
                '전화번호': '054-275-5150', '선정여부': 'Y', '신우편번호': '37820', '안심식당취소일': ''}}
            '''
            origin = json.loads(l)
            origin['sido'] = origin.pop('시도명')
            origin['sigungu'] = origin.pop('시군구명')
            origin['category'] = origin.pop('업종')
            origin['category_lv2'] = origin.pop('업종상세')
            origin['name'] = origin.pop('사업장명')
            origin['safe_restaurant_d_date'] = origin.pop('안심식당지정일')
            origin['phone_no'] = origin.pop('전화번호')
            origin['is_selection'] = origin.pop('선정여부')
            origin['representative_name'] = origin.pop('대표자명')
            origin['postal_code'] = origin.pop('신우편번호')
            origin['cancel_date'] = origin.pop('안심식당취소일')


            nop.append(origin)
        except Exception as e:
            err_cnt += 1
            err_str.append(l)
            print(e, l)

        try:
            origin['addr_road'] = origin.pop('도로명주소')
            origin['latitude'] = origin.pop('위도')
            origin['longitude'] = origin.pop('경도')
        except Exception as e:
            origin['addr_road'] = ''
            origin['latitude'] = ''
            origin['longitude'] = ''

    print(err_cnt)

    with open('bds_safe_restaurant_error.json', 'w+', encoding='utf-8-sig') as f2:
        for l in err_str:
            f2.write(json.dumps(l, ensure_ascii=False) + '\n')

    with open('bds_safe_restaurant_201212.json', 'w+', encoding='utf-8-sig') as f2:
        idx = 1
        for l in nop:
            l['idx'] = idx
            f2.write(json.dumps(l, ensure_ascii=False) + '\n')
            idx += 1
