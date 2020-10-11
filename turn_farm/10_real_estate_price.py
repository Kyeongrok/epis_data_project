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

def append_real_estate(befor_filename, target_filename):
    realestate_buy_sell = json.load(open('./realestate_data/addr_code_real_estate_prices.json'))
    realestate_rent = json.load(open('./realestate_data_rent/addr_code_real_estate_rent_prices.json'))

    l = []
    with open(befor_filename) as f:
        jl = json.loads(f.read())
        for r in jl:
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
                r['LAD_BFE_TOP_AMOUNT'] = buy_sell_prices['LAD_BFE_TOP_AMOUNT']
                r['LAD_BFE_LWET_AMOUNT'] = buy_sell_prices['LAD_BFE_LWET_AMOUNT']
                r['LAD_RICFLD_AVRG_AMOUNT'] = buy_sell_prices['LAD_RICFLD_AVRG_AMOUNT']
                r['LAD_RICFLD_TOP_AMOUNT'] = buy_sell_prices['LAD_RICFLD_TOP_AMOUNT']
                r['LAD_RICFLD_LWET_AMOUNT'] = buy_sell_prices['LAD_RICFLD_LWET_AMOUNT']
                r['ORCHRD_AVRG_AMOUNT'] = buy_sell_prices['ORCHRD_AVRG_AMOUNT']
                r['ORCHRD_TOP_AMOUNT'] = buy_sell_prices['ORCHRD_TOP_AMOUNT']
                r['ORCHRD_LWET_AMOUNT'] = buy_sell_prices['ORCHRD_LWET_AMOUNT']

            l.append(r)

    open(target_filename, 'w+').write(json.dumps(l))
    am = AddressManager()
    am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')
append_real_estate('t_fm_acc_cult_cv_locfd_apc.json', 't_fm_acc_cult_cv_locfd_apc_instut_real_estate.json')
