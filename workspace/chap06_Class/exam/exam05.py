'''
 <급여 계산 문제>
문) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 구현하시오.
    <조건> pay_pro 함수 재정의     
'''

# 부모클래스 
class Employee :
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    
    # 원형 함수 : 급여 계산 함수     
    def pay_pro(self):
        pass

# 자식클래스 - 정규직 
class Permanent(Employee):
    # name = None
    # pay = 0
    gi = bonus = 0

    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, gi, bonus):
        self.gi = gi
        self.bonus = bonus
        self.pay = gi + bonus

    def display(self):
        print("="*30)
        print("고용 형태 : 정규직\n이름 : {}\n급여 : {}".format(self.name, self.pay))
        print("=" * 30)

name = input("이름을 입력하세요 :")
gi = int(input("기본 급여를 입력하세요 :"))
bonus = int(input("보너스를 입력하세요 :"))
permanent = Permanent(name)
permanent. pay_pro(gi, bonus)
permanent.display()


   
# 자식클래스 - 임시직 
class Temporary(Employee):
    # name = None
    # pay = 0
    time = tpay = 0
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, time, tpay):
        self.time = time
        self.tpay = tpay
        self.pay = time * tpay

    def display(self):
        print("="*30)
        print("고용 형태 : 임시직\n이름 : {}\n급여 : {}".format(self.name, self.pay))
        print("="*30)

name = input("이름을 입력하세요 :")
time = int(input("작업 시간을 입력하세요 :"))
tpay = int(input("시급을 입력하세요 :"))
temporary =Temporary(name)
temporary. pay_pro(time, tpay)
temporary.display()
    
    
  #################################################### 원래 함수에서 self.time=time과같이 time변수 적역변수로 안만들어줘도도미
# 자식클래스 - 정규직
class Permanent(Employee):
    # name = None
    # pay = 0

    def __init__(self, name):
        super().__init__(name)

    # 함수 재정의 : 인수+내용 추가
    def pay_pro(self, gi, bonus):
        self.pay = gi + bonus

    def display(self):
        print("="*30)
        print("고용 형태 : 정규직\n이름 : {}\n급여 : {}".format(self.name, self.pay))
        print("=" * 30)

name = input("이름을 입력하세요 :")
gi = int(input("기본 급여를 입력하세요 :"))
bonus = int(input("보너스를 입력하세요 :"))
permanent = Permanent(name)
permanent. pay_pro(gi, bonus)
permanent.display()

