'''
함수의 가변인수
 - 한 개의 가인수로 여러 개의 실인수를 받는 인수
  형식) det 함수(*인수)
'''

# 1. tuple 형으로 받는 가변인수
def Func1(name, *names) :
    print(name)  # 홍길동
    print(names)  # ('이순신', '유관순') : tuple

Func1('홍길동', '이순신', '유관순')

import scatter.scatter_module  # 방법1) import 패키지.모듈 or 모듈
from scatter.scatter_module import Avg, var_std  # 방법2) from 패키지.모듈 import 함수1, 함수2, 클래스1, 클래스2

datas = [2,3,5,6,7,8.5]
avg1 = scatter.scatter_module.Avg(datas)   # 방법1)
avg2 = Avg(datas)  # 방법2)
print(avg1)
print(avg2)  # 5.25

var, std = var_std(datas)
print('var =', var)  # var = 5.975
print('std =', std)  # std = 2.444381312316063

def statis(func, *data) :
    if func == 'sum' :
        return sum(data)  # 함수 실행 종료(exit)
    elif func == 'avg' :
        return Avg(data)
    elif func == 'var':
        return var_std(data)
    elif func == 'std' :
        return var_std(data)
    else:
        return '해당 함수 없음'

print('sum =', statis('sum', 1,2,3,4,5))  # sum = 15
print('avg =', statis('avg', 1,2,3,4,5))  #avg = 3
print('var =', statis('var', 1,2,3,4,5))  # var = (2.5, 1.5811388300841898) 두개가나오므로
var, _ = statis('var', 1,2,3,4,5)
print('var =', var)  # var = 2.5
_, std = statis('std', 1,2,3,4,5)
print('std =', std)  # std = 1.5811388300841898

# 2. dict형 가변인수
def person(w, h, **other):
    print('w =', w)
    print('h =', h)
    print(other)

person(65, 175, name='홍길동', age=35)
# w = 65
# h = 175
# {'name': '홍길동', 'age': 35}

# 3. 함수를 인수로 받기
def square(x) :
    return x**2

def my_func(func, datas) :
    result = [func(d) for d in datas]
    return result

datas = [1,2,3,4,5]
my_func(square, datas)  # [1, 4, 9, 16, 25]




