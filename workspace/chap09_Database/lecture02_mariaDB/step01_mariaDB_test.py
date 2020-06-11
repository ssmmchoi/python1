'''
MariaDB 연동 TEST
 - 외부에서 접근 가능하기 때문에 환경변수를 이용해서 db에 연결줘야함.data/db_config.txt 참조
'''

import  pymysql

print(pymysql.version_info)  # (1, 3, 12, 'final', 0)  : 버전 정보가 정상 출력되므로 라이브러리가 정상 설치 되었음을 알 수 있음.

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    # 1. db 연동 객체
    conn = pymysql.connect(**config)  # 함수에서 동적 변수를 받을 때 ** 사용

    # 2. sql 실행 객체
    cursor = conn.cursor()

    # 3. table 생성
    sql = """create or replace table goods(
        code int primary key,
        name varchar(30) not null,
        su int default 0,
        dan int default 0.0
        )"""  # 각 항목의 속성 표시 sqlite03과 다름. 원래 mysql과 동일함. 그리고 원래 work DB내에 동일 이름 table 존재했으므로 of replace 붙여줌
    cursor.execute(sql)  # table 생성

    # 3. 테이블에 레코드 추가
    cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()

    # 4. 레코드 조회
    sql = "select * from goods"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    for row in dataset :
        print(row[0], row[1], row[2], row[3])

    print('전체 레코드 수 :', len(dataset))

except Exception as e:
    print('db 연동 에러 :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

# 1 냉장고 2 850000
# 2 세탁기 3 550000
# 3 전자레인지 0 0
# 4 HDTV 0 1500000
# 전체 레코드 수 : 4



