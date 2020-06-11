'''
CRUD
 Create, Read, Update, Delete
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
    # 1.
    conn = pymysql.connect(**config)
    # 2.
    cursor = conn.cursor()  # sql문 실행시

    '''
    # 4. Insert
    code = int(input("추가할 코드 입력 :"))
    name = input("추가할 이름 입력 :")
    su = int(input("추가할 수량 입력 :"))
    dan = int(input("추가할 단가 입력 :"))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()

    # 5. Update : code -> su, dan 수정
    code = int(input("업데이트할 코드 입력 :"))
    su = int(input("업데이트할 수량 입력 :"))
    dan = int(input("업데이트할 단가 입력 :"))
    sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # 6. Delete : code -> 유무 -> 삭제 or '코드 없음'
    code = int(input("code delete :"))
    cursor.execute(f"select * from goods where code = {code}")
    row = cursor.fetchall()
    if row :
        cursor.execute(f"delete from goods where code = {code}")
    else :
        print('no such code')


    # 3. Read(select(
    sql = "select * from goods"
    cursor.execute(sql)
    conn.commit()
    data = cursor.fetchall()

    for row in data :
        print(row[0], row[1], row[2], row[3], sep='\t')

    print('전체 레코드 수 :', len(data))

    '''
    # 상품명 조회
    name = input('조회할 상품명 입력 :')
    #sql = f"select * from goods where name = {name}"  : error
    sql2 = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql2)
    data2 = cursor.fetchall()

    if data2 :
        for row in data2 :
            print(row[0], row[1], row[2], row[3], sep='\t')
            print('조회된 레코드 수 :', len(data2))
    else :
        print("해당 상품이 존재하지 않습니다.")

    # 상품 코드 조회(primary key이므로 한개만 나올 것.
    code = int(input("조회할 상품 코드 입력 :"))
    sql3 = f"select * from goods where code={code}"
    cursor.execute(sql3)
    row = cursor.fetchone()  # 레코드 1개 반환

    if row:
        print(row[0], row[1], row[2], row[3], sep='\t')
    else :
        print("해당 상품이 존재하지 않습니다.")
    '''

except Exception as e :
    print("db연동 error :", e)
    conn.rollback()

finally :
    cursor.close(); conn.close()
