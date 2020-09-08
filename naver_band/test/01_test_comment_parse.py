from naver_band.parse_subpage import parse

file = open('429301312.html', encoding='utf-8').read()

print(parse(file)['post_body'])


