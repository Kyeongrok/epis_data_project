from collections import  Counter
from libs.AddressManager import AddressManager


cnt = Counter([l.replace('\n', '') for l in open('adm_cds.txt').readlines()])

am = AddressManager()
lst = am.counter_to_list(cnt)
am.save_list_to_excel(lst, 'cv_inf_cnt.xlsx')

am.export_list_to_json_file(lst, 'cv_inf_cnt.json')

am.export_to_index_json(lst, 'cv_inf_cnt_idx.json')
