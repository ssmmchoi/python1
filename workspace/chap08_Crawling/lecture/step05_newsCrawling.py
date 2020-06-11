'''
1. news Crawling
   url : http://media.daum.net
2. pickle save
   binary file save : 객체 그대로 유지해서 저장
'''

import urllib.request as req  # url요청
from bs4 import BeautifulSoup  # html 파싱

url = 'http://media.daum.net'

# 1. url 요청
res = req.urlopen(url)
src = res.read()  # source
print(src)

# 2. html parsing
data = src.decode('utf-8')
html = BeautifulSoup(data, 'html.parser')
print(html)

# 3. tag[속성='값'] -> 'a[class="link_txt"]'
links = html.select('a[class="link_txt"]')
print(len(links))  # 62
print(links)

crawling_data = []  # 빈 list

for link in links :
    link_str = str(link.string)  # 내용 추출
    crawling_data.append(link_str.strip()) # 문장 끝에 오는 불용어 처리(\n, 공백, ...)

print(crawling_data)  # list
# ["민주당-정부 재난지원금 '밀당'..5월 지급 가능할까?", '이인영 "여야, 재난지원금 전국민 지급 약속 실천해야"', '여야 원내대표, 오후 회동..재난지원금 전국민 지급 논의',  ...]
print(len(crawling_data))  # 62

# 4. pickle file save
import pickle

file = open('./chap08_Crawling/data/new_crawling.pickle', mode='wb')
pickle.dump(crawling_data, file)
print('pickle file saved')

