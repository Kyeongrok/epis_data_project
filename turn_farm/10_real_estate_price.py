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

def run(num):
    if num == None or num == '':
        print('num is None or empty')
        exit()

    num = int(num)
    if num == 0 or num == 1:
        'academy'
        da.append_academy('t_fm_acc_cult_cv_locfd_apc.json', 't_fm_acc_cult_cv_locfd_apc_instut.json', './academy_cnt/academy_cnt.json')

    if num == 0 or num == 2:
        da.append_real_estate('t_fm_acc_cult_cv_locfd_apc.json',
                           './realestate_data/addr_code_real_estate_prices.json',
                           't_fm_acc_cult_cv_locfd_apc_instut_real_estate.json')
    if num == 0 or num == 3:
        # rent
        da.append_real_estate_rent('t_fm_acc_cult_cv_locfd_apc_instut_real_estate.json',
                                   './realestate_data_rent/addr_code_real_estate_rent_prices.json',
                                   't_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent.json')
    if num == 0 or num == 4:
        '''alter school'''
        da.alter_school('t_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent.json',
                        './alter_school/alter_school_cnt.json',
                        't_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent_alter_school.json')

    if num == 0 or num == 5:
        da.append_infra_accessibility('t_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent_alter_school.json',
                               'infra_accessibility/2017_infra_accessibility_level2.json',
                               'tf_elem_middle.json')

num = input('select number all:0 academy:1 realestate_price:2, realestate_rent:3, alter_school:4, infra_accessibility:5')

print(num)
run(num)