
'''
중첩함수(inner function)

형식)
def outer_func(인수) :
    실행문
    def inner_func(변수) :
        실행문

    return inner_func
'''

# 1. 중첩함수 예
def a() : # outer
    print('function a')
    def b () : # inner
        print('function b')
    return b  # Inner func

a()  # call out outer function
# function a
# <function a.<locals>.b at 0x00000161A5318C18>

b=a()  # outer 호출  : function a : 일급함수(inner 함수를 객체로 받은??)
b()  # inner 호출  : function b

# 2. 중첩함수 응용
'''
inner 함수 종류
getter() : 함수내에서 사용하는 data를 외부로 꺼내오는 획득자 
setter() : 함수내에서 사용하는 data를 조작하는 지정자
'''

def outer_func(data) :  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner:데이터 조작
    def tot() :  # 합계
        tot_val = sum(dataSet)
        return  tot_val
    def avg(tot_val) :  # 평균
        avg_val = tot_val / len(dataSet)
        return  avg_val

    return tot, avg

data = list(range(1,101))
tot, avg = outer_func(data)  # 일급함수(tot, avg)

tot_val = tot()  # 합계 계싼
avg_val = avg(tot_val)  # 평균 계산
print('tot =', tot_val)  # tot = 5050
print('avg =', avg_val)  # avg = 50.5



def outer_func(data) :  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner:데이터 조작
    def tot() :  # 합계
        tot_val = sum(dataSet)
        return  tot_val
    def avg(tot_val) :  # 평균
        avg_val = tot_val / len(dataSet)
        return  avg_val
    def getData() :
        return dataSet

    return tot, avg, getData

data = list(range(1,101))
tot, avg, getData = outer_func(data)  # 일급함수(tot, avg)
tot_val = tot()  # 합계 계싼
avg_val = avg(tot_val)  # 평균 계산

print('tot =', tot_val)
print('avg =', avg_val)
print('dataset =', getData())  # dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def outer_func(data) :  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner:데이터 조작
    def tot() :  # 합계
        tot_val = sum(dataSet)
        return  tot_val
    def avg(tot_val) :  # 평균
        avg_val = tot_val / len(dataSet)
        return  avg_val

    # getter
    def getData() :
        return dataSet
    # setter
    def setData(newData) :
        nonlocal  dataSet  # 2. outer 변수가 됨
        dataSet = newData  # 1. 흐린 dataSet는 지역변수

    return tot, avg, getData, setData

data = list(range(1,101))
tot, avg, getData, setData = outer_func(data)  # 일급함수(tot, avg)

newData = list(range(1,51))
setData(newData)  # dataSet 변경

# getter 이용 : dataSet 확인
print('dataSet =', getData())  # dataSet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print('')


# 3. 함수 장식자 : Tensorflow2.0
# - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식해주는 역할
'''
@함수장식자
def 함수명() :
    실행문
'''

# 함수장식자 작성
def hello_deco(func) : # outer : 함수를 인수로 받음
    def inner() :  # 함수 장식하는 역할
        print('-'*20)  # 함수 앞부분
        func()  # 함수 실행
        print('-'*20)  # 함수 뒷부분
    return  inner

@hello_deco
def hello() :
    print('My name is 홍길동!!')

# 함수 호출
hello()
# --------------------
# My name is 이순신!!
# --------------------



def hello_deco(func) : # outer : 함수를 인수로 받음
    def inner(name) :  # 함수 장식하는 역할
        print('-'*20)  # 함수 앞부분
        func(name)  # 함수 실행
        print('-'*20)  # 함수 뒷부분
    return  inner

@hello_deco
def hello(name) :
    print('My name is ' + name + "!!")

hello("이순신")
# --------------------
# My name is 이순신!!
# --------------------


# 구구단 장식하기
'''
***** 2단 *****
2 * 1 =
  :
2 * 9 = 18
***************
'''

def gugu_deco(gugu) :
    def inner(dan) :
        print("***** %d단 *****" %(dan))
        gugu(dan)
        print("*" * 15)
    return inner

@gugu_deco
def gugu(dan) :
    for i in range(1,10) :
        cal = dan * i
        print("%d * %d = %d" %(dan, i, cal))


dan = int(input('단 입력 : '))
gugu(dan)
