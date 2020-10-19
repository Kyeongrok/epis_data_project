import json
import pandas as pd
from libs.AddressManager import AddressManager

class DataAppender():
    am = AddressManager()

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
        am = AddressManager()
        am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

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
                    print(rent_prices)
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
        am = AddressManager()
        am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

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
        self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

    def append_infra_accessibility(self, before_turn_farm_filename, cnt_file_name, target_filename):
        jo = json.loads(open(before_turn_farm_filename).read())
        jo_infra = json.load(open(cnt_file_name, encoding='utf-8'))

        res = []
        for r in jo:
            r['ARPRT_ACCES_POSBLTY'] = 0
            r['BUS_TRMINL_ACCES_POSBLTY'] = 0
            r['TRAIN_STATN_ACCES_POSBLTY'] = 0
            r['ELESCH_ACCES_POSBLTY'] = 0
            r['MSKUL_ACCES_POSBLTY'] = 0
            r['HGSCHL_ACCES_POSBLTY'] = 0
            r['PUBLIC_MLFLT_ACCES_POSBLTY'] = 0
            r['GNRL_HSPTL_ACCES_POSBLTY'] = 0
            r['GNRLZ_HSPTL_ACCES_POSBLTY'] = 0
            r['LRSCL_STOR_ACCES_POSBLTY'] = 0
            r['TRDIT_MRKT_ACCES_POSBLTY'] = 0

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
        pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

    def append_academy(self, before_filename, target_filename, cnt_filename):
        # load academy cnt
        d_academy_cnt = json.load(open(cnt_filename))

        l = []
        with open(before_filename) as f:
            jl = json.loads(f.read())
            for r in jl:
                add_cd = str(r['add_code'])
                add_cd = self.am.convert_to_adm_code_from_law_code(add_cd)
                if d_academy_cnt.get(add_cd) !=  None:
                    print(add_cd)
                    academy_cnt = d_academy_cnt[add_cd]['number']
                else:
                    academy_cnt = 0

                r['INSTUT_CO'] = academy_cnt
                l.append(r)

        open(target_filename, 'w+').write(json.dumps(l))
        self.am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')
