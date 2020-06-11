'''
table 전체 조회 -> 생성 및 조회
1. 없는 경우 : table 생성
2. 있는 경우 : table 조회
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
    #db연동 객체
    conn = pymysql.connect(**config)
    #cursor 객체 : sqp문 실행
    cursor = conn.cursor()

    # 1. 전체 테이블 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()

    # table 유무 검색
    sw = False  # 스위칭 기법에 사용
    if tables :  # 검색되는 테이블이 있는 경우
        for t in tables :
            #print(t)  # ('emp_table',)... 튜플
            #print(t[0])  # emp_table
            if t[0] == 'emp' :
                sw = True

    if sw == False :  # table 생성 -> 레코드 삽입
        #print('emp 테이블 없음')
        sql = f"""create table emp(
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int,
        bonus int default 0,
        job varchar(20) not null,
        dno int
        )"""  # auto_increment 최초로 들어간 사번 이후 레코드를 추가할 때마다 자동으로 1씩 사번이 증가
        cursor.execute(sql)  # table 생성
        sql2 = "alter table emp auto_increment = 1001"
        cursor.execute(sql2)

        sql3 = """insert into emp(ename, hiredate, sal, bonus, job, dno)
        values('홍길동', '2010-10-20', 300, 35, '관리자', 10)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
                values('강호동', '2015-09-20', 250, '사원', 20)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
                values('유관순', '2020-10-20', 220, '사원', 10)"""
        cursor.execute(sql3)
        conn.commit()  # 레코드 3개 최종 추가
        print('emp 테이블 작성 완료~~~')


    else :  # 레코드 조회
        #print('emp 테이블 있음')
        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()

        for row in data :
            print(row)  # 튜플타입  :  (1001, '홍길동', datetime.date(2010, 10, 20), 300, 35, '관리자', 10) ...

        print('전체 레코드 수 :', len(data))

        # 문1) 사원 조회 : 키보다(이름) -> 사번, 이름 부서 칼럼 출력 or 'no such 사원'
        name = input("검색할 사원 이름 입력 :")
        sql = f"select eno, ename, dno from emp where ename like '%{name}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data :
            for row in data :
                print(row)
        else :
            print("해당 이름의 사원이 존재하지 않습니다.")

        '''
        # 문2) 사원 수정 : 키보드(사번, 급여, 보너스) -> (급여, 보너스) 수정
        eno = int(input("정보를 수정할 사원의 사번 입력 :"))
        sql = f"select eno, ename, sal, bonus from emp where eno={eno}"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data :
            sal = int(input("업데이트 후 급여 :"))
            bonus = int(input("업데이트 후 보너스 :"))
            sql = f"update emp set sal={sal}, bonus={bonus} where eno={eno}"
            cursor.execute(sql)
            conn.commit()
        
            sql2 = f"select eno, ename, sal, bonus from emp"
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            print(data2)  # 어차피 1명이니까 for문 사용 X
        else :
            print('해당 사번의 사원이 존재하지 않습니다.')
        '''

        '''
        # 문3) 레코드 삭제 : 키보드(사번) -> 검색(유무) -> 레코드 삭제 or '없음'
        eno = int(input("삭제할 사원의 사번 입력 :"))
        sql = f"select * from emp where eno={eno}"
        cursor.execute(sql)
        data = cursor.fetchall()

        if data :
            sql2 = f"delete from emp where eno={eno}"
            cursor.execute(sql2)
            conn.commit()
            print(str(eno) + " 레코드 삭제함")
            print('-'*30)

            sql3 = "select * from emp"
            cursor.execute(sql3)
            data2 = cursor.fetchall()
            for d in data2 :
                print(d)
        else :
            print('해당 사원 없음')
        '''

except Exception as e :
    print('db연동 오류 :', e)
    conn.rollback()

finally :
    cursor.close(); conn.close()