'''
set 특징
 - 순서 없음(index 사용 불가) : 올 땐 순서 있어도 갈 땐 순서 없다..
 - 중복 허용 불가(partition 없으므로..)
   형식) 변수 = {값1, 값2, ...}
 - 집합 개념
'''

s = {1,3,5}
print(s)  # {1, 3, 5}
s = {3,1,5}
print(s)  # {1, 3, 5}
print(len(s))  # 3

s = {1,3,5,1,5}
print(s, len(s), sep=" : ")  # {1, 3, 5} : 3

for d in s :
    print(d, end=' ')    # 1 3 5


s2 = {3,6}
# 집합 관련 함수
print(s.union(s2))  # {1, 3, 5, 6}  : 합집합
print(s.difference(s2))  # {1, 5}  : 차집합
print(s.intersection(s2))  # {3}  : 교집합


# list : gender
gender = ['남자','여자', '남자', '여자']   # 중복 허용
sgender = set(gender)
print(sgender)  # {'남자', '여자'}
# print(sgender[0])  # TypeError


# set -> list
lgender = list(sgender)
print(lgender)  # ['남자', '여자']
print(lgender[0])  # 남자


#  원소 추가/삭제는 가능함
s3 = {1,3,5,7}
print(s3, type(s3))  # {1, 3, 5, 7} <class 'set'>

s3.add(9)
print(s3)  # {1, 3, 5, 7, 9}
s3.remove(9)
print(s3)  # {1, 3, 5, 7}
s3.discard(1)
print(s3)  # {3, 5, 7}