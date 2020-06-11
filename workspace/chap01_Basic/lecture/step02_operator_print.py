'''
연산자(Operator)
1. 변수에 값 할당(=, 대입연산자)
2. 연산자 : 산술, 관계, 논리
3. print 형식
4. input : 키보드 입력
'''

# 1. 변수에 값 할당(=)
i = tot = 10
i += 1  # i = i + 1  # : 카운터 변수
tot += i  # tot = tot + i  # : 누적 변수
print('tot =', tot)  # tot = 21
print('i =', i)  # i = 11

v1, v2 = 100, 200
print('v1 =', v1, 'v2 =', v2)  # v1 = 100 v2 = 200

# 변수 값 교체
v1, v2 = v2, v1
print('v1 =', v1, 'v2 =', v2)  # v1 = 200 v2 = 100 서로 바뀜
'''
tmp = v1
v1 = v2
v2 = tmp
'''

# 패킹(packing) 할당
lst = [1,2,3,4,5]  # vector
len(lst)  # 5
v1, *v2 = lst
print('v1 =', v1, 'v2 =', v2)  # v1 = 1 v2 = [2, 3, 4, 5]
*v1, v2 = lst
print('v1 =', v1, 'v2 =', v2)  # v1 = [1, 2, 3, 4] v2 = 5


# 2. 연산자 : 산술, 관계, 논리
print("산술연산자")
num1 = 100  # 피연산자1
num2 = 21  # 피연산자2

add = num1 + num2
sub = num1- num2
mul = num1 * num2
div = num1 / num2
div2 = num1 // num2
div3 = num1 % num2
square = num1**2

print(add, sub, mul)  # 121 79 2100
print(div, div2, div3)  # 4.761904761904762 4 16
print(square)  # 10000

print("관계연산자")  # True or False
# 1) 동등비교
num1 == num2  # False
bool_re = num1 != num2
print(bool_re)  # True


# 2) 대소 관계 : >, >=, <, <=
bool_re = num1 >= num2
print(bool_re)  # True

bool_re = num1 <= num2
print(bool_re)  # False

print("논리 연산자")  # or, and, not
bool_re = num1 >= num2 or num1 <= 10
print(bool_re)  # True, 둘 중 하나

bool_re = num1 >= num2 and num1 <= 10
print(bool_re)  # False, 둘 다 만족해야

bool_re = not(num1 <= 10)  # (False) -> True
print(bool_re)  # True


3. print 형식
help(print)  # 함수 도움말
# package > module > function or class
# Help on built-in function print in module builtins:
# print(value, ..., sep=' ', end='\n'
# module builtins : 기본 모듈(python 설치 시 자동으로 설치되는 모듈)

'''
함수의 인수
매개변수 : 값을 넘겨 받는 변수  :  f(x,y)에서 x, y
파라미터 : 값을 갖는 변수  :  print 함수에서 sep, end ...
'''

# 1) 기본 인수
print("values =", 10+20+30)  # values = 60
print("출력1", end=',')  # 출력1,
print("출력2")
print("010", "1111", "2222", sep="-")  # 010-1111-2222

# 2) format(value, '형식')
print("원주율=", format(3.14159, "8.3f") )   # 원주율=    3.142  (총 8자리이므로 space 4)
print("금액 =", format(10000, "10d"))        # 금액 =      10000
print("금액 =", format(125000, "3,d"))       # 금액 = 125,000  (1000 단위마다 콤마 찍어주기)
print("원주율=", format(3.141592, "4.3f"))  # 원주율= 3.142
print("금액 =", format(10000, "6d"))        # 금액 =  10000
print("금액 =", format(125000125, "3,d"))   # 금액 = 125,000,125

# 3) print("양식문자") %(값))  양식문자 p.22
num1 =10; num2 =20
tot = num1 +num2
print("tot = %d" %(tot))  # tot = 30
print("%d + %d = %d" %(num1, num2, tot))  # 10 + 20 = 30
print("8진수 = %o, 16진수 = %x" %(num1,num1))  # 8진수 = 12, 16진수 = a
print("%s = %4.3f" %("PI", 3.14159))  # PI = 3.142

# 4. 외부 상수 받기
# "{}, {}". format(value1, value2)
print("name : {}, age : {}". format("홍길동", 35))  # name : 홍길동, age : 35
print("name : {1}, age : {0}". format("홍길동", 35))  # name : 35, age : 홍길동
print("name : {1}, age : {0}".format(35, '홍길동'))

# format 축약형 : sql
# select * from emp where name = '홍길동'
name = '홍길동'
age = 35
sql = "select * from emp where name = '{name}'"
sql = f"select * from emp where name = '{name}' and age = {age}"  # format 축약형
print(sql)  # select * from emp where name = '홍길동' and age = 35


# 4. input("prompt") : 키보다입력(표준입력장치)
a = input("첫번째 숫자 입력 : ")
b = input("두번째 숫자 입력 : ")
print("a + b = ", a+b)  # a + b =  1020    10과 20이 문자로 해석
a = int(input("첫번째 숫자 입력 : "))  # string -> int
10
b = int(input("두번째 숫자 입력 : "))
20
print("a + b = ", a+b)  # a + b =  30

'''
형변환 관련 함수
int(value) : value -> integer
float(value) : value -> float
str(value) : value -> string
bool(value) : value -> boolean
'''
a = float(input("첫번째 숫자 입력 : "))
b = float(input("두번째 숫자 입력 : "))
print("a + b = ", a+b)  # a + b =  24.456
print('b =', b)  # b = 12.0

# boolean -> int
print(int(False))  # 0
print(int(True))  # 1

# int -> boolean
print(bool(0))  # False
print(bool(1))  # True
print(bool(12345))  # True
print(bool(-123))  # True : 0을 제외하면 모두 True


name = input("이름이 무엇인가요? ")
print("만나서 반갑습니다. " + name + "씨!")  # 만나서 반갑습니다. 홍길동씨!
age = input("나이는요?")
print("네, 그러면 당신은 이미 " + age + "살이시군요, " + name + "씨.")  # 네, 그러면 당신은 이미 30살이시군요, 홍길동씨.


word = 'Python'
word[0:2]  # 'Py'
word[-2:]  # 'on'
