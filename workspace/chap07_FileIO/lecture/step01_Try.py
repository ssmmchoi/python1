'''
예외 : 프로그램 실행상태에서 예기치 않은 상황(오류)

try :
    예외발생 코드
except :
    예외처리 코드
finally :   # (생략 가능)
    항상 처리되는 코드
'''

print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]

for i in x :
    print(i)
    y = i**2
    print('y =', y)

print('프로그램 종료')


# 1. 간단한 예외처리

print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]

for i in x :
    try :
        print(i)
        y = i**2
        print('y =', y)
    except :
        print('예외 발생(숫자아님) :', i)


print('프로그램 종료')


# 2. 유형별 예외처리
print('유형별 예외처리')

try :
    div = 1000/2.5  # 정상
    print('div = %.3f' %div)
    #div2 = 1000/0  # 1차 : 산술적 예외
    #print('div2 = %.3f' %div2)
    #f = open('c:/text.txt')  # 2차 : 파일 열기
    num = int(input('숫자 입력 :'))  # 3차 : 기타 예외 발생
    print('num =', num)
except ZeroDivisionError as e:  # class as object
    print('예외 발생 :', e)  # 예외발생 : division by zero
except FileNotFoundError as e :  # file io 예외처리
    print('예외 발생 :', e)  # 예외 발생 : [Errno 2] No such file or directory: 'c:/text.txt'
except Exception as e :
    print('기타 예외 발생 :', e)  # 기타 예외 발생 : invalid literal for int() with base 10: 'ㅇㅇ'
finally :
    print('프로그램 종료')

print('유형별 예외처리')

# Exception 예외처리는 만능임.
print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]

for i in x :
    try :
        print(i)
        y = i**2
        print('y =', y)
    except Exception as e :
        print('예외 발생 :', e)  # 예외 발생 : unsupported operand type(s) for ** or pow(): 'str' and 'int'

print('프로그램 종료')
# 10
# y = 100
# 20
# y = 400
# 35.5
# y = 1260.25
# 15
# y = 225
# num
# 예외 발생 : unsupported operand type(s) for ** or pow(): 'str' and 'int'
# 14.5
# y = 210.25
# 프로그램 종료







