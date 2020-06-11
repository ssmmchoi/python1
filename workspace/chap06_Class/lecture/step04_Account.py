'''
중첩함수 -> 클래스(data + function)
'''

class Account:  # outer -> class
    # outer 변수 -> 멤버변수
    balance = 0  # 잔액(balance)

    # 생성자 추가
    def __init__(self, bal):
        self.balance = bal  # 멤버변수 초기화화

   # inner -> 멤버베서드
    def getBalance(self):  # 잔액확인(getter)
        return self.balance

    def deposit(self, money):  # 입금하기(setter)
        if money < 0:
            print("금액을 확인하세요.")
        else :
            self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        # balance = balance - money
        if self.balance < money :
            print("잔액이 부족합니다.")
        else:
            self.balance -= money

acc = Account(1000)
print('잔액 :', acc.getBalance())  # getter : 잔액 : 1000
acc.deposit(20000)  # 2만원 입금
print('잔액 :', acc.getBalance())  # 잔액 : 21000
acc.withdraw(5000)
print('잔액 :', acc.getBalance())  # 잔액 : 16000
acc.withdraw(20000)  # 잔액이 부족합니다.
acc.deposit(-10000)  # 금액을 확인하세요.

'''
1. 예금주(accName), 계좌번호(accNo) 동적 멤버변수 추가하기
   -> 예금주 : 홍길동, 계좌번호 : 012-125-41520
2. getBalance() 메서드를 이용하여 잔액, 예금주, 계좌번호 조회
'''

class Account:  # outer -> class
    # outer 변수 -> 멤버변수
    balance = 0  # 잔액(balance)
    name = account = ""

    # 생성자 추가
    def __init__(self, bal, name, account):
        self.balance = bal  # 멤버변수 초기화화
        self.name = name
        self.account = account

   # inner -> 멤버베서드
    def getBalance(self):
        return self.balance

    def deposit(self, money):  # money는 지역변수
        if money < 0:
            print("금액을 확인하세요.")
        else :
            self.balance += money

    def withdraw(self, money):  # 출금하기
        # balance = balance - money
        if self.balance < money :
            print("잔액이 부족합니다.")
        else:
            self.balance -= money


acc2 = Account(1000, '홍길동', '012-125-41520')
print('잔액 :', acc2.getBalance(), '\n',
      '예금주 :', acc2.name, '\n',
      '계좌번호 :', acc2.account, sep='')

# 잔액 :1000
# 예금주 :홍길동
# 계좌번호 :012-125-41520