import pandas as pd
import os
import glob
from threading import Thread

def convert(idx, fileName):
    print(fileName)
    df = ''
    df = pd.read_csv(fileName, sep='|', encoding='utf-8',dtype={'읍면':'str','읍면영문':'str',
                                                                '도로명코드':'str', '법정동코드':'str','법정동명' :'str', '리명':'str'})
    # 도로명 주소가 있는 파일을 불러온다.
    do = fileList[0].split('\\')[1].split('.')[0]
    df = df[['시도', '시군구', '읍면', '법정동코드', '도로명']]
    return df
fileList = glob.glob('C:/Users/ocean/Desktop/zipcode_DB/'+"*.txt")

threads = [None] * len(fileList)
frames = []
for i in range(len(fileList)):
    # threads[i] = Thread(target=convert, args=(i, fileList[i]))
    # threads[i].start()
    frames.append(convert(1, fileList[i]))

df_result = pd.concat(frames, ignore_index=True)
path = os.getcwd()
df_result.to_json('road_name.json')
