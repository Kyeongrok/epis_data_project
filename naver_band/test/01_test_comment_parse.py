from naver_band.parse_subpage import parse

file = open('../7727806/html/212883265.html', encoding='utf-8').read()

print(parse(file)['post_body'])


