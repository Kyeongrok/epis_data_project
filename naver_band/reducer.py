import glob
from naver_band.parse_subpage import parse
import os, json

def reduce(band_id):
    fileList = glob.glob('./{}/html/'.format(band_id)+"*.html")

    cnt = 0
    post_cnt = 0

    result = []
    for fileName in fileList:
        cnt += 1
        file_size = os.path.getsize(fileName)
        if file_size > 0:
            print('try:{}'.format(fileName))
            file = open(fileName, encoding='utf-8')
            string = file.read()
            post_cnt += 1
            try:
                row = parse(string)
                row['year'] = row['post_date'].split(', ')[1]
                row['post_cnt'] = post_cnt
                result.append(row)
                print('cnt:{}, {} has successed.'.format(cnt, fileName))
            except Exception as e:
                print('-----------{} parse fail---------'.format(fileName), e)
        else:
            print('File size of {} is 0.')
    print('band_id:{} result_size:{}'.format(band_id, len(result)))
    return result

band_ids = [7727806,49247132,53029650,56517936,56530371,56609722]
for band_id in band_ids[2:3]:
    result = reduce(band_id)
    open('{}.json'.format(band_id), 'w+').write(json.dumps(result))

#             try:
# except Exception as e:
#         print(fileName, e)

