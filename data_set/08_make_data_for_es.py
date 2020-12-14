# 읽어서
# dump해서 저장
import json
from libs.FileManager import FileManager
fm = FileManager()

path = 'C:/Users/ocean/Desktop/빅데이터셋 3종/*.json'

fnms = fm.get_file_list(path)
es_id_nm = [
    'bds_fmlg_vilage_sttus_20201214.json',
    'bds_fmlg_vilage_base_20201214.json',
    'bds_fmlg_vilage_resr2_20201214.json',
    'bds_fmlg_vilage_nmpr_20201214.json',
    'bds_fmlg_vilage_resr1_20201214.json',
]
for i in range(0, 5):
    fnm = fnms[i]
    print(fnm)
    fm.head(fnm, 50)
    with open(es_id_nm[i], 'w+', encoding='utf-8') as f:
        for l in fm.json_from_json_file_nm(fnm):
            f.write(json.dumps(l) + '\n')

    fm.head(es_id_nm[i], 1)

# fm.head(fnms[0], 50)
# fm.json_from_json_file_nm(fnms[0])

