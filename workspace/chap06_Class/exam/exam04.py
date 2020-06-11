'''
 <급여 계산 문제>
문4) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 완성하시오.     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name

    def display(self):
        print("이름 : {}".format(self.name))





# 자식클래스 - 정규직
class Permanent(Employee):

    def __init__(self, name, pPay, bonus):
        self.name = name
        self.pay = pPay + bonus




# 자식클래스 - 임시직 
class Temporary(Employee):

    def __init__(self, name, time, tPay):
        self.name = name
        self.pay = time * tPay
 
    
empType = input("고용형태 선택(정규직<P>, 임시적<T>) : ")
if empType == 'P' or empType == 'p' :
    name = input('이름 : ')
    gi = int(input('기본급 : '))
    bonus = int(input('상여금 : '))
    p = Permanent(name, gi, bonus)
    print('='*30)
    print('고용형태 : 정규직')
    print('이름 : ', p.name)
    print('급여 : ', format(p.pay, '3,d'))    
elif empType == 'T' or empType == 't' :
    name = input('이름 : ')
    time = int(input('작업시간 : '))
    tpay = int(input('시급 : '))
    t = Temporary(name, time, tpay)
    print('='*30)
    print('고용형태 : 임시직')
    print('이름 : ', t.name)
    print('급여 : ', format(t.pay, '3,d'))
else :
    print('='*30)
    print('입력 오류')     
    





empType = input("고용형태 선택(정규직<P>,  임시적<T>) : ")
if empType =="P" or empType =='p' :
    name = input("이름 :")
    gi = int(input("기본급 :"))
    bonus = int(input("보너스 :"))
    permanent = Permanent(name, gi, bonus)
    print('='*30)
    print("고용형태 : 정규직")
    print("이름 : {}".format(permanent.name))
    print("급여 : {}원".format(permanent.pay, '3,d'))
elif empType =="T" or empType =='t' :
    name = input("이름 :")
    time = int(input("작업시간 :"))
    tpay = int(input("시급 :"))
    temporary = Temporary(name, time, tpay)
    print('=' * 30)
    print("고용형태 : 임시직")
    print("이름 : {}".format(temporary.name))
    print("급여 : {}원".format(temporary.pay, '3,d'))
else :
    print('=' * 30)
    print("입력 오류")

