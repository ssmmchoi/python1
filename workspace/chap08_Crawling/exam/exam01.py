'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건> <tr> 태그 하위 태그인 <th> 태그의 모든 내용 출력
    
   <출력 결과>
   th 태그 내용 
    아이디 
    비밀번호 
'''

from bs4 import BeautifulSoup

# 1. 파일 읽기 
file = open("./chap08_Crawling/data/login.html", mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

# 3. 태그 찾기 
ths = html.find_all('th')
print(ths)  # [<th> 아이디 </th>, <th> 비밀번호 </th>]
print(len(ths))  # 2

# 4. 태그 내용 출력 
for th in ths :
    print(th.string)
#  아이디
#  비밀번호


#### 답 :
print('th 테그 내용')
for th in ths :
    print(th.string)
'''
th 테그 내용
 아이디 
 비밀번호 
 '''





# 5. tr 테그로 찾기
trs = html.find_all('tr')
print(trs)
# <tr> -> <th> tag 찾기
print('\n<tr> 테그로 찾기')
for tr in trs:
    th = tr.find('th')
    print(th.string)