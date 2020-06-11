'''
원격 서버의 웹 수집
'''


from bs4 import BeautifulSoup  # source -> html 형식으로 파싱
import urllib.request as res  # 별칭 : 원격 서버 파일 요청

url = "http://www.naver.com/index.html"

# 1. 원격 서버에 url 요청
req = res.urlopen(url)  # 요청 -> 응답
print(req)  # object info
data = req.read()  # source
print(data)  # <!doctype html> -> source

# 2. source(문자열) -> html : html 파싱(특정한 데이터를 다른 포멧으로 변경하는 과정)
src = data.decode('utf-8')  # 디코딩 -> 소스
html = BeautifulSoup(src, 'html.parser')  # class()는 생성자 꼴. 외부의 인수를 넘겨받을 수 있음  : source -> html
print(html)

# 3. Tag 내용 가져오기
link = html.find('a')  #  <a href='url'>내용</a>
print(link)
# <a href="#news_cast" onclick="document.getElementById('news_cast2').tabIndex = -1;document.getElementById('news_cast2').focus();return false;"><span>연합뉴스 바로가기</span></a>

'''
element : <시작테그 속성명='값'>내용</종료테그>
'''
link.string  # 테그 내용 추출 : '연합뉴스 바로가기'
print('a 테그 내용 :', link.string)  # a 테그 내용 : 연합뉴스 바로가기

