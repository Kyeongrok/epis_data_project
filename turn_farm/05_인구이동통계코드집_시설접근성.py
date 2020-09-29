import pandas as pd
# 시설접근성에 시도 군구 읍면동으로  add_code넣기

# 코드집 불러오기
# 시설교통 접근성 불러오기

df_addr_code = pd.read_excel('C:/Users/ocean/Desktop/2017 인구이동통계 코드집_공공용.xlsx', sheet_name='행정구역코드 등록 및 말소 내역')
df_acc = pd.read_excel('C:/Users/ocean/Desktop/시설접근성_2017 교통접근성지표_작업.xlsx', sheet_name='db')

# 접근성 행정구역코드	행정구역시도명	행정구역시군구명	행정구역읍면동명	시설물대분류	시설물소분류	평균접근시간(분)
# 코드집 행정동코드	시도명	시군구명	읍면동명	생성일자	말소일자

df_addr_code = df_addr_code.rename(columns={'시도명':'행정구역시도명', '시군구명':'행정구역시군구명', '읍면동명':'행정구역읍면동명'})
print(df_addr_code.count())
print(df_addr_code.shape)
print(df_acc.shape)

df_m = pd.merge(df_acc, df_addr_code, on=['행정구역시도명', '행정구역시군구명', '행정구역읍면동명'])

df_m.to_excel('2017시설접근성_add_code.xlsx')

# turn_farm_2019와 합치기
# 행정구역코드	행정구역시도명	행정구역시군구명	행정구역읍면동명	시설물대분류	시설물소분류	평균접근시간(분)	행정동코드	생성일자	말소일자
# 정규화가 안되어 있다 그냥 넣는다.

# sheet3 불러와서 json으로 저장


