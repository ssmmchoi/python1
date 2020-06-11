'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자 
        
        분산 함수(var_func)
        var = sum((x-mu)**2) / (n-1)
        
        표준편차 함수(std_func)
        std = sqrt(var)
        
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt


###  내 풀이(틀림)
x = [5, 9, 1, 7, 4, 6]

class Scattering :
    variables = length = average = 0


    def __init__(self, x, n, mu):
        self.variables = x
        self.length = n
        self.average = mu

    # 메서드
    def var_func(self):
        self.average = mean(self.variables)
        self.length = len(self.variables)

        var = sum((self.variables - self.average) ** 2) / (self.length - 1)
        return(var)

    def std_func(self):
        std = sqrt(self.var_func())


objt1 = Scattering(x, "n", "mu")
print('분산 :', objt1.var_func())





### 정답
from statistics import mean
from math import sqrt


class Scattering:
    def __init__(self, x):
        self.x = x

    def var_func(self):
        mu = mean(self.x)
        diff = [(i - mu)**2 for i in self.x]

        self.var = sum(diff) / (len(self.x) - 1)

    def std_func(self):
        self.std = sqrt(self.var)


# object 생성
x = [5, 9, 1, 7, 4, 6]
scatter = Scattering(x)
scatter.var_func()  # 분산 계산
print('분산 :', scatter.var)   # 분산 : 7.466666666666666
scatter.std_func()  # 표준편차 계산
print('표준편차 :', scatter.std)  # 표준편차 : 2.7325202042558927