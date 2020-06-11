'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd
import os
print(os.getcwd())

# 1. file read
emp = pd.read_csv('./chap07_FileIO/data/emp.csv', encoding='utf-8')
print(emp.info())
'''
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
'''

empNo = emp['No']
eName = emp['Name']
ePay = emp.Pay
print(ePay)
print('관측치 :', len(ePay))  # 관측치 : 5
emean = ePay.mean()
print('전체 평균 :',emean)  # 전체 평균 : 370.0

max_p = max(ePay)
print(max_p)
print(eName[ePay==max_p])





print('관측치 :', len(ePay))
emean = ePay.mean()
print('전체 평균 급여 :', emean)
print('='*35)
min_p = min(ePay)
max_p = max(ePay)
min_name = eName[ePay == min_p]  #[0]
max_name = eName[ePay == max_p]
print('최저 급여 : {}, 이름 : {}'.format(min_p, min_name.values[0]))
print('최고 급여 : {}, 이름 : {}'.format(max_p, max_name.values[0]))
print('='*35)
'''
관측치 : 5
전체 평균 급여 : 370.0
===================================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
===================================
'''


'''
min_p = min(ePay)
max_p = max(ePay)

def outer_deco(sol_exam03) :
    print('관측치 :', len(ePay))
    emean = ePay.mean()
    print('전체 평균 급여 :', emean)
    def inner(emp) :
        print('=' * 35)
        inner(emp)
        print('=' * 35)
    return inner

@outer_deco
def sol_exam03(emp):
    for e in emp :
        if e[2] == min_p :
            print('최고 급여 : {}, 이름 : {}'.format(e[2], e[1]))
        elif e[2] == max_p :
            print('최저 급여 : {}, 이름 : {}'.format(e[2], e[1]))
        else :
            pass

print(sol_exam03(emp))
'''




help(enumerate)
print('관측치 :', len(ePay))
emean = ePay.mean()
print('전체 평균 급여 :', emean)
min_p = min(ePay)
max_p = max(ePay)

print('='*30)
for i, p in enumerate(ePay) :   # index, pay
    if p == min_p :
        print(f'최저 급여 : {p}, 이름 : {eName[i]}')
    if p == max_p :
        print(f'최고 급여 : {p}, 이름 : {eName[i]}')
print('='*30)