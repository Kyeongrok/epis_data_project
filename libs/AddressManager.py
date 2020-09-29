import pandas as pd
import json, os
import glob
# '시', '군', '구'라면 앞에 시, 도를 찾아서 붙여주는 기능
# 행정구역코드에서 '완주군'을 검색한 후 '전라북도'를 찾는다.
# 이름이 중복될 수도 있지만 일단 붙여보는 것으로 한다.

class AddressManager():
    j_sigungu_sido = []
    law_adm_code_dic = {}
    road_nm_adm_cd_dic = {}

    def __init__(self):
        # file을 load한다. class의 local variable에 넣는다.
        self.j_sigungu_sido = json.loads(open(os.path.dirname(__file__) + '/sigungu_sido.json').read())
        self.law_adm_code_dic = json.loads(open(os.path.dirname(__file__) + '/tree_law_adm.json').read())
        self.road_nm_adm_cd_dic = json.loads(open(os.path.dirname(__file__) + '/road_nm_addr_code.json').read())

    def get_adm_code(self, law_code):
        '''
        법정동 코드를 행정동 코드로 변화시켜준다.
        행정동 코드는 1111000000 이렇게 10자리로 되어 있다.
        '''
        try:
            f = law_code[:2]
            s = law_code[2:5]
            t = law_code[5:]
            adm_code = self.law_adm_code_dic[f][s][t]
            return adm_code
        except Exception as e:
            print('error---', law_code)
            return None

    def make_json_from_excel(self, fr_f_nm, to_f_nm, sheet_name='Sheet1'):
        '''

        '''
        df = pd.read_excel(fr_f_nm, sheet_name=sheet_name)
        # df = df.set_index('sigungu')
        df.reset_index().to_json(to_f_nm, orient='records')
    def export_excel(self):

        print('export succeed')

    def find_do(self, sigungu):
        '''
        시군구를 입력하면 '시도'를 retrun해준다.
        ex_ '완주군'을 검색 하면 '전라북도'를 찾는다.
        중복되는 구가 있으면 맨 첫번째 시도가 return되는 문제가 있다.
        '''
        memo = []
        # j_sigungu_sido를 전체 scan한다
        for i in range(len(self.j_sigungu_sido)):
            row = self.j_sigungu_sido[i]
            if row['sigungu'] == sigungu:
                memo.append(row)
        # 검색 끝나고 2개 이상이면 읍면동도 검색한다.
        if len(memo) > 0:
            return memo[0]['sido']
        else:
            return ''
    def counter_to_list(self, counter):
        '''
        counter를 list로 만들어준다.
        return list
        '''
        li = []
        for key, value in counter.items():
            ret = {}
            ret['id'] = key
            ret['number'] = value
            li.append(ret)
        return li

    def save_list_to_excel(self, list, file_name):
        pd.DataFrame(list).to_excel(file_name)
    def export_list_to_json_file(self, list, file_name):
        with open(file_name, 'w+') as f:
            f.write(json.dumps(list))
    def export_to_index_json(self, lst, file_name, key_name='id'):
        # df로 변환 한 후에 orient를 index로 해준다.
        df = pd.DataFrame(lst)
        df = df.set_index(key_name)
        df.to_json(file_name, orient='index')

    def get_file_list(self, file_location):
        file_names = glob.glob(file_location)
        print(len(file_names))
        return file_names