import os, json, requests
import shutil

path = os.getcwd()


# band_id와 category를 넣으면 본글과 comment의 파일을 다운로드 받아줌.
def crawl_and_save(image_url, target_dir, file_name):
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        file_name = '{}/{}.jpg'.format(target_dir, file_name)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', file_name)
    else:
        print('Image Couldn\'t be retreived')


def fn(band_id, category):
    # json을 연다.
    for info in json.loads(open('{}.json'.format(band_id)).read()):
        # print(info['post_id'], info['image_urls'])
        img_cnt = 0
        for image_url in info['image_urls']:
            img_cnt+=1
            target_dir = '{}/{}/{}'.format(path, category, info['post_id'])
            crawl_and_save(image_url, target_dir, img_cnt)

        for comment in info['comments']:
            if len(comment['cmt_img_url']) > 0:
                target_dir = '{}/{}/{}/cmt/'.format(path, category, info['post_id'])
                print(info['post_id'], comment['cmt_img_url'])
                crawl_and_save(comment['cmt_img_url'], target_dir, comment['cmt_no'])

band_infos = [
    {"band_id":49247132, "category":'참외', 'from':425435584, 'to':425436125},
    {"band_id":7727806, "category": '딸기', 'from':426019125, 'to': 426020244}, # 2020시작:426019840
    {"band_id":56517936, "category":'토마토', 'from':2807, 'to':3465}, # 2020시작:3217
    {"band_id":56530371, "category":'오리', 'from':2554, 'to':3688}, # 2020시작 : 3120
    {"band_id":56609722, "category":'무', 'from':353, 'to':492},
    {"band_id":53029650, "category": '염소', 'from': 429301115, 'to': 429301860},
]

for band_info in band_infos:
    print(band_info['band_id'], band_info['category'])
for i in range(2, 6):
    fn(band_infos[i]['band_id'], band_infos[i]['category'])