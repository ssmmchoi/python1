'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자  > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''

from bs4 import BeautifulSoup
import os
os.getcwd()
# 1. html source 가져오기
file = open('./chap08_Crawling/data/login.html', mode='r', encoding='utf-8')
src = file.read()
print(src)

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. 선택자 이용 태그 내용 가져오기
# 조건1> id="login_wrap" 선택자의  하위 태그  전체 출력
login_wrap = html.find_all(id = 'login_wrap')
print(login_wrap)
# or
login = html.select_one('#login_wrap')
print(login)

# 조건2> id="login_warp" 선택자  > form > table 태그 내용 출력
tables = html.select('#login_wrap> form> table')
print(tables)

# 조건3> find_all('tr') 함수 이용  th 태그 내용 출력
trs = html.find_all('tr')
for tr in trs :
    ths = tr.find_all('th')
    for th in ths :
        print(th.string)
#  아이디
#  비밀번호








tmp = html.select('div[id="login_wrap"]')
print(tmp)
for t in tmp :
    trs = t.find_all('tr')
    for tr in trs :
        ths = tr.find_all('th')
        for th in ths :
            print(th.string)
#  아이디
#  비밀번호

