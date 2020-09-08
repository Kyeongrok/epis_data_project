
from bs4 import BeautifulSoup
import re

def get_content(txtBody):
    if txtBody == None:
        return ''

    con = ''
    for e in txtBody.descendants:
        # print(e.name, e)
        if e.name == 'br':
            con += '\n'
        elif e.name == 'a':
            con += e.text
        else:
            con += str(e)
    return con

def get_comment_content(txtBody):
    con = ''
    if txtBody == None:
        return ''
    for e in txtBody.descendants:
        if str(e) == '<br/>':
            con += '\n'
        elif e.name == 'a':
            con += e.text
            if e.get('href') != None:
                con += e.get('href')
        else:
            con += str(e)
    return con


def parse_a_comment(cComment):
    # 댓글 쓰신 분0, 댓글 쓰신 날짜0, 댓글 body
    name = cComment.find('strong', {'class':'name'}).text
    comment_body = cComment.find('div', {'class':'commentBody'})
    func = comment_body.find('div',{'class':'func'})
    write_time = func.find('time', {'class':'time'})['title']
    commentContent = get_comment_content(comment_body.find('p', {'class':'txt _commentContent'}))

    # 사진 url
    cmt_img_url = ''
    DCommentAttachedPhotoView = cComment.find('a', {'data-viewname':'DCommentAttachedPhotoView'})
    if DCommentAttachedPhotoView != None:
        cmt_img_url = DCommentAttachedPhotoView.find('img')['src']

    return {'cmt_name':name, 'cmt_wrt_time':write_time,'cmt_content':commentContent, 'cmt_img_url':cmt_img_url}

def parse_comments(sComments):
    comments = []
    comment_cnt = 0
    for i in range(len(sComments)):
    # for i in range(2, 3):
        comment_cnt += 1
        # try:
        parsed_comment = parse_a_comment(sComments[i])
        parsed_comment['cmt_no'] = comment_cnt
        comments.append(parsed_comment)
        # except Exception as e:
        #     print('comment_cnt:{}'.format(comment_cnt), e)
    return comments

def parse_image_url(DPostPhotoView):
    return DPostPhotoView.find('img')['src']

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    postWriterInfoWrap = ''
    writer = ''
    post_date = ''

    try:
        postWriterInfoWrap = bsobj.find('div', {'class':'postWriter uFlexItem'})
        wr = postWriterInfoWrap.find('div',{'class':'postWriterInfoWrap'}).find('strong', {'class':'text'}).text
        writer = re.compile(r'[\n\r\t]').sub('',wr).strip()
    except Exception as e:
        print('error during parse writer')

    # post info 없으면 안되는 정보들
    pstLstInfWr = bsobj.find('div', {'class':'postListInfoWrap'})
    pstLstInfWrA = pstLstInfWr.find('a')
    post_url = pstLstInfWrA['href']
    post_date = postWriterInfoWrap.find('time').text
    pst_url_spl = post_url.split('/post/')
    post_id = pst_url_spl[1]
    band_id = pst_url_spl[0].split('/band/')[1]

    read_count = postWriterInfoWrap.find('span', {'class':'readCount'})
    if read_count != None:
        read_count = read_count.text.split(' ')[0]

    postReadersA = bsobj.find('div', {'class':'readNotice _postReaderWrap'}).find('p', {'class':'_postReaders'}).find('a')
    if postReadersA != None:
        read_count = postReadersA.find('strong').text

    sharePost = bsobj.find('div', {'class':'sharePost'})
    post_body = ''
    image_urls = []
    if sharePost == None:
        postBody = bsobj.find('div', {'class':'postBody'})
        DPostPhotoViews = postBody.find_all('div', {'data-viewname':'DPostPhotoView'})
        image_urls = [parse_image_url(DPostPhotoView) for DPostPhotoView in DPostPhotoViews]
        DPostTextView = bsobj.find('div',{'class':'dPostTextView'})
        if DPostTextView != None:
            txtBody = DPostTextView.find('div',{'class':'postText _postText'}).find('div', {'class':'txtBody'})
            post_body = get_content(txtBody)
    else:
        share_post_body = sharePost.find('p', {'class':'txtBody'})
        photoRegion = sharePost.find('div', {'class':'_attachmentPhotosRegion'})
        DPhotoCollageView = photoRegion.find('ul', {'data-viewname': 'DPhotoCollageView'})
        if DPhotoCollageView != None:
            photoLis = DPhotoCollageView.find_all('li')
            image_urls = [li.find('img')['src'] for li in photoLis]

        try:
            post_body = get_content(share_post_body)
        except Exception as e:
            print('shared post body not exist')
        # text_body가 없는 경우가 있음

    # 댓글
    sCommentList = bsobj.find('div', {'class':'sCommentList'})
    # print(sCommentList)
    sComments = sCommentList.find_all('div', {'class':'cComment'})
    comments = parse_comments(sComments)
    comment_cnt = len(comments)
    print('comment_cnt:{}'.format(comment_cnt))

    # comment obj만들 때 쓸것 왜냐하면 엑셀로 저장해야하는데 table형태로 가공해야함
    post_obj = {'writer':'', 'post_url':post_url, 'post_date':'', 'post_id':post_id, 'band_id':band_id,
            'read_count':'', 'post_body':'', 'comment_cnt':''}

    return {'writer':writer, 'post_url':post_url, 'post_date':post_date, 'post_id':post_id, 'band_id':band_id,
            'read_count':read_count, 'post_body':post_body, 'comment_cnt':comment_cnt,
            'comments':comments, 'image_urls':image_urls}

post_ids = [
    {'band_id':49247132, 'post_id':425435838},
    {'band_id':49247132, 'post_id':425435833},
    {'band_id':56517936, 'post_id':3460},
]


# subpage_url = https://band.us/band/49247132/post/425435833
# 49247132/html/425435838 SharedPost가 있음


# 49247132/post/425435833 본문 2줄, 본문사진1 댓글2
# 425435838


# 댓글의 이미지.
