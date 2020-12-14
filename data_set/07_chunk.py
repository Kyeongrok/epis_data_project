import pandas as pd
from libs.FileManager import FileManager
fm = FileManager()

path = 'C:/Users/ocean/Desktop/빅데이터셋 3종/*.json'

fnms = fm.get_file_list(path)
print(fnms[11])
df = pd.read_json(fnms[11], chunksize=1000, lines=True)

print(df.count())



