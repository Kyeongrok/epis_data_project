import glob
from naver_band.parse_subpage import parse
import os, json, time
from threading import Thread

def run_thread(idx, results, post_ids, band_id):
    fileName = './{}/html/{}.html'.format(band_id, post_ids[idx])
    success_target_path = './{}/successed'.format(band_id)
    print(fileName)
    post_id = post_ids[idx]

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
            print('---{} parse fail---'.format(fileName), e)
            file.close()
            if os.path.exists(fileName):
                os.remove(fileName)
                print('{} removed'.format(fileName))
            else:
                print("The file does not exist")

    else:
        print('{} File size of {} is 0. or already successed'.format(idx, fileName))

def reduce(band_id):
    target_post_ids = []
    post_ids = [filename.split('/html\\')[1].replace('.html', '') for filename in glob.glob('./{}/html/'.format(band_id)+"*.html")]
    success_post_ids = [filename.split('/successed\\')[1].replace('.json', '') for filename in glob.glob('./{}/successed/'.format(band_id)+"*.json")]

    for post_id in post_ids:
        if post_id not in success_post_ids:
            target_post_ids.append(post_id)

    results = [None] * len(target_post_ids)
    threads = [None] * len(target_post_ids)
    total_size = len(target_post_ids)
    for i in range(len(target_post_ids)):
        print('{}/{} started'.format(i, total_size))
        threads[i] = Thread(target=run_thread, args=(i, results, target_post_ids, band_id)).start()
        time.sleep(0.01)
    time.sleep(1)
    print('band_id:{} result_size:{}'.format(band_id, len(results)))
    return results

band_ids = [7727806,49247132,53029650,56517936,56530371,56609722]
for band_id in band_ids:
    result = reduce(band_id)

