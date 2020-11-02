'''
6개 excel file불러온다
df로 변환한다
합친다
json으로 저장한다.
'''

from libs.AddressManager import AddressManager
import pandas as pd


am = AddressManager()

fi_li = am.get_file_list('2019/*.xlsx')

l_df = [None] * len(fi_li)

for i in range(1, len(fi_li)):
    nm = fi_li[i]
    # df만든다.
    # 하나로 합친다
    df = pd.read_excel(nm)
    category = nm.split('\\')[1].split('_')[0]
    print(nm, df.shape)
    # 필요한 열만 고른다.
    df = df[['도명', '시군명', '작목명', '기준면적', '총 재배면적(자가+임차)', '총영농경력',
             '조사작목재배경력', '조사작목재배면적_합계', '주작목1_작목명', '주작목1_면적',
             '주품종1', '재배면적1', '재배기간_시작', '재배기간_종료', '수확기간_시작', '수확기간_종료',
             '재포기간', '재배유형', '총수입_금액', '주산물평가액_금액', '주산물평가액_수량', '농가수취단가', '농약비_비용', '경영비_비용',
             '자가노동시간_합계', '소득_금액', '부가가치_금액', '소득률', '부가가치율']]
    df['작물구분'] = category
    print(nm, df.shape)
    l_df[i] = df
df_r = pd.concat(l_df)
print(df_r.shape)
df_r = df_r[df_r['기준면적'] != '평']
df_r = df_r[df_r['도명'] != '']
print(df_r.shape)
df_r.to_json('income_info.json', orient='records')
df_r.to_excel('income_info.xlsx')



