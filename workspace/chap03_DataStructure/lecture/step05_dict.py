'''
dict 특징
 - set 구조와 유사함(순서 없음, index 사용불가)
 - R의 List와 유사
 - key와 value 한 쌍으로 원소 구성
 - key -> value 참조
 - key 중복 불가, value 중복 가능
   형식) 변수 = {key1:값1, key2:값2, ...}
'''

# 1. dict 생성

# 방법1)
dic = dict(key1=100, key2=200, key3=300)
print(dic, len(dic), type(dic))  # {'key1': 100, 'key2': 200, 'key3': 300} 3 <class 'dict'>

# 방법2)
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(dic2)  # {'name': '홍길동', 'age': 35, 'addr': '서울시'}


# 2. 수정, 추가, 삭제, 검색 : key 이용
dic2['age'] = 45  # 수정
print(dic2)  # {'name': '홍길동', 'age': 45, 'addr': '서울시'}
dic2['pay'] = 350  # 추가
print(dic2)  # {'name': '홍길동', 'age': 45, 'addr': '서울시', 'pay': 350}
del dic2['addr']
print(dic2)  # {'name': '홍길동', 'age': 45, 'pay': 350}

# 키 검색
'age' in dic2  # True
print("age" in dic2)  # True

# 3. for 이용
for k in dic2 :
    print(k, end=" : ")    # name : age : pay :
# 즉, k는 value가 아니라 key이다.
# 다음과 같음.
for k in dic2.keys() :
    print(k, end="->")   # keys
    print(dic2[k], end=" ")   # values
# name->홍길동 age->45 pay->350

for v in dic2.values() :
    print(v, end=" ")     # 홍길동 45 350


for k, v in dic2.items() :  # key, value를 함께 넘김
    print(k, end='->')
    print(v)
# name->홍길동
# age->45
# pay->350

for d in dic2.items() :
    print(d, end=", ")   # ('name', '홍길동'), ('age', 45), ('pay', 350), : tuple 구조로 넘어옴


# 4. key -> value
print(dic2['name'])  # 홍길동  : index 형식
print(dic2.get('name'))  # 홍길동  : get() 형식
print(dic2.get(name))  # None  : fail.

# 5. {'key' : [value1, value2, ...]} - {'이름' : [급여, 수당]}
emp = {'hong' : [250, 50], 'lee' : [350, 80], 'yoo':[200,40]}
print(emp)  # {'hong': [250, 50], 'lee': [350, 80], 'yoo': [200, 40]}

for k, v in emp.items() :  # key, value
    print(k, end='->')
    print(v)
# hong->[250, 50]
# lee->[350, 80]
# yoo->[200, 40]

# 급여 250 이상인 사원 정보 출력
for k, v in emp.items() :
    if v[0] >= 250 :
        print(k, end='->')
        print(v)
# hong->[250, 50]
# lee->[350, 80]

# 급여 250 이상인 경우 사원명, 수당 합계
for k, v in emp.items() :
    if v[0] >= 250 :
        print(k, end=' : ')
        su = sum(v)
        print(su)
# hong : 300
# lee : 430

# 6. 문자 빈도수 구하기
charset = ['love','test','love','hello','test','love']
print(len(charset))  # 6
wc = {}

# 방법1)
for word in charset :
    if word in wc :
        wc[word] += 1
    else :
        wc[word] = 1 # 최초발견 : 1로 초기화( wc = {'love' : 1} )
print(wc)  # {'love': 3, 'test': 2, 'hello': 1}
max(wc, key=wc.get)  # 'love'

# 방법2)
wc2 = {}
for word in charset:
    wc2[word] = wc2.get(word, 0) + 1
print(wc2)

