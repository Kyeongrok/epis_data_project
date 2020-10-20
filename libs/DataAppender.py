import json
import pandas as pd
from libs.AddressManager import AddressManager
from statistics import mean

class DataAppender():
    am = AddressManager()
    mode = 0

    def __init__(self, mode):
        # mode=1이면 json만 저장 0이면 excel도 저장
        self.mode = mode

    def append_real_estate(self, before_filename, cnt_filename, target_filename):
        realestate_buy_sell = json.load(open(cnt_filename))

        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                r['LAD_BFE_AVRG_AMOUNT'] = 0.0
                r['LAD_BFE_TOP_AMOUNT'] = 0.0
                r['LAD_BFE_LWET_AMOUNT'] = 0.0
                r['LAD_RICFLD_AVRG_AMOUNT'] = 0.0
                r['LAD_RICFLD_TOP_AMOUNT'] = 0.0
                r['LAD_RICFLD_LWET_AMOUNT'] = 0.0
                r['ORCHRD_AVRG_AMOUNT'] = 0.0
                r['ORCHRD_TOP_AMOUNT'] = 0.0
                r['ORCHRD_LWET_AMOUNT'] = 0.0

                add_cd = str(r['add_code'])
                if realestate_buy_sell.get(add_cd) !=  None:
                    buy_sell_prices = realestate_buy_sell[add_cd]
                    r['LAD_BFE_AVRG_DELNG_AMOUNT'] = buy_sell_prices['LAD_BFE_AVRG_AMOUNT']
                    r['LAD_BFE_TOP_DELNG_AMOUNT'] = buy_sell_prices['LAD_BFE_TOP_AMOUNT']
                    r['LAD_BFE_LWET_DELNG_AMOUNT'] = buy_sell_prices['LAD_BFE_LWET_AMOUNT']
                    r['LAD_RICFLD_AVRG_DELNG_AMOUNT'] = buy_sell_prices['LAD_RICFLD_AVRG_AMOUNT']
                    r['LAD_RICFLD_TOP_DELNG_AMOUNT'] = buy_sell_prices['LAD_RICFLD_TOP_AMOUNT']
                    r['LAD_RICFLD_LWET_DELNG_AMOUNT'] = buy_sell_prices['LAD_RICFLD_LWET_AMOUNT']
                    r['ORCHRD_AVRG_DELNG_AMOUNT'] = buy_sell_prices['ORCHRD_AVRG_AMOUNT']
                    r['ORCHRD_TOP_DELNG_AMOUNT'] = buy_sell_prices['ORCHRD_TOP_AMOUNT']
                    r['ORCHRD_LWET_DELNG_AMOUNT'] = buy_sell_prices['ORCHRD_LWET_AMOUNT']

                l.append(r)

        open(target_filename, 'w+').write(json.dumps(l))

        if self.mode == 0:
            self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def append_real_estate_rent(self, before_filename, cnt_filename, target_filename):
        realestate_rent = json.load(open(cnt_filename))

        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                r['LAD_BEF_AVRG_RENT_AMOUNT'] = 0.0
                r['LAD_BFE_TOP_RENT_AMOUNT'] = 0.0
                r['LAD_BFE_LWET_RENT_AMOUNT'] = 0.0
                r['LAD_RICFLD_AVRG_RENT_AMOUNT'] = 0.0
                r['LAD_RICFLD_TOP_RENT_AMOUNT'] = 0.0
                r['LAD_RICFLD_LWET_RENT_AMOUNT'] = 0.0
                r['ORCHRD_AVRG_RENT_AMOUNT'] = 0.0
                r['ORCHRD_TOP_RENT_AMOUNT'] = 0.0
                r['ORCHRD_LWET_RENT_AMOUNT'] = 0.0

                add_cd = str(r['add_code'])
                if realestate_rent.get(add_cd) !=  None:
                    rent_prices = realestate_rent[add_cd]
                    r['LAD_BFE_AVRG_RENT_AMOUNT'] = rent_prices['LAD_BFE_AVRG_RENT_AMOUNT']
                    r['LAD_BFE_TOP_RENT_AMOUNT'] = rent_prices['LAD_BFE_TOP_RENT_AMOUNT']
                    r['LAD_BFE_LWET_RENT_AMOUNT'] = rent_prices['LAD_BFE_LWET_RENT_AMOUNT']
                    r['LAD_RICFLD_AVRG_RENT_AMOUNT'] = rent_prices['LAD_RICFLD_AVRG_RENT_AMOUNT']
                    r['LAD_RICFLD_TOP_RENT_AMOUNT'] = rent_prices['LAD_RICFLD_TOP_RENT_AMOUNT']
                    r['LAD_RICFLD_LWET_RENT_AMOUNT'] = rent_prices['LAD_RICFLD_LWET_RENT_AMOUNT']
                    r['ORCHRD_AVRG_RENT_AMOUNT'] = rent_prices['ORCHRD_AVRG_RENT_AMOUNT']
                    r['ORCHRD_TOP_RENT_AMOUNT'] = rent_prices['ORCHRD_TOP_RENT_AMOUNT']
                    r['ORCHRD_LWET_RENT_AMOUNT'] = rent_prices['ORCHRD_LWET_RENT_AMOUNT']
                else:
                    # print(add_cd)
                    pass
                l.append(r)

        open(target_filename, 'w+').write(json.dumps(l))
        if self.mode == 0:
            self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def alter_school(self, before_filename, cnt_filename, target_filename):
        '''
        대안_초등학교_여부
        대안_초중고_여부
        대안_초중_여부
        대안_중학교_여부
        대안_중고_여부
        대안_고등학교_여부
        ALTRV_ELESCH_AT
        ALTRV_ELESCH_MSKUL_HGSCHL_AT
        ALTRV_ELESCH_MSKUL_AT
        ALTRV_MSKUL_AT
        ALTRV_MSKUL_HGSCHL_AT
        ALTRV_HGSCHL_AT
        있으면 1이고 없으면 0이다
        '''

        alter_school_cnt = json.load(open(cnt_filename))
        # print(alter_school_cnt['4272033000'])
        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                r['ALTRV_ELESCH_AT'] = 0
                r['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = 0
                r['ALTRV_ELESCH_MSKUL_AT'] = 0
                r['ALTRV_MSKUL_AT'] = 0
                r['ALTRV_MSKUL_HGSCHL_AT'] = 0
                r['ALTRV_HGSCHL_AT'] = 0
                add_cd = str(r['add_code'])
                if alter_school_cnt.get(add_cd) != None:
                    cnt = alter_school_cnt[add_cd]
                    r['ALTRV_ELESCH_AT'] = cnt['ALTRV_ELESCH_AT']
                    r['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = cnt['ALTRV_ELESCH_MSKUL_HGSCHL_AT']
                    r['ALTRV_ELESCH_MSKUL_AT'] = cnt['ALTRV_ELESCH_MSKUL_AT']
                    r['ALTRV_MSKUL_AT'] = cnt['ALTRV_MSKUL_AT']
                    r['ALTRV_MSKUL_HGSCHL_AT'] = cnt['ALTRV_MSKUL_HGSCHL_AT']
                    r['ALTRV_HGSCHL_AT'] = cnt['ALTRV_HGSCHL_AT']
                l.append(r)

        open(target_filename, 'w+').write(json.dumps(l))
        if self.mode == 0:
            self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def append_infra_accessibility_cnt(self, before_turn_farm_filename, cnt_file_name, target_filename):
        jo = json.loads(open(before_turn_farm_filename).read())
        jo_infra = json.load(open(cnt_file_name, encoding='utf-8'))

        field_names = [
            'ARPRT_ACCES_POSBLTY',
            'BUS_TRMINL_ACCES_POSBLTY',
            'TRAIN_STATN_ACCES_POSBLTY',
            'ELESCH_ACCES_POSBLTY',
            'MSKUL_ACCES_POSBLTY',
            'HGSCHL_ACCES_POSBLTY',
            'PUBLIC_MLFLT_ACCES_POSBLTY',
            'GNRL_HSPTL_ACCES_POSBLTY',
            'GNRLZ_HSPTL_ACCES_POSBLTY',
            'LRSCL_STOR_ACCES_POSBLTY',
            'TRDIT_MRKT_ACCES_POSBLTY'
        ]
        res = []
        for r in jo:
            for field_name in field_names:
                r[field_name] = 0

            if jo_infra.get(str(r['add_code'])) != None:
                try:
                    acc = jo_infra[str(r['add_code'])]
                    r['ARPRT_ACCES_POSBLTY'] = acc['공항']
                    r['BUS_TRMINL_ACCES_POSBLTY'] = acc['버스터미널']
                    r['TRAIN_STATN_ACCES_POSBLTY'] = acc['철도역']
                    r['ELESCH_ACCES_POSBLTY'] = acc['초등학교']
                    r['MSKUL_ACCES_POSBLTY'] = acc['중학교']
                    r['HGSCHL_ACCES_POSBLTY'] = acc['고등학교']
                    r['PUBLIC_MLFLT_ACCES_POSBLTY'] = acc['공공의료시설']
                    r['GNRL_HSPTL_ACCES_POSBLTY'] = acc['병·의원']
                    r['GNRLZ_HSPTL_ACCES_POSBLTY'] = acc['종합병원']
                    r['LRSCL_STOR_ACCES_POSBLTY'] = acc['대규모점포']
                    r['TRDIT_MRKT_ACCES_POSBLTY'] = acc['전통시장']
                    res.append(r)
                except Exception as e:
                    print('error:', e, r)
            else:
                print(r['add_code'], '가 jo_acc에 없음')

        print(res[0])
        print('jo len:', len(jo))

        open(target_filename, 'w+').write(json.dumps(res))
        if self.mode == 0:
            pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

    def append_academy(self, before_filename, cnt_filename, target_filename):
        # load academy cnt
        d_academy_cnt = json.load(open(cnt_filename))

        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                add_cd = str(r['add_code'])
                # add_cd = self.am.convert_to_adm_code_from_law_code(add_cd)
                if d_academy_cnt.get(add_cd) !=  None:
                    academy_cnt = d_academy_cnt[add_cd]['number']
                else:
                    academy_cnt = 0

                r['INSTUT_CO'] = academy_cnt
                l.append(r)

        open(target_filename, 'w+').write(json.dumps(l))
        if self.mode == 0:
            self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def append_culture_center_library_museum(self, before_filename, cnt_filename, target_filename):
        d_cnt = json.load(open(cnt_filename))
        field_names = ['CLTUR_HOUSE_CO','LBRRY_CO','LCLTY_CLTUR_HOUSE_CO','MUSEUM_CO']
        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                for field_name in field_names:
                    r[field_name] = 0
                add_cd = str(r['add_code'])
                if d_cnt.get(add_cd) !=  None:
                    cnt = d_cnt[add_cd]
                    for field_name in field_names:
                        r[field_name] = cnt[field_name]
                l.append(r)
        open(target_filename, 'w+').write(json.dumps(l))
        if self.mode == 0:
            self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def append_infra_accessibility_avg(self, before_turn_farm_filename, cnt_filename, target_filename):
        jo = json.loads(open(before_turn_farm_filename).read())
        jo_acc = json.load(open(cnt_filename, encoding='utf-8'))

        # {'광역교통시설': [], '교육시설': [], '의료시설': [], '판매시설': []}
        res = []
        for r in jo:
            r['TRNSPORT_AVG_ACCES_POSBLTY'] = 0
            r['EDC_AVG_ACCES_POSBLTY'] = 0
            r['HSPTL_AVG_ACCES_POSBLTY'] = 0
            r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = 0

            if jo_acc.get(str(r['add_code'])) != None:
                try:
                    acc = jo_acc[str(r['add_code'])]
                    r['TRNSPORT_AVG_ACCES_POSBLTY'] = mean(acc['광역교통시설'])
                    r['EDC_AVG_ACCES_POSBLTY'] = mean(acc['교육시설'])
                    r['HSPTL_AVG_ACCES_POSBLTY'] = mean(acc['의료시설'])
                    r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = mean(acc['판매시설'])
                    res.append(r)
                except Exception as e:
                    print('err:', e, r)
            else:
                print(r['add_code'], '가 jo_acc에 없음')

        print(res[0])
        print('jo len:', len(jo))

        open(target_filename, 'w+').write(json.dumps(res))
        if self.mode == 0:
            pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

    def append_bank(self, before_turn_farm_filename, cnt_filename, target_filename):
        jo = json.loads(open(before_turn_farm_filename).read())
        jo_acc = json.load(open(cnt_filename, encoding='utf-8'))
        l = []
        for r in jo:
            if jo_acc.get(str(r['add_code'])) != None:
                acc = jo_acc[str(r['add_code'])]
                print(acc)

        # if self.mode == 0:
        #     self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')
