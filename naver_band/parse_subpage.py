
from bs4 import BeautifulSoup

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    postListInfoWrap = bsobj.find('div', {'class':'postListInfoWrap'})
    print(postListInfoWrap)

string = open('49247132/html/425435833.html', encoding='utf-8').read()

parse(string)

# 된거 : 년도, 게시자, 순번(id), 게시일시, URL, 조회수

# 게시내용	댓글수
# 댓글작성자	댓글내용	댓글작성일시
# post의 이미지들 주소 -> 이건 나중에 저장 해야됨 ㅋㅋ 아 ㅋㅋ
# 댓글, 댓글의 이미지..... ㅁㅋㅋㅋㅋ
