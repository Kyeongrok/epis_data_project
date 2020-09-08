import glob
from naver_band.parse_subpage import parse
import os, json, time
from threading import Thread

def run_thread(idx, results, file_list, band_id):
    fileName = file_list[idx]
    success_target_path = './{}/successed'.format(band_id)
    post_id = fileName.split('html\\')[1].replace('.html', '')

    file_size = os.path.getsize(fileName)
    if file_size > 0 and os.path.exists('{}/{}.json'.format(success_target_path, post_id)) == False:
        print('try:{}'.format(fileName))
        file = open(fileName, encoding='utf-8')
        string = file.read()
        try:
            row = parse(string)
            row['year'] = row['post_date'].split(', ')[1]
            row['post_cnt'] = idx + 1
            results[idx] = row
            print('cnt:{}, {} has successed.'.format(idx + 1, fileName))

            if not os.path.isdir(success_target_path):
                os.makedirs(success_target_path)
            su_f = open('{}/{}.json'.format(success_target_path, post_id), 'w+')
            su_f.write(json.dumps(row))
            su_f.close()
        except Exception as e:
            print('-----------{} parse fail---------'.format(fileName), e)
            file.close()
            if os.path.exists(fileName):
                os.remove(fileName)
                print('{} removed'.format(fileName))
            else:
                print("The file does not exist")

    else:
        print('{} File size of {} is 0. or already successed'.format(idx, fileName))

def reduce(band_id):
    fileList = glob.glob('./{}/html/'.format(band_id)+"*.html")[173:]

    results = [None] * len(fileList)
    threads = [None] * len(fileList)
    for i in range(len(fileList)):
        threads[i] = Thread(target=run_thread, args=(i, results, fileList, band_id)).start()
        time.sleep(0.02)
    time.sleep(60)
    print('band_id:{} result_size:{}'.format(band_id, len(result)))
    return result

band_ids = [7727806,49247132,53029650,56517936,56530371,56609722]
for band_id in band_ids[:1]:
    result = reduce(band_id)
    open('{}.json'.format(band_id), 'w+').write(json.dumps(result))

#             try:
# except Exception as e:
#         print(fileName, e)

