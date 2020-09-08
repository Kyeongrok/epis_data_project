import glob
from naver_band.single_page_parser import parse

def fn(band_id):
    fileList = glob.glob('./{}/pages/'.format(band_id) + "*.html")

    result = set([])
    for file_name in fileList:
        print(file_name)
        string = open(file_name, encoding='utf-8').read()
        result = result.union(set(parse(string)))
    return result

band_id = 49247132
result = fn(band_id)
print(result)
open('{}/{}_post_ids.json'.format(band_id, band_id), 'w+').write(str(result))

