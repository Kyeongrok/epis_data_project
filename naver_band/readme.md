## 개요
crawl_subpage.py를 이용해 밴드의 데이터를 수집 합니다.

디버그 모드로 켠 크롬을 컨트롤 하며 데이터를 받아와서 저장하는 기능입니다.

## 크롬 디버그 모드로 열기
https://krksap.tistory.com/1730

위 포스트를 참고해서 크롬을 디버그 모드로 열 수 있습니다.

## 밴드 id 얻기
https://band.us/band/49246423

밴드에 들어가면 위와 같이 주소 표시줄에 나오는 숫자가 밴드의 id입니다. 


## Parsing Case
* 댓글에 사진과 대댓글 있음 : https://band.us/band/7727806/post/426020153
* 본문 + link형태 : https://band.us/band/7727806/post/426019864
* 본문 + a tag가 2개 이상 : https://band.us/band/7727806/post/426019980
