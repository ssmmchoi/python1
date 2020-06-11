'''
1. 축약함수(lambda)
 - 한 줄 함수
   형식) 변수 = lambda 인수 : 리턴값
   ex) lambda x,y : x + y

2. scope
 - 전역변수, 지역변수

'''

# 1. 축약함수
def adder(x,y) :
    add = x + y
    return add

add = lambda x, y : x + y
# [lambda x,y : x+y for 변수 in 열거형객체]

re = add(10, 20)
print(re)  # 30

# 2. scope
'''
전역 변수 : 전지역에서 사용되는 변수
지역 변수 : 특정 지역(함수)에서만 사용되는 변수
'''

x = 50  # 전역변수

def local_func(x) :
    x += 50   # x가 100이 되는건 : 지역변수
    # 해당 함수가 종료되면 자동으로 소멸되는 변수

local_func(x)  # x = 50
print('x =', x)  # x = 50

def global_func() :
    global x # 전역변수   # x=0이라고 쓰면 x초기값이 0 인 전역변수 탄생
    x += 50

global_func()
print('x =', x)  # x = 100  전역변수네욤.
