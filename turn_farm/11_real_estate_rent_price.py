# 부동산 가격 붙이기
import json
from libs.AddressManager import AddressManager

'''
LAD_BFE_TOP_AMOUNT
LAD_BFE_LWET_AMOUNT
LAD_RICFLD_AVRG_AMOUNT
LAD_RICFLD_TOP_AMOUNT
LAD_RICFLD_LWET_AMOUNT
ORCHRD_AVRG_AMOUNT
ORCHRD_TOP_AMOUNT
ORCHRD_LWET_AMOUNT
LAD_BFE_TOP_RENT_AMOUNT
LAD_BFE_LWET_RENT_AMOUNT
LAD_RICFLD_AVRG_RENT_AMOUNT
LAD_RICFLD_TOP_RENT_AMOUNT
LAD_RICFLD_LWET_RENT_AMOUNT
ORCHRD_AVRG_RENT_AMOUNT
ORCHRD_TOP_RENT_AMOUNT
ORCHRD_LWET_RENT_AMOUNT
'''

def append_real_estate(befor_filename, cnt_filename, target_filename):
    realestate_rent = json.load(open(cnt_filename))

    l = []
    with open(befor_filename) as f:
        jl = json.loads(f.read())
        for r in jl:
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
append_real_estate('t_fm_acc_cult_cv_locfd_apc_instut_real_estate.json','./realestate_data_rent/addr_code_real_estate_rent_prices.json', 't_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent.json')
