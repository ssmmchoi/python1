'''
tag 속성과 내용 가져오기
 - element : tag + 속성 + 내용
   ex) <a href="www.naver.com">네이버</a>
       a : tag
       href : 속성(attribute)
       네이버 : 내용(content)
'''

from bs4 import BeautifulSoup

# 1. local file 가져오기
file = open("./chap08_Crawling/data/html02.html", encoding='utf-8')
src = file.read()

# 2. html 피싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. a 테그 엘리먼트 찾아오기
links = html.find_all('a')
print(links)
# [<a href="www.naver.com">네이버</a>, <a href="http://www.naver.com">네이버</a>,
# <a href="http://www.naver.com" target="_blank">네이버 새창으로</a>,
# <a href="www.duam.net">다음</a>, <a href="http://www.duam.net">다음</a>]

# 4. a 테그 -> 속성(href(5), target(1))
urls = []
for link in links :
    print(link.string)  # 내용
    atts = link.attrs  #  속성. dict
    print(atts)

    urls.append(atts['href'])  # value

    try:
        print(atts['target'])  # 타겟이 있는 엘리먼트도 있고 없는 엘리먼트도 있음. 그냥 넣으면 오류발생  'blank'
    except Exception as e :
        print('예외 발생 :', e)
    finally:
        print('*'*20)
# 네이버
# {'href': 'www.naver.com'}
# 예외 발생 : 'target'
# ********************
# 네이버
# {'href': 'http://www.naver.com'}
# 예외 발생 : 'target'
# ********************
# 네이버 새창으로
# {'href': 'http://www.naver.com', 'target': '_blank'}
# _blank
# ********************
# 다음
# {'href': 'www.duam.net'}
# 예외 발생 : 'target'
# ********************
# 다음
# {'href': 'http://www.duam.net'}
# 예외 발생 : 'target'
# ********************

print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
print(len(urls))  # 5

# urls -> 정상 url을 -> new_urls  : pattern 이용
import re  # findall, match, sub
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net'] 중 3개


new_urls = []
print('findall 사용 예')
for url in urls:
    tmp = re.findall('^http://', url)
    if tmp :  # 일치된 경우
        new_urls.append(tmp)
print(new_urls)
# findall 사용 예
# [['http://'], ['http://'], ['http://']]


new_urls.clear()  # list 원소제거

print('match 사용 예')
for url in urls :
    tmp = re.match('^http://', url)
    if tmp :
        new_urls.append(url)
print(new_urls)

# match 사용 예
# ['http://www.naver.com', 'http://www.naver.com', 'http://www.duam.net']

