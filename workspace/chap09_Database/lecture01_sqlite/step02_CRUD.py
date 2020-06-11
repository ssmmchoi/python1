'''
CRUD
 - Create(create, insert into), Read(select), Update(update set, insert into), Delete(delete)
'''

import sqlite3

try :
    # 1. 기존에 만들어진 db : db 연동 객체
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")  # sqlite.db 생성
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""  # integer 정수, real 실수, default 0 입력하지 않으면 기본값 0
    cursor.execute(sql)

    # 3. 레코드 추가
    '''cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()'''

    # 4. 조회
    cursor.execute("select * from goods where su >= 2")  # where su >= 2 : 세 번째
    dataset = cursor.fetchall()
    for row in dataset :
        #print(row[0], row[1], row[2], row[3]) # : 첫 번째
        print("%d   %s  %d  %d" %(row))  # : 두 번째

    print('전체 레코드 수 :', len(dataset))

    # 키보드 입력 -> 검색
    name = input("검색할 상품명을 입력하시오 :")
    cursor.execute(f"select * from goods where name like '%{name}%'")
    dataset = cursor.fetchall()
    if dataset :  # if True, 즉 레코드가 존재한다면
        for row in dataset :
            print("%d   %s  %d  %d" %(row))  # 네 번째
            print('검색된 레코드 수 :', len(dataset))
    else :
        print('검색된 상품 없음')

except Exception as e:
    print('db 연동 오류 :',e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

# 첫 번째
# 1 냉장고 2 850000.0
# 2 세탁기 3 550000.0
# 3 전자레인지 0 0.0
# 4 HDTV 0 1500000.0
# 전체 레코드 수 : 4

# 두 번째
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 4   HDTV  0  1500000
# 전체 레코드 수 : 4

# 세 번째
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 전체 레코드 수 : 2

# 네 번째
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 전체 레코드 수 : 2
# 검색할 상품명을 입력하시오 :>? 가스
# 검색된 상품 없음

# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 전체 레코드 수 : 2
# 검색할 상품명을 입력하시오 :>? 냉
# 1   냉장고  2  850000
#검색된 레코드 수 : 1


try :
    # 1. 기존에 만들어진 db : db 연동 객체
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")  # sqlite.db 생성
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""  # integer 정수, real 실수, default 0 입력하지 않으면 기본값 0
    cursor.execute(sql)

    # 3. 레코드 추가
    '''
    cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()'''

    # 4. 조회
    cursor.execute("select * from goods")
    dataset = cursor.fetchall()
    print(dataset)

except Exception as e:
    print('db 연동 오류 :',e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

# dataset을 for문으로 쪼개지 않은은경우 :# [(1, '냉장고', 2, 850000.0), (2, '세탁기', 3, 550000.0), (3, '전자레인지', 0, 0.0), (4, 'HDTV', 0, 1500000.0)]



## Update 실습

try :
    # 1. 기존에 만들어진 db : db 연동 객체
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")  # sqlite.db 생성
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""  # integer 정수, real 실수, default 0 입력하지 않으면 기본값 0
    cursor.execute(sql)

    # 3. 레코드 추가
    '''cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()'''
    '''
    # 7. 더 추가
    code = int(input("추가할 코드 입력 :"))
    name = input('상품명 입력 :')
    su = int(input("수량 입력 :"))
    dan = int(input('단가 입력 :'))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()
    '''


    # 5. 레코드 수정
    '''
    sql = "update goods set name ='테스트' where code=4"
    cursor.execute(sql)
    conn.commit()
    '''

    code = int(input("수정 코드 입력 :"))
    su = int(input("수정 수량 입력 :"))
    dan = int(input("수정 단가 입력 :"))
    sql = f"update goods set su = {su}, dan = {dan} where code={code}"
    cursor.execute(sql)
    conn.commit()


    '''
    # 6. 레코드 삭제
    code = int(input("삭제할 코드 입력 :"))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    if dataset :
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()
    else :
        print('해당 코드 없음')
    '''

    # 4. 조회
    cursor.execute("select * from goods")  # where su >= 2 : 세 번째
    dataset = cursor.fetchall()
    for row in dataset :
        #print(row[0], row[1], row[2], row[3]) # : 첫 번째
        print("%d   %s  %d  %d" %(row))  # : 두 번째

    print('전체 레코드 수 :', len(dataset))


except Exception as e:
    print('db 연동 오류 :',e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 4   테스트  0  1500000
# 전체 레코드 수 : 4

# 수정 코드 입력 :>? 1
# 수정 수량 입력 :>? 5
# 수정 단가 입력 :>? 900000
# 1   냉장고  5  900000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 4   HDTV  3  1500000
# 전체 레코드 수 : 4


# 삭제할 코드 입력 :>? 5
# 해당 코드 없음
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 4   테스트  0  1500000
# 전체 레코드 수 : 4

# 삭제할 코드 입력 :>? 4
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 전체 레코드 수 : 3

# 추가할 코드 입력 :>? 4
# 상품명 입력 :>? HDTV
# 수량 입력 :>? 3
# 단가 입력 :>? 1500000
# 1   냉장고  2  850000
# 2   세탁기  3  550000
# 3   전자레인지  0  0
# 4   HDTV  3  1500000
# 전체 레코드 수 : 4


