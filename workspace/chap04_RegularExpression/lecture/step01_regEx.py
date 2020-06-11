'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

import re  # 방법1) 정규표현식 모듈
from  re import findall, match, sub  # 방법2) from 모듈 import 함수
'''
re.findall()  # 방법1)
findall()  # 방법2)
'''

# 1. findall
findall(pattern='정규식의 메타문자 패턴', string='문자열')

# 1) 숫자 찾기
print(re.findall('1234', st1))  # ['1234']  : list 반환
print(findall('[0-9]{3}', st1))  # ['123', '555']  : 연속 3개 숫자열을 list 반환
print(findall('[0-9]{3,}', st1))  # ['1234', '555']  : 연속 3개 이상 숫자열을 list 반환
print(findall('\\d{3,}', st1))  # ['1234', '555']
print(findall(r'\d{3,}', st1))  # ['1234', '555']

# 2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))  # ['홍길동', '이사도시']
print(findall('[a-z]{3,}', st1))  # ['abc']
print(findall('[a-z|A-Z]{3,}', st1))  # ['abc', 'ABC']

#
str_list = st1.split(sep=' ')
print(str_list)  # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names=[]
for s in str_list :
     tmp = findall('[가-힣]{3,}', s)
     print(tmp)         # [], ['홍길동'], [], ['이사도시']  : 빈 리스트는 해당 패턴과 일치하는 문자열 없다는 뜻

names = []
for s in str_list :
    tmp = findall('[가-힣]{3,}', s)
    if tmp : # [] -> F, [something] -> T
        names.append(tmp)
print(names)  # [['홍길동'], ['이사도시']]  : 중첩 list

names = []
for s in str_list :
    tmp = findall('[가-힣]{3,}', s)
    if tmp : # [] -> F, [something] -> T
        names.append(tmp[0])
print(names)  # ['홍길동', '이사도시']


# 3) 접두어 / 접미어 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('^test', st2))  # ['test']
print(findall('st$', st2))  # ['st']

# 종료문자 찾기
print(findall('.bc', st2))  # ['abc', 'mbc']  : 3자리, 끝 두자리는 bc인것
# 시작 문자 찾기
print(findall('t.', st2))  # ['te', 't1', 'te']

# 4) 단어 찾기(\\w) : word : 한글, 영문자 숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(findall('\\w{3,}', st3))  # ['test', '홍길동', 'abc', '123', 'tbc']  - list 반환

# 5) 특정 문자열 제외 [^x], +를 추가하면 1개 이상의 연속된 문자열로 변환
print(findall('[^t]+', st3))  # ['es', '^홍길동 abc 대한*민국 123$', 'bc'] : t 스팟을 기준으로 세 덩어리
print(findall('[^t]', st3))  # ['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']
# 특수 문자 제외
print(findall('[^^*$]+', st3))  # ['test', '홍길동 abc 대한', '민국 123', 'tbc']


# 2. match
# match(pattern='패턴', string='문자열')
# - 패턴 일치 여부 반환(일치: object  반환, 불일치 : NULL 반환)

jumin = '123456-1234567'
result = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result)  # <re.Match object; span=(0, 14), match='123456-1234567'>

if result :
    print('정상 주민번호')
else :  # None(NULL)
    print('비정상 주민번호')

jumin = '123456-5234567'
result2 = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result2)   # None


# 3. sub('pattern', 'rep', 'string')
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

result = sub('[\^*$]', '', st3)  # \^의 \는 ^를 메타데이터가 아닌 특수기호로 인식하겠다는 뜻
print(result)  # test홍길동 abc 대한민국 123tbc





