'''
제어문 : 조건문(if), 반복문(while, for)
python 블럭 : 콜론과 들여쓰기

형식1)
if 조건식 :
    실행문
    실행문
'''

var = 10
if var>= 10 :
    print("var =", var)
    print("var는 10보다 크거나 같다.")

print("항상 실행되는 영역")

'''
형식2)
if 조건식:
    실행문1
else :
    실행문2
'''

var = 2
if var >= 5 :
    print("var는 5보다 크거나 같다.")
else :
    print("var는 5보다 작다.")
# var는 5보다 작다.

# 키보드 점수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score=int(input("점수 입력 : "))

if score>=60 :
    print("합격")
else :
    print("불합격")
# 합격

import datetime  # module 임포트
datetime.datetime.now()  # module.class.method()  :  datetime.datetime(2020, 4, 7, 11, 8, 13, 348434)
today = datetime.datetime.now()
print(today)  # 2020-04-07 11:09:31.316521

# 요일 반환
week = today.weekday()
print(week)  # 1 : 화요일  (0~4는 평일, 5~6 주말)
if week >= 5 :
    print("오늘은 주말이다.")
else :
    print("학원 가야 한다.")

'''
if 조건식1 :
    실행문1
elif 조건식2:
    실행문2
else :
    실행문3
'''

# 문2) 키보드 score입력: A(100-90), B(89-80), C(79-70), D, F(59-...)
score = int(input("점수 입력 : "))
if score>=90 and score<=100 :
    print("A")
elif score>=80 and score <=89 :
    print("B")
elif score>=70 and score <= 79 :
    print("C")
elif score>=60 and score <= 69 :
    print("D")
else :
    print("F")


score = int(input("점수 입력 : "))
# 전역변수 : score, grade
# grade = ""
if score>=90 and score<=100 :
    grade = "A"
elif score>=80 and score <=89 :
    grade = "B"
elif score>=70 and score <= 79 :
    grade = "C"
elif score>=60 and score <= 69 :
    grade = "D"
else :
    grade = "F"

print("당신의 점수는 %d점이고, 등급은 %s이다." %(score, grade))  # 파이썬은 if문 블록에서 만들어진 변수 블록 밖에서도 사용 가능

# 블럭 if vs 라인 if
# 블럭 if
num = 9
if num >= 5 :
    result = num*2
else :
    result = num+2
print(result)  # 18

# 라인 if
# 형식) 변수 = 참 if 조건문 else 거짓

result = num*2 if num >= 5 else num + 2
print(result)  # 18





