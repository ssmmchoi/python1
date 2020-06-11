'''
List 특징
 - 1차원 배열 구조
   형식) 변수 = [값1, 값2, ...]
 - 다양한 자료형 저장 가능(R의 벡터는 한 벡터 내에 하나의 자료형만 저장 가능했음)
 - index 사용, 순서 존재
   형식) 변수[index], index=0부터 시작
 - 값 수정(추가, 삽입, 수정, 삭제)
'''

# 1. 단일 list
lst = [1,2,3,4,5]
print(lst, type(lst), len(lst))

for i in lst :
    # print(i, end=' ')  # 1 2 3 4 5
    print(lst[i-1:])  # 변수[start:stop]
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]

for i in lst :
    print(lst[:i])  # stop-1까지
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]

'''
처음/마지막 데이터 추출
'''
x = list(range(1,101))
print(x)
print(x[:5])  # 처음 다섯개 원소
print(x[-5:])  # 마지막 다섯개 원소

'''
index 형식
변수[start:stop-1:step]
'''

print(x[:])  # 전체 데이타
print(x[1:5])  # [2, 3, 4, 5]
print(x[0:10:2])  # [1, 3, 5, 7, 9]
print(x[::10])  # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
print(x[9::10])  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(x[1::2])  # 짝수
print(x[7:1:-1])  # [8, 7, 6, 5, 4, 3]


# 2. 중첩 list : [[], []] -> 1 dimension
a = ['a', 'b', 'c']
b = [10, 20, 5, True, 'hong']  # 서로 다른 type 저장 가능
print(b)
b = [10, 20, 5, a, True, 'hong']
print(b)  # [10, 20, 5, ['a', 'b', 'c'], True, 'hong'] : 중첩 리스트
print(b[3])  # ['a', 'b', 'c']
print(b[3][2])  # c
print(b[3][1:])  # ['b', 'c']

print(type(a), type(b))  # <class 'list'> <class 'list'>
print(id(a), id(b))  # 2469897016968 2469897016584
print(id(b[3]))  # 2469897016968 : same as a's


# 3. 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 'two', 'three', 'four']
print(len(num))  # 4
'''
object.method()
'''

num.append('five')
print(num)  # ['one', 'two', 'three', 'four', 'five']

num.sort()
print(num)  # ['five', 'four', 'one', 'three', 'two']

num.remove('five')
print(num)  # ['four', 'one', 'three', 'two']

num = ['one', 'two', 'three', 'four']
num.insert(0, 'zero')
print(num)  # ['zero', 'one', 'two', 'three', 'four']

num[4] = 4
print(num)  # ['zero', 'one', 'two', 'three', 4]


# 4. list 연산

# 1) list 결합
x = [1,2,3,4,5]
y = [1.5, 2.5]
z = x + y  # new object. auch list
print(z)  # [1, 2, 3, 4, 5, 1.5, 2.5]
print(type(z))  # <class 'list'>

# 2) list 확장
x.extend(y)  # 기존 object에 추가.
print(x)  # [1, 2, 3, 4, 5, 1.5, 2.5]  - 단일 list

# 3) list 추가
x.append(y)  # 기존 object에 추가.
print(x)  # [1, 2, 3, 4, 5, 1.5, 2.5, [1.5, 2.5]]  - 중첩 list


# 5. list 곱셈(*) : 반복
lst = [1,2,3,4]
result = lst * 2
print(result)  # [1, 2, 3, 4, 1, 2, 3, 4]


# 6. list 정렬
result
result.sort()
print(result)  # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse=True)
print(result)  # [4, 4, 3, 3, 2, 2, 1, 1]

'''
scala 변수 : 한 개의 상수(값)을 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 방향)
'''

dataset = []  # 빈 list
size = int(input("vector size : "))  # scala 변수

for i in range(size) :  # range(5) : 0 ~ 4
    dataset.append(i+1)  # vector 변수

print(dataset)  # [1, 2, 3, 4, 5]


# 7. list에서 원소 찾기
'''
if 값 in list :
    참 실행문
else :
    거짓 실행문
'''

if 5 in dataset :
    print("5가 있음")
else :
    print("5가 없음")


def func(lst):
    lst[0] = 99

values = [0,1,1,2,3,5,8]
print(values)
func(values)
print(values)





