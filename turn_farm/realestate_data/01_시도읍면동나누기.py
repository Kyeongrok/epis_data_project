from libs.AddressManager import AddressManager
# file읽어서 0번 column을 시도 시군구 읍면동으로 나눈다

# 시군구 읍면동 중 여기에 포함되어 있는 데이터만 남긴다.
# 세종특별자치시는 시군구가 없다. 참고할 것

# 시군구 읍면동으로 addr_code를 찾는다.
am = AddressManager()

f_lst = am.get_file_list('./raw_data/*.csv')

for f_nm in f_lst:
    print(f_nm)


d

