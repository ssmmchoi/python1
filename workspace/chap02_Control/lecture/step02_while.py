'''
반복문(while)

while 조건식 :
    실행문
    실행문
'''

# 카운터 변수, 누적변수
cnt = tot = 0  # 변수 초기화
while cnt < 5 :   # 조건식 T 이면 -> Loop(명령문의 집합)을 반복
    cnt += 1
    tot += cnt
    print(cnt, tot)

# 1~100까지 합 출력
cnt = tot = 0
while cnt < 100 :
    cnt +=1
    tot += cnt
    print(tot)
print("1~100까지 합 : %d" %(tot))

cnt=tot=0
data = [] # 빈 List(짝수 저장)
while cnt < 100 :
    cnt += 1
    tot += cnt
    if cnt % 2 == 0 :
        data.append(cnt)  # 짝수 값 추가

print("1~100까지 합 : %d" %(tot))  # 1~100까지 합 : 5050
print("짝수 값 : ", data)  # 짝수 값 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]


# 문2 ) 1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값만 append 추가
cnt = 0
data = []  # 5의 배수이면서 3의 배수가 아닌 값
num5 = []
num3 = []
while cnt < 100 :
    cnt += 1
    if cnt % 5 ==0 and cnt % 3 != 0 :
        data.append(cnt)

print(data)  # [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]


# 무한 loop -> 종료 조건(숫자 입력 : 0이면)
while True :
    num = int(input("숫자 입력 : "))
    if num == 0 :
        break # 탈출(exit) : 종료조건
    print("num =", num)

# random : 난수 생성
help(random.random)
help(random.choice)
help(random.randint)
import random  # 난수 생성 모듈
random.random()

r = random.random()  # 모듈.함수(0~1 난수)
print("r = ", r)  # r =  0.2561295155836314

r = random.randint(1,5)  # 1~5 난수 정수
print(r)

print(">>>숫자 맞추기 게임<<<")
'''
숫자 범위 1~10
myInput == computer : 성공(exit) -> 종료조건
myInput > computer : "더 작은 수를 입력하세요."
myInput < compuer : "더 큰 수를 입력하세요."
'''
computer = random.randint(1,10)
while True :
    myInput = int(input("예상 숫자 입력 : "))
    if myInput == computer :
        print("~~~성공~~~")
        break
    elif myInput > computer :
        print("더 작은 수를 입력하세요.")
    else :
        print("더 큰 수를 입력하세요.")



# 문3) 난수 0.01 미만이면 프로그램 종료, 아니면 난수 개수 출력
cnt = 0
while True :
    r = random.random()
    if r < 0.01 :
        break
    else :
        cnt += 1
print("난수 개수 : ", cnt)


'''
continue vs break
 - 반복문에서 사용되는 명령어
 - continue : 반복을 지속, 다음문장으로 skip
 - break : 반복을 멈춤
'''
i = 0
while i < 10 :
    i += 1

    if i == 3 :
        continue  # 다음문장으로 skip
    if i == 6 :
        break
    print(i, end=" ")   # 1 2 4 5

i = 0
while i < 10 :
    i += 1
    print(i, end=" ")   # 1 2 3 4 5 6 7 8 9 10














