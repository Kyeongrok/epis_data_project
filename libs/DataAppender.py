import json
from libs.AddressManager import AddressManager

class DataAppender():
    def append_academy(self):
        pass
    def append_real_estate(self, befor_filename, cnt_filename, target_filename):
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

    def append_real_estate(self, befor_filename, cnt_filename, target_filename):
        realestate_buy_sell = json.load(open(cnt_filename))

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
