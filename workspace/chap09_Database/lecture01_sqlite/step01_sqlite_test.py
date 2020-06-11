'''
sqlite3
 - 내장형 DBMS : 기기 내부에서만 사용
 - 외부 접근 허용 안됨
'''

import sqlite3

print(sqlite3.version_info)  # (2, 6, 0)  : 나오면 제대로 실행된다는 뜻.
print(sqlite3.sqlite_version_info)  # (3, 31, 1)

try :
    # 1. database 생성 & db 연동 객체
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")  # sqlite.db 생성
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. table 생성
    sql = """create table if not exists test_tab(
    name text(10),
    phone text(15),
    addr text(50) )"""
    cursor.execute(sql)  # table 생성

    # 3. 테이블에 레코드 추가 # 쌍따옴표!!
    '''
    cursor.execute("insert into test_tab values('홍길동', '010-111-1111', '서울시')")
    cursor.execute("insert into test_tab values('이순신', '010-111-1111', '해남시')")
    cursor.execute("insert into test_tab values('유관순', '010-111-1111', '충남시')")
    conn.commit()  # db 반영, table 생성단계는 auto commit
    '''

    # 4. 레코드 조회 : commit의 대상이 아님. commit은 데이타베이스의 구조를 변화시킬 때에만.
    cursor.execute("select * from test_tab")
    dataset = cursor.fetchall()  # 객체에 저장된 레코드를 -> fetchall 사용하여 레코드 가져오기
    for row in dataset :
        print(row)

    print('='*35)
    print('이름\t\t전화번호\t\t주소')
    print('=' * 35)
    for row in dataset :
        print(row[0] + '\t' + row[1] + '\t' + row[2])
    print('=' * 35)

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행을 취소
finally :
    cursor.close()
    conn.close()

# ('홍길동', '010-111-1111', '서울시')
# ('이순신', '010-111-1111', '해남시')
# ('유관순', '010-111-1111', '충남시')
# ===================================
# 이름		전화번호		주소
# ===================================
# 홍길동	010-111-1111	서울시
# 이순신	010-111-1111	해남시
# 유관순	010-111-1111	충남시
# ===================================

