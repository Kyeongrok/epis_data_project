import pandas as pd
import json
from dateutil.parser import parse as parse_dt
from naver_band.naver_band_excel_saver_with_style import save_to_excel

# df = pd.read_json('./7727806.json')

def load_and_save(band_id, type_no):
    jj = json.loads(open('{}.json'.format(band_id)).read())

    list = []
    for j in jj:
        comments = j['comments']
        del j['comments']
        del j['image_urls']
        dt = parse_dt(j['post_date'])
        j['post_date'] = '{} {}'.format(dt.date(), dt.time())
        cmt_fields = {'cmt_name': '', 'cmt_wrt_time': '', 'cmt_content': '', 'cmt_no':''}
        # print(j)
        j_u = {**j, **cmt_fields}
        if j_u['year'] == '2020':
            list.append(j_u)

            cmt_no = 0
            for comment in comments:
                cmt_no += 1
                del comment['cmt_img_url']
                comment['cmt_no'] = cmt_no
                dt_c = parse_dt(comment['cmt_wrt_time'])
                comment['cmt_wrt_time'] = '{} {}'.format(dt_c.date(), dt_c.time())
                base = {'year':'', 'writer': '', 'post_url': '', 'post_date': '', 'post_id': '', 'band_id': '', 'read_count': '',
                        'post_body': '', 'comment_cnt': '','post_cnt':''}

                list.append({**base, **comment})
    df = pd.DataFrame(list)
    print(df.shape)

    df = df[['year', 'post_cnt', 'writer', 'post_date', 'read_count', 'post_body', 'comment_cnt', 'cmt_no', 'cmt_name', 'cmt_content', 'cmt_wrt_time', 'post_url']]
    df = df.rename(columns={"year": "년도", 'post_cnt':'순번', 'writer':'게시자', 'post_date':'게시일시', 'read_count':'조회수', 'post_body':'게시내용',
                            'comment_cnt':'댓글수', 'cmt_no':'댓글순번', 'cmt_name':'댓글작성자', 'cmt_content':'댓글내용', 'cmt_wrt_time':'댓글작성일시', 'post_url':'URL'})

    save_to_excel(df, '{}.xlsx'.format(type_no))

band_infos = [
    {"band_id": 7727806, "category": '딸기', 'from': 426019823, 'to': 426020244},
    {"band_id":56517936, "category":'토마토', 'from':3174, 'to':3465},
    {"band_id":56530371, "category":'오리', 'from':3109, 'to':3688},
    {"band_id":56609722, "category":'무', 'from':400, 'to':492},
    {"band_id":49247132, "category":'참외', 'from':425435833, 'to':425436125},
    {"band_id":53029650, "category": '염소', 'from': 429301115, 'to': 429301860},
]

for band_info in band_infos:
    load_and_save(band_info['band_id'], band_info['category'])

# {'writer': '', 'post_url': '', 'post_date': '', 'post_id': '', 'band_id': '', 'read_count': '',
#  'post_body': '', 'comment_cnt': ''}
