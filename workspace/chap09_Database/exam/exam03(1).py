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

try:
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            sql="select * from goods"
            cursor.execute(sql)
            dataset = cursor.fetchall()
            print('1. 레코드 조회')
            print('-'*35)
            for row in dataset :
                print(row[0],'\t', row[1], '\t', row[2], '\t', row[3])
            print('-'*35)

        elif menu == 2:
            print('menu2')
            code = int(input("추가할 레코드의 코드 입력 : "))
            name = input("추가할 레코드의 이름 입력 : ")
            su = int(input("추가할 레코드의 수량 입력 : "))
            dan = int(input("추가할 레코트의 단가 입력 : "))
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()
            sql2 = "select * from goods"
            cursor.execute(sql2)
            dataset = cursor.fetchall()
            print('2. 레코드 추가 및 추가 결과 조회')
            print('-' * 35)
            for row in dataset:
                print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
            print('-' * 35)

        elif menu == 3:
            code = int(input("수정할 레코드의 코드 입력 :"))
            name = input("수정할 레코드의 이름 입력 :")
            su = int(input("수정할 레코드의 수량 입력 :"))
            dan = int(input("수정할 레코트의 단가 입력 :"))
            sql = f"update table goods set name = '{name}', su={su}, dan={dan} where code={code}"
            cursor.execute(sql)
            conn.commit()
            sql2 = "select * from goods"
            cursor.execute(sql2)
            dataset = cursor.fetchall()
            print('3. 레코드 수정 및 수정 결과 조회')
            print('-' * 35)
            for row in dataset:
                print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
            print('-' * 35)

        elif menu == 4:
            code = int(input("삭제할 코드 입력 :"))
            sql = f"delete from goods where code={code}"
            cursor.execute(sql)
            conn.commit()
            sql2 = "select * from goods"
            cursor.execute(sql2)
            dataset = cursor.fetchall()
            print('4. 레코드 삭제 및 삭제 결과 조회')
            print('-' * 35)
            for row in dataset:
                print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
            print('-' * 35)

        elif menu == 5 :
            print("5. 프로그램 종로")
            break # 반복 exit

        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close() 
