'''
선택자(selector)
 - 웹 문서 디자인(css)에서 사용
 - 선택자 : id(#) : 중복 불가, class(.) : 중복 가능
 - html.select('선택자') : 여러 개 element 수집
 - html.select_one('선택자') : 한 개 element 수집
'''


from bs4 import BeautifulSoup

import os
os.getcwd()
file = open('./chap08_Crawling/data/html03.html', encoding='utf-8')
src = file.read()
print(src)

html = BeautifulSoup(src, 'html.parser')

# 테그 선택자 -> element 수집
# 1) id 선택자 : #
table = html.select_one('#tab')  # id = 'tab'
print(table)

# <table) <tr> <th> or <td>

ths = html.select('#tab > tr > th')
print(ths)
print(len(ths))  # 4

for th in ths :
    print(th.string)  # tag 내용


# 2) class 선택자 : .
trs = html.select('#tab > .odd')  # 5 <tr> 中 2 <tr>
print(trs)

for tr in  trs :
    #print(tr)
    tds = tr.find_all('td')  # list
    for td in tds :
        print(td.string)


# 3) tag[속성='값'] 찾기
trs = html.select("tr[class='odd']")  # 두 따옴표 유형을 달리해야 함.
print(trs)

for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)


