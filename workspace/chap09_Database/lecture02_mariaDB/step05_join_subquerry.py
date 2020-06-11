'''
emp join dept
subquery : emp(사원정보) vs dept(부서정보)
'''

'''
table 전체 조회 -> 생성 및 조회
1. 없는 경우 : table 생성
2. 있는 경우 : table 조회
'''

import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}


try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 1. join : ANSI 표준 방식 inner join
    sal = int(input("join 급여 :"))
    sql = f"""select e.eno, e.ename, e.sal, d.dname
    from emp e inner join dept d
    on e.dno = d.dno and e.sal >= {sal}"""

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2], row[3])

    # 2. subquery : 부서번호(dept) -> 사원정보(emp) 출력
    dno = int(input("부서번호 입력 :"))
    sql = f"""select eno, ename, hiredate, dno from emp
    where dno = (select dno from dept where dno={dno})
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2], row[3])

    print('해당 부서 사원 수 :', len(data))

    # 문) subquery2 : 키보드 입력 - 사원이름(ename) -> 부서정보 출력 (이름은 unique 함)
    ename = input("조회할 사원 이름 :")
    sql = f"select dno, dname from dept where dno = (select dno from emp where ename = '{ename}')"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data :
        for row in data :
            print(row[0], row[1], sep='\t')
    else :
        print('그런 사원 없음')

except Exception as e:
    print('db연동 오류 :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()