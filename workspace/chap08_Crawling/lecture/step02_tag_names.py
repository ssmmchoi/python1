'''
tag명으로 찾기
형식1) html.find('tag') : 최초로 발견된 tag element 가져오기
형식2) html.find_all('tag') : 해당 tag 전체 수집
'''

from bs4 import BeautifulSoup

# 1. local file 불러오기
import os
os.getcwd()
file = open("./chap08_Crawling/data/html01.html", mode='r', encoding='utf-8')
src = file.read()
print(src)  # 얜 파일을 읽어오면서 디코딩이 됐으므로 별도 디코딩 단계 필요 없음
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="UTF-8">
# <title> html5 - 시멘틱 태그 </title>
# </head>
# <body>
#    <h1> 시멘틱 태그 ?</h1>
#    <p> html5에서 웹문서에 의미를 부여하는 태그를 의미 </p>
#    <h2> 주요 시멘틱 태그 </h2>
#    <ul>
#       <li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>
#       <li> nav : 네이게이션(메뉴) </li>
#       <li> section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그</li>
#       <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>
#       <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>
#    </ul>
# </body>
# </html>

# 2. src->html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <title> html5 - 시멘틱 태그 </title>
# </head>
# <body>
# <h1> 시멘틱 태그 ?</h1>
# <p> html5에서 웹문서에 의미를 부여하는 태그를 의미 </p>
# <h2> 주요 시멘틱 태그 </h2>
# <ul>
# <li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>
# <li> nav : 네이게이션(메뉴) </li>
# <li> section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그</li>
# <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>
# <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>
# </ul>
# </body>
# </html>


# 3. tag 찾기 -> 내용 추출

# 1) tag
h1 = html.html.body.h1
print(h1)  # <h1> 시멘틱 태그 ?</h1>   : element
print(h1.string)  # 시멘틱 태그 ?   : 내용

# 2) find('tag')
h2 = html.find('h2')
print(h2)  # <h2> 주요 시멘틱 태그 </h2>
print(h2.string)  # 주요 시멘틱 태그

# 3) find_all('tag')  : 리스트나 튜플에 여러 개 저장
lis = html.find_all('li')
print(lis)
# [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>,
# <li> section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그</li>,
# <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>,
# <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>]
print(len(lis))  # 5

for li in lis :
    print(li.string)
#  header : 문서의 머리말(사이트 소개, 제목, 로그 )
#  nav : 네이게이션(메뉴)
#  section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그
#  aside : 문서의 보조 내용(광고, 즐겨찾기, 링크)
#  footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호)

li_cont = [li.string for li in lis]
print(li_cont)  # list
#[' header : 문서의 머리말(사이트 소개, 제목, 로그 )', ' nav : 네이게이션(메뉴) ', ' section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그',
# ' aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) ', ' footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) ']
