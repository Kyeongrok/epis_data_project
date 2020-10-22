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


da = DataAppender(1)
def run(num):
    if num == None or num == '':
        print('num is None or empty')
        exit()

    num = int(num)
    if num == 0 or num == 1:
        'academy'
        da.append_academy('turn_farm_fminf.json',
                          './academy_cnt/academy_cnt.json',
                          't_fm_acc_cult_cv_locfd_apc_instut.json')

    if num == 0 or num == 2:
        da.append_real_estate('t_fm_acc_cult_cv_locfd_apc_instut.json',
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
        da.append_infra_accessibility_cnt('t_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent_alter_school.json',
                               'infra_accessibility/2017_infra_accessibility_level2.json',
                               'tf_elem_middle.json')
    if num == 0 or num == 6:
        da.append_infra_accessibility_avg('tf_elem_middle.json',
                                          'infra_accessibility/2017_infra_accessibility.json',
                                          'tf_elem_middle_infra_avg.json')
    if num == 0 or num == 7:
        da.append_culture_center_library_museum('tf_elem_middle_infra_avg.json',
                                                './culture_center_library_etc/culture_museum_library_cnt.json',
                                                'tf_elem_middle_museum.json')
    if num == 0 or num == 8:
        da.append_bank(
            'tf_elem_middle_museum.json',
            './bank_cnt/bank_cnt.json',
            'tf_elem_middle_museum_bank.json'
        )

    if num == 0 or num == 9:
        da.append_culture_centers_avg(
            'tf_elem_middle_museum_bank.json',
            'culture_center_library_etc/culture_etc_cnt.json',
            'tf_elem_middle_museum_bank_culture_etc.json'
        )


    if num == 0 or num == 10:
        da.append_apc_cult_cv(
            'tf_elem_middle_museum_bank_culture_etc.json',
            'tf_elem_middle_museum_bank_culture_etc_apc.json',
        )
        da.append_avg(
            'tf_elem_middle_museum_bank_culture_etc_apc.json',
            'tf_elem_middle_museum_bank_culture_etc_avg.json'
        )

num = input('select number all:0 academy:1 realestate_price:2, realestate_rent:3, alter_school:4, infra_accessibility:5, museum_culture_center:6')

print(num)
run(num)