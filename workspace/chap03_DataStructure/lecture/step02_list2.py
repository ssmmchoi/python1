'''
리스트 내포

 - list에서 for문 사용

  형식1) 변수 = [실행문 for 변수 in 열거형객체]
         실행 순서 : 1. for문 > 2. 실행문 > 3. 실행결과 변수에 저장

  형식2) 변수 = [실행문 for 변수 in 열거형객체 if 조건식]
         실행순서 : 1. for문 > 2. if문 > (3.실행문) > 2. 변수에 저장
'''

# 형식1) 변수 = [실행문 for 변수 in 열거형객체]
# x 각 변량에 제곱
x = [2,4,1,3,7]
x **2   ## type error.
y = [i**2 for i in x]
print(y)  # [4, 16, 1, 9, 49]

# 원래 방법은

data=[]
for i in x :
    print(i**2)
    data.append(i**2)
print(data)    # [4, 16, 1, 9, 49]

# 형식2) 변수 = [실행문 for 변수 in 열거형객체 if 조건식]
z = [i**2 for i in x if i>2]
print(z)  # [16, 9, 49]

# 원래는
data = []
for i in x :
    if i>2 :
        print(i**2)
        data.append(i**2)
print(data)  # [16, 9, 49]

# 1~100 - > 3dml qotn
num=list(range(1,101))
print(num)

data3 = []
for i in num :
    if i % 3 == 0 :
        print(i**2)
        data3.append(i**2)

print(data3)