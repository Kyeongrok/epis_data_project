from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+mysqldb://root:{}@localhost/{}?charset=utf8".format('', 'epis_bigdata_portal'), encoding='utf-8')
conn = engine.connect()

df = pd.read_json('tf_elem_middle.json', encoding='utf-8')
df = df.rename(columns={
    'code':'CODE', 'farm_id':'FRMHS_ID', 'add_code':'ADRES_CODE',
    'addr1':'CTPRVN', 'addr2':'SIGNGU', 'addr3':'EMD',
'f.add_code':'FRMHS_ADRES_CODE',
'f.addr1':'MVT_CTPRVN',
'f.addr2':'MVT_SIGNGU',
'f.addr3':'MVT_EMD',
'p1.age':'MNGMT_OWNR_AGE',
'p1.sex':'MNGMT_OWNR_SEXDSTN',
'toddler':'INFANT_CHLDRN_ENNC',
'kinder':'CHILD_CHLDRN_ENNC',
'elem':'SCHBOY_CHLDRN_ENNC',
'middle':'MSKLSD_CHLDRN_ENNC',
'high':'HGSCHST_CHLDRN_ENNC',
'parents':'PARNTS_SUPORT_AT',
'child':'SCHBOY_BELOW_CHLDRN_ENNC',
'teenager':'MSKLSD_HGSCHST_CHLDRN_ENNC',
'age_c':'MNGMT_OWNR_AGE_SCTN',

'index7':'INDEX_'
})
df = df[['CODE', 'FRMHS_ID', 'ADRES_CODE',
        'CTPRVN',
        'SIGNGU',
        'EMD',
        'FRMHS_ADRES_CODE',
        'MVT_CTPRVN',
        'MVT_SIGNGU',
        'MVT_EMD',
        'MNGMT_OWNR_AGE',
        'MNGMT_OWNR_SEXDSTN',
        'INFANT_CHLDRN_ENNC',
        'CHILD_CHLDRN_ENNC',
        'SCHBOY_CHLDRN_ENNC',
        'MSKLSD_CHLDRN_ENNC',
        'HGSCHST_CHLDRN_ENNC',
        'PARNTS_SUPORT_AT',
        'SCHBOY_BELOW_CHLDRN_ENNC',
        'MSKLSD_HGSCHST_CHLDRN_ENNC',
'LAD_BFE_AVRG_DELNG_AMOUNT',
'LAD_BFE_TOP_DELNG_AMOUNT',
'LAD_BFE_LWET_DELNG_AMOUNT',
'LAD_RICFLD_AVRG_DELNG_AMOUNT',
'LAD_RICFLD_TOP_DELNG_AMOUNT',
'LAD_RICFLD_LWET_DELNG_AMOUNT',
'ORCHRD_AVRG_DELNG_AMOUNT',
'ORCHRD_TOP_DELNG_AMOUNT',
'ORCHRD_LWET_DELNG_AMOUNT',
'LAD_BFE_AVRG_RENT_AMOUNT',
'LAD_BFE_TOP_RENT_AMOUNT',
'LAD_BFE_LWET_RENT_AMOUNT',
'LAD_RICFLD_AVRG_RENT_AMOUNT',
'LAD_RICFLD_TOP_RENT_AMOUNT',
'LAD_RICFLD_LWET_RENT_AMOUNT',
'ORCHRD_AVRG_RENT_AMOUNT',
'ORCHRD_TOP_RENT_AMOUNT',
'ORCHRD_LWET_RENT_AMOUNT',
'ALTRV_ELESCH_AT',
'ALTRV_ELESCH_MSKUL_HGSCHL_AT',
'ALTRV_ELESCH_MSKUL_AT',
'ALTRV_MSKUL_AT',
'ALTRV_MSKUL_HGSCHL_AT',
'ALTRV_HGSCHL_AT'
         ]]
df.to_sql(name='t_rtrn_farmer_data_set2', con=conn, if_exists='append', index=False)
# print(df)


