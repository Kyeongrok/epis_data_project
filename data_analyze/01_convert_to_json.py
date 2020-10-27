import pandas as pd


df = pd.read_excel('C:\\Users\\ocean\\Desktop\\2019 데이터셋\\01.DB농업경영체\\☆(200916) 농업경영체 추출 1부(2015~2019년 경영주, 경영주외농업인)\\2019년 경영주.xlsx')

print(df.columns)
df = df.rename(columns={
       '연번':'code',
       '경영체등록년도':'reg_year',
       '영농경력':'career',
       '경영주시도':'live_sido',
       '경영주시군구':'live_sigungu',
       '경영주읍면동':'live_emd',
       '성별':'gender',
       '나이':'age',
       '취업동기':'motivation',
       '농업종사형태':'farm_type',
       '농지시도':'farm_sido',
       '농지시군구':'farm_sigungu',
       '농지읍면동':'farm_emd',
       '품목코드':'prd_code',
       '대분류':'category_level_1',
       '중분류':'category_level_2',
       '소분류':'category_level_3'
})
df.to_json('2019_farmer.json', orient='records')

