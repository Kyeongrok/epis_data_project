from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+mysqldb://root:{}@localhost/{}?charset=utf8".format('', 'epis_bigdata_portal'), encoding='utf-8')
conn = engine.connect()

df = pd.read_json('incom_info_complete.json', encoding='utf-8')
df = df.rename(columns={
    '도명':'CTPRVN', '시군명':'SIGNGU',
    '작목명':'CROPS_NM', '기준면적':'STDR_AR', '총영농경력':'TOT_FARM_CAREER',
    '조사작목재배경력':'EXAMIN_CROPS_CTVT_CAREER',
    '조사작목재배면적_합계':'EXAMIN_CROPS_CTVT_AR',
    '주작목1_작목명':'MAIN_CROPS_NM',
    '주작목1_면적':'MAIN_CROPS_AR',
    '주품종1':'MAIN_SPCIES',
    '재배면적1':'MAIN_SPCIES_CTVT_AR',
    '재배기간_시작':'CTVT_PD_BEGIN',
    '재배기간_종료':'CTVT_PD_END',
    '수확기간_시작':'YL_PD_BEGIN',
    '수확기간_종료':'YL_PD_END',
    '재포기간':'RPT_PD',
    '재배유형':'CTVT_TY',
    '총수입_금액':'GR_INCME_AMOUNT',
    '주산물평가액_수량':'MAIN_FRMPRD_EVL_AMOUNT',
    '농가수취단가':'FRMHS_RECEPT_UNTPC',
    '농약비_비용':'AGCHM_CT',
    '경영비_비용':'MNGMT_CT',
    '자가노동시간_합계':'SELF_LABOR_TIME',
    '소득_금액':'INCOME_AMOUNT',
    '부가가치_금액':'ADI_VALU_AMOUNT',
    '소득률':'INCOME_RATE',
    '부가가치율':'ADI_VALU_RATE',
    '작물구분':'CROPS_SE',
    '총 재배면적(자가+임차)':'TOT_CTVT_AR'



})
print(df.count())
df = df[[
    'CTPRVN', 'SIGNGU', 'CROPS_NM','CROPS_SE',
    'STDR_AR', 'TOT_FARM_CAREER','EXAMIN_CROPS_CTVT_CAREER',
    'INCOME_DTA_CODE', 'PRDLST_CODE_WHSAL', 'PRDLST_CODE_ENTRPRS',
    'EXAMIN_CROPS_CTVT_CAREER',
    'EXAMIN_CROPS_CTVT_AR',
    'MAIN_CROPS_NM',
    'MAIN_CROPS_AR',
    'MAIN_SPCIES',
    'MAIN_SPCIES_CTVT_AR',
    'CTVT_PD_BEGIN',
    'CTVT_PD_END',
    'YL_PD_BEGIN',
    'YL_PD_END',
    'RPT_PD',
    'CTVT_TY',
    'GR_INCME_AMOUNT',
    'MAIN_FRMPRD_EVL_AMOUNT',
    'FRMHS_RECEPT_UNTPC',
    'AGCHM_CT',
    'MNGMT_CT',
    'SELF_LABOR_TIME',
    'INCOME_AMOUNT',
    'ADI_VALU_AMOUNT',
    'INCOME_RATE',
    'ADI_VALU_RATE',
    'TOT_CTVT_AR'
]]
df['PRDLST_CODE_KAMIS'] = ''

df.to_sql(name='T_RTRN_FARMER_PRDLST_INCOME_INFO_2', con=conn, if_exists='append', index=False)


