# 부동산 가격 붙이기
import json
from libs.AddressManager import AddressManager
from libs.DataAppender import DataAppender

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

da = DataAppender()

da.append_real_estate('t_fm_acc_cult_cv_locfd_apc.json',
                   './realestate_data/addr_code_real_estate_prices.json',
                   't_fm_acc_cult_cv_locfd_apc_instut_real_estate.json')
