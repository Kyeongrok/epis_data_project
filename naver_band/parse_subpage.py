
from bs4 import BeautifulSoup
import re

def get_content(txtBody):
    con = ''
    for e in txtBody.descendants:
        if str(e) == '<br/>':
            con += '\n'
        else:
            con += str(e)
    return con

def parse_a_comment(cComment):
    # 댓글 쓰신 분0, 댓글 쓰신 날짜0, 댓글 body
    name = cComment.find('strong', {'class':'name'}).text
    comment_body = cComment.find('div', {'class':'commentBody _commentModification'})
    write_time = comment_body.find('div',{'class':'func'}).find('time', {'class':'time'})['title']
    commentContent = get_content(comment_body.find('p', {'class':'txt _commentContent'}))

    return {'cmt_name':name, 'cmt_wrt_time':write_time,'cmt_content':commentContent}

def parse_image_url(DPostPhotoView):
    return DPostPhotoView.find('img')['src']

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    postWriterInfoWrap = ''
    writer = ''

    try:
        postWriterInfoWrap = bsobj.find('div', {'class':'postWriter uFlexItem'})
        wr = postWriterInfoWrap.find('div',{'class':'postWriterInfoWrap'}).find('strong', {'class':'text'}).text
        writer = re.compile(r'[\n\r\t]').sub('',wr).strip()
    except Exception as e:
        print('error during parse writer')

    post_date = ''
    pstLstInfWrA = bsobj.find('div', {'class':'postListInfoWrap'}).find('a')
    post_url = pstLstInfWrA['href']
    post_date = postWriterInfoWrap.find('time').text
    pst_url_spl = post_url.split('/post/')
    post_id = pst_url_spl[1]
    band_id = pst_url_spl[0].split('/band/')[1]

    read_count = postWriterInfoWrap.find('span', {'class':'readCount'}).text
    read_count = read_count.split(' ')[0]


    sharePost = bsobj.find('div', {'class':'sharePost'})
    txt_body = ''
    image_urls = []
    if sharePost == None:
        postBody = bsobj.find('div', {'class':'postBody'})
        DPostPhotoViews = postBody.find_all('div', {'data-viewname':'DPostPhotoView'})
        image_urls = [parse_image_url(DPostPhotoView) for DPostPhotoView in DPostPhotoViews]
        DPostTextView = bsobj.find('div',{'class':'dPostTextView'})
        txt_body = get_content(DPostTextView.find('div', {'class':'txtBody'}))
    else:
        share_post_body = sharePost.find('p', {'class':'txtBody'})
        txt_body = get_content(share_post_body)

    comment_cnt = 0
    # 댓글
    comments = []
    sComments = bsobj.find('div', {'class':'sCommentList'}).find_all('div', {'class':'cComment'})
    comment_cnt = len(sComments)
    for i in range(len(sComments)):
        parsed_comment = parse_a_comment(sComments[i])
        parsed_comment['cmt_no'] = i + 1
        comments.append(parsed_comment)

    # comment obj만들 때 쓸것 왜냐하면 엑셀로 저장해야하는데 table형태로 가공해야함
    post_obj = {'writer':'', 'post_url':post_url, 'post_date':'', 'post_id':post_id, 'band_id':band_id,
            'read_count':'', 'txt_body':'', 'comment_cnt':''}

    return {'writer':writer, 'post_url':post_url, '':post_date, 'post_id':post_id, 'band_id':band_id,
            'read_count':read_count, 'txt_body':txt_body, 'comment_cnt':comment_cnt, 'comments':comments, 'image_urls':image_urls}

post_ids = [
    {'band_id':49247132, 'post_id':425435838},
    {'band_id':49247132, 'post_id':425435833},
    {'band_id':56517936, 'post_id':3460},
]


# subpage_url = https://band.us/band/49247132/post/425435833
# 49247132/html/425435838 SharedPost가 있음

for post_info in post_ids[2:3]:
    print(post_info)
    string = open('{}/html/{}.html'.format(post_info['band_id'], post_info['post_id']), encoding='utf-8').read()
    # print(parse(string)['txt_body'])
    print(parse(string))

# 49247132/post/425435833 본문 2줄, 본문사진1 댓글2
# 425435838

# 된거 : 년도, 게시자, 순번(id), 게시일시, URL, 조회수

# post의 이미지들 주소 -> 이건 나중에 저장 해야됨 ㅋㅋ 아 ㅋㅋ
# 댓글, 댓글의 이미지..... ㅁㅋㅋㅋㅋ
