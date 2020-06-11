'''
재귀호출(recursive call)
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
   ex) 1~n (1+2+3+4+...n)
 - 반드시 종료조건이 필요하다.
'''

# 1.카운터 : 1~n
def Counter(n):
    if n == 0 : # 종료조건
        print("프로그램 종료")
        return 0
    else :
        Counter(n-1)  # 재귀호출

Counter(0)



def Counter(n):
    if n == 0 : # 종료조건
        #print("프로그램 종료")
        return 0  # 함수 종료
    else :
        Counter(n-1)  # 재귀호출
        '''
        1. stack : [5(first), 4(5-1) ... 0(1-1)종료조건이므로 재귀를 멈추고 종료함
           stack의 특징은 가장 처음 저장한 변수를 꺼낼 때는 가장 나중에 꺼내는 변수.
        '''
        print(n, end=' ')  # 카운트

print(Counter(0))
# 프로그램 종료
# 0
Counter(5)  # 1 2 3 4 5


def Counter(n):
    if n == 0 : # 종료조건
        #print("프로그램 종료")
        return 0  # 함수 종료
    else :
        print(n, end=' ')
        Counter(n-1)  # 재귀호출

Counter(5)  # 5 4 3 2 1  아니 뭐여.....왜 거꾸로나와


# 2. 누적(1+2+3+...+n)
def Adder(n) :
    if n ==1 : # 종료조건
        return 1
    else :
        result = n + Adder(n-1)  # 재귀호출
        '''
        stack : LIFO (후입선출)
        1. stack [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1) : 종료조건이므로 stack역에 저장안됨]
        2. stack 역순으로 값 누적 :1 + [2+3+4+5] = 15
        '''
        print(result, end=' ')
        return result

print(Adder(1))  # 1
print(Adder(5))  # 15










