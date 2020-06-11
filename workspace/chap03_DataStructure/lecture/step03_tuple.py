'''
tuple 특징
 - index 사용, 순서 존재
 - 1차원 배열 구조
 - list와 차이점: 수정 불가, 리스트에 비해 처리 속도 빠름
 - 따라서 제공 함수 없음
   형식) 변수 = (원소1, 원소2, ...)
'''

tp = 10  # scala
tp1 = (10)  # scala
print(tp, tp1)  # 10 10
print(type(tp), type(tp1))  # <class 'int'> <class 'int'>

tp2 = (10, )
print(tp2, type(tp2))  # (10,) <class 'tuple'>

# index
tp3 = (10, 58, 4, 96, 55, 2)
tp3[:4]  # (10, 58, 4, 96)
tp3[-3:]  # (96, 55, 2)

#  수정 불가
# tp3[0] = 100  ### Type Error

# max/min
vmax = vmin = tp3[0]  # 첫 번째 원소로 초기화
for t in tp3 :
    if vmax < t :
        vmax = t
    if vmin > t :
        vmin = t
print('최댓값 =', vmax)  # 최댓값 = 96
print('최솟값 =', vmin)  # 최솟값 = 2

# list -> tuple
lst = list(range(10000))
print(len(lst))  # 10000

tlst = tuple(lst)
print(type(tlst))  # <class 'tuple'>

# 튜플 대입 연산
student1 = ("철수", 19, "CS")
(name, age, major)  = student1
name  # '철수'
age  # 19
major  # 'CS'


