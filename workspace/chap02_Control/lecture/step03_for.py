'''
반복문(for)

형식)
for 변수 in 열거형객체 :
    실행문
    실행문

열거형 객체란? iterable : string, [list], tuple, set/dict
제너레이터 식 : 변수 in 열거형객체(원소 순회 -> 앞에 있는 변수에 넘김)
'''

# 1. string 열거형 객체 이용
string = "나는 홍길동 입니다."
len(string)  # 11
for s in string :
    print(s, end=':')         # 나:는: :홍:길:동: :입:니:다:.:

for s in string.split() :   # split(sep=' ') or split(''): 3회
    print(s)
# 나는
# 홍길동
# 입니다.

# 2. list 열거형 객체 이용
help(list)  # class
lst = [1,2,3,4,5]
print(lst)  # [1, 2, 3, 4, 5] : object 내용 출력(vector)
print(type(lst))  # <class 'list'>  : object 타입 출력
print(len(lst))  # 5

for i in lst :      # 제너레이터 식
    print(i, end=" ")           # 1:2:3:4:5:

lst2 = []   # empty list object
for i in lst :
    print(i)
    lst2.append(i**2)          # 원소추가(순서보장)   ### print(lst2**2)는 type error. 그래서 for문 씀
    print("lst2 : ", lst2)


lst2 = []   # empty list object
for i in lst :
    print(i, end=":")
    lst2.append(i**2)

print("\nlst2 : ", lst2)


# 1~100 원소를 갖는 list 객체 생성
lst3 = list(range(1, 101))  # stop보다 step작은 수만큼 생성, step=1은 default
print(lst3)


# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수
range(start, stop) : start ~ stop-1 정수
range(start, stop, step) : start ~ stop-1, step 만큼 증가하는 정수 
'''

num1 =range(10)  # 0~9
num2 =range(1,10)  # 1~9
num3 = range(1,10,2)  # 1,3,5,7,9
print(num1, num2, num3, sep=" : ")  # range(0, 10) : range(1, 10) : range(1, 10, 2)
                                    # 객체 정보만 나옴. 내용을 보려면
for i in num1 :
    print(i, end= ", ")    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

for i in num2 :
    print(i, end=", ")     # 1, 2, 3, 4, 5, 6, 7, 8, 9,

for i in num3 :
    print(i, end=", ")     # 1, 3, 5, 7, 9,


# 4. list + range 열거형 객체 이용
idx = range(5)  # 0~4 다섯개 인덱스 저장
print(idx)  # range(0, 5)

idx = list(range(5))  # range object -> list object
print(idx)  # [0, 1, 2, 3, 4]

for i in idx :
    print(i, end=", ")
    print(i**2)


# 문) lst1에 1~100 100개의 원소를 갖는 vector를 생성하고,
#     3의 배수만 lst2에 저장하기

lst2 = []
lst1 = list(range(1, 101))
print(len(lst1), lst1)

for i in lst1 :
    if i % 3 == 0 :
        lst2.append(i)

print(lst2)
print(len(lst2))  # 33


# index 이용 : 분류정확도
y = [1,0,2,1,0]  # 관측치(정답) : 범주형(0,1,2)
y_pred = [1,0,2,0,0]  # 예측치

size = len(y)
print(size)  # 5
print(range(size))
acc = 0

for i in range(size) :    # range(5) : 0-4
    fit = int(y[i] == y_pred[i])   # True/False -> 1/0
    acc += fit * 20  # 누적변수

print("분류정확도 = ", acc,"%")    # 분류정확도 =  80 %


# 5. 이중 for 문
# 1) 구구단
for i in range(2, 10) :
    print("<< %d단 >>" %(i))

    for j in range(1, 10) :
        print("%d * %d = %d" %(i, j, (i*j)))

    print("\n")

for i in range(2, 10) :
    print("<< {}단 >>".format(i))

    for j in range(1, 10) :
        print("%d * %d = %d" %(i, j, (i*j)))

    print("\n")

# 2) 문자열 처리
'''
for 변수 in 문단 :  # 문단 -> 문장
    for 변수 in 문장 :  # 문장 -> 단어
'''

para = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''
sents = []  # 문장
words = []  # 단어
for sent in para.split('\n') :
    sents.append(sent)  # 문장 저장
    for word in sent.split(' ') :
        words.append(word)

print(sents, words, sep='\n')
print('문장 길이 : ', len(sents))  # 문장 길이 :  3
print('단어 길이 : ', len(words))  # 단어 길이 :  9


# 제너레이터 식 : 변수 in 열거형객체
'''
for 변수 in 열거형객체 :
    -> 객체의 원소 수 만큼 반복
if 값 in 열거형객체 :
    -> 객체 원소 중에서 값이 있으면 True, 없으면 False
'''
if "홍길동" in words :
    print("해당 단어 있음")
else :
    print("해당 단어 없음")             # 해당 단어 있음


search = input("검색 단어 입력 :")
if search in words :
    print("해당 단어 있음")
else:
    print("해당 단어 없음")





