'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd
import pymysql

# 칼럼 단위 읽기 
emp = pd.read_csv("../data/emp.csv", encoding='utf-8')
print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)

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

    '''
    #  1. table 생성 : emp_table(sql 폴더)
    sql = """create or replace table emp_table(
    no int(3) primary key,
    name char(3) not null,
    pay int(3) not null)"""
    cursor.execute(sql)
    conn.commit()
    '''

    # 2. 조회
    sql2 = "select * from emp_table"
    cursor.execute(sql2)
    data = cursor.fetchall()


    if data :
        # 3. python code : 레코드 조회(사원이름)
        name = input("조회할 사원의 이름을 입력하시오 :")
        sql = f"select * from emp_table where name like '%{name}%'"
        cursor.execute(sql)
        result = cursor.fetchall()

        if result :
            for row in result :
                print(row[0], row[1], row[2], sep='\t')
        else :
            print("해당 사원이 존재하지 않습니다.")

    else :
        # 2. python code : 레코드 추가
        for i in range(len(no)) :
            sql = f"insert into emp_table values({no[i]}, '{name[i]}', {pay[i]})"
            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
        print('레코드 추가 성공~~~')
        for row in result :
            print(row[0], row[1], row[2], sep='\t')


except Exception as e:
    print("db 연동 오류 :", e)
    conn.rollback()

finally :
    cursor.close() ; conn.close()

    
    
    
    











