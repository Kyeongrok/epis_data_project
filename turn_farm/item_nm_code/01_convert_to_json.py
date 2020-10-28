from libs.AddressManager import AddressManager
import pandas as pd
am = AddressManager()

def extract_target_fields(from_excel_filename):
    # df로 불러와서 필요한 column만 뽑은 후
    df = pd.read_excel(from_excel_filename)
    df = df[['연번', '품목코드', '소분류']]
    df = df.drop_duplicates(['연번']) # distinct한 후
    df = df.set_index('연번')
    spl = from_excel_filename.replace('.xlsx', '').replace('farmers/','').split('년 ')
    df.to_json('farmer_{}_idx.json'.format(spl[0]), orient='index')

for i in range(7, 10):
    extract_target_fields('farmers/201{}년 경영주.xlsx'.format(i))

# am.csv_to_json('farmer_2019.csv')

# jo = am.json_from_json_file_nm('farmer_2019.json')
# am.export_to_index_json(jo, 'farmer_2019_idx.json', '연번', ['연번'])