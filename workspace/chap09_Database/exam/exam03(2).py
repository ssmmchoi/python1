'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
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

    while True :
        print('    [레코드 처리 메뉴 ]')
        print('[1. 레코드 조회]')
        print('[2. 레코드 추가]')
        print('[3. 레코드 수정]')
        print('[4. 레코드 삭제]')
        print('[5. 프로그램 종료]')
        menu = int(input("    메뉴번호 입력 : "))

        if menu == 1 :

            sql = f"select * from goods"
            cursor.execute(sql)
            result = cursor.fetchall()

            print('=' * 30)
            print("1. 레코드 조회 결과")
            print('='*30)
            for row in result :
                print(row[0], row[1], row[2], row[3], sep='\t')
            print('=' * 30)

        elif menu == 2 :
            code = int(input("code insert : "))
            name = input("name insert : ")
            su = int(input("su insert : "))
            dan = int(input("dan insert : "))
            sql = f"insert into goods values({code},'{name}',{su},{dan})"
            cursor.execute(sql)
            conn.commit()

            print('=' * 30)
            print("2. 레코드 추가 결과 조회")
            print('=' * 30)
            sql = f"select * from goods"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row[0], row[1], row[2], row[3], sep='\t')
            print('=' * 30)

        elif menu == 3 :
            code = int(input("select update code : "))
            name = input("name update : ")
            su = int(input("su update : "))
            dan = int(input("dan update : "))
            sql = f"update goods set name = '{name}', su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()

            print('=' * 30)
            print("2. 레코드 수정 결과 조회")
            print('=' * 30)
            sql = f"select * from goods"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row[0], row[1], row[2], row[3], sep='\t')
            print('=' * 30)

        elif menu == 4 :
            code = int(input("select code will be deleted : "))
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()

            print('=' * 30)
            print("2. 레코드 삭제 결과 조회")
            print('=' * 30)
            sql = f"select * from goods"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row[0], row[1], row[2], row[3], sep='\t')
            print('=' * 30)

        elif menu == 5 :
            break

        else :
            print("메뉴 번호를 잘못 입력하였습니다.")

except Exception as e :
    print('db연동 오류 :', e)
    conn.rollback()

finally :
    cursor.close(); conn.close