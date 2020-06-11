'''
step04, 05 문제 

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict  
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']

sposition = set(position)
lposition = list(sposition)
print("중복되지 않은 직위 :", lposition)

# 1 method
wc = {}
for word in position :
    if word in wc :
        wc[word] += 1
    else :
        wc[word] = 1
print("각 직위별 빈도수 ", wc)

#중복되지 않은 직위 : ['부장', '사장', '대리', '과장']
#각 직위별 빈도수  {'과장': 2, '부장': 1, '대리': 2, '사장': 1}




# 2 method   ?>???????????????????????????????????????????????????????
print('중복되지 않은 직위 :', list(set(position)))
wc2={}
for word in position:
    wc2[word] = wc2.get(word, 0) + 1
print('각 직위별 빈도수 =', wc2)
# 중복되지 않은 직위 : ['부장', '사장', '대리', '과장']
# 각 직위별 빈도수 = {'과장': 2, '부장': 1, '대리': 2, '사장': 1}