'''
group by 집단변수(범주형)
'''


import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 1. 부서, 2. 직책
    gcol = int(input("1. 부서, 2. 직책 :"))

    if gcol > 2 or gcol <1 :
        print('group by 불가')

    else :
        if gcol == 1 :  # group by dno 그룹
            sql = """select dno, sum(sal), round(avg(sal), 2) from emp
            group by dno order by dno"""

        elif gcol == 2 :  # group by job
            sql = """select job, sum(sal), round(avg(sal), 2) from emp
            group by job order by job"""


        ## sql 실행 -> 검색 결과 출력하기  : python에서는 어떤 블록에서든 객체가 만들어지면 메모리에 저장되므로 전역 변수로 사용 가능
        cursor.execute(sql)
        data = cursor.fetchall()
        gtitle = "부서" if gcol ==1 else "직책"
        for row in data :
            print(row[0], '=>', '급여 총합 =', row[1], '급여 평균 =', row[2])

        print('전체 레코드 수(부서 or 직책 수) :', len(data))

except Exception as e :
    print('db연동 에러 :', e)
    conn.rollback()

finally :
    cursor.close()
    conn.close()