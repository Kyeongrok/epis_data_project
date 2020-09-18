import glob, json
import os



def get_filename(file_id):
    filename = './success\\{}.json'.format(file_id)
    return filename

def run():
    target_ids = [int(f.replace('./success\\', '').replace('.json', '')) for f in glob.glob('./success/' + "*.json") ]
    failed_list = []
    addr_codes = []
    succeed = []

    finished = set()
    if os.path.isfile('success.json'):
        with open('success.json') as f:
            ll = f.read()
            if len(ll) > 1:
                finished = set([int(row) for row in json.loads(ll)])
    target = set(target_ids) - finished
    print(len(target_ids), len(finished))
    if input('go:1? exit:0') == '0':
        exit()

    for file_id in target:
        filename = './success\\{}.json'.format(file_id)
        try:
            addr_code = reduce(filename)
            addr_codes.append(addr_code)
            # 성공 했으면 idx를 저장한다.
            succeed.append(int(file_id))

        except Exception as e:
            print('idx:{} error:'.format(file_id), filename, e)
            failed_list.append((file_id, filename))
            # 에러난거 지운다.
            if os.path.exists(filename):
                os.remove(filename)
                print('------------{} removed'.format(filename))
            else:
                print("The file does not exist")

    with open('addr_codes.json', 'w+') as f:
        f.write(json.dumps(addr_codes))
    with open('log.txt', 'w+') as f_e:
        f_e.write(json.dumps(failed_list))
    with open('success.json', 'w+') as f:
        tt =json.dumps(list(finished.union(set(succeed))))
        print(tt)
        print('succeed:', len(tt))
        f.write(tt)
    print('finished_c:{} failed_cnt:{} su_c:{}'.format(len(finished), len(failed_list), len(addr_codes)))

def reduce(filename):
    print(filename)
    jo = json.loads(open(filename).read())
    common = jo['results']['common']
    print(common)
    if common['totalCount'] != '0':
        # print(jo)
        for juso in jo['results']['juso']:
            print(juso)

        return jo['results']['juso'][0]['admCd']
# run()
reduce(get_filename(0))
