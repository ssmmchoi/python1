'''
get vs post
 - 파라미터 전송 방식
 - get : url에 노출(소량의 데이타 전송시)
 - post : body에 포함되어 변수 전송(대량)

<작업 순서>
1. index 페이지 : 메뉴 선택(radio or select) -> get 방식
2. flask server 파라미터 받기(메뉴 번호)
3. 메뉴 번호에 따라서 각 페이지로 이동
'''

# db 연결 객체 생성 함수
def db_conn() :
    import pymysql
    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


# 전체 조회 함수
def select_func() :
    sql = f"select * from goods"
    conn, cursor = db_conn()  # db 연동 객체
    cursor.execute(sql)
    data = cursor.fetchall()

    print('=' * 30)
    print("조회 결과")
    print('=' * 30)
    for row in data:
        print(row[0], row[1], row[2], row[3], sep='\t')
    print('전체 레코드 수 :', len(data))
    print('=' * 30)

    cursor.close(); conn.close()
    return data


from flask import Flask, render_template, request  # app 생성, html 템플릿 호출

app = Flask(__name__)  # object -> app object


# 함수 장식자
@app.route('/')  # 기본 url 요청 -> 함수 호출
def index() :
    return render_template("./app04/index.html")

@app.route('/select', methods=['GET', 'POST'])  # http://127.0.0.1:5000/select?menu=1&name=홍길동
def select() :
    if request.method == 'GET' :
        menu = int(request.args.get('menu'))
        #name = request.args.get('name')
        print('menu :', menu)  # menu : 1

    if menu == 1 : # 전체 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)

    if menu == 2 : # 레코드 추가
        return render_template("/app04/insert_form.html")

    if menu == 3 :  # 레코드 수정
        return render_template("/app04/update_form.html")

    # 1. delete_form(code) -> get -> flask server(파라미터) -> delete
    if menu == 4 :  # 레코드 삭제
        return render_template("/app04/delete_form.html")

@app.route("/insert", methods=['GET', 'POST'])
def insert() :
    try :
        if request.method == 'POST' :
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            # 레코드 삽입
            conn, cursor = db_conn()
            sql = f"insert into goods values({code}, '{name}', {su}, {dan}"

            cursor.execute(sql)  # 레코드 추가
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e :
        return  render_template("/app04/error.html", error_info=e)

@app.route("/update", methods=['GET', 'POST'])
def update() :
    try :
        if request.method == 'POST' :
            code = int(request.form['code'])
            #name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            # 레코드 삽입
            conn, cursor = db_conn()
            sql = f"update goods set su={su}, dan={dan} where code={code}"

            cursor.execute(sql)  # 레코드 추가
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e :
        return render_template("/app04/error.html", error_info=e)


@app.route("/delete", methods=['GET', 'POST'])
def delete() :
    try :
        if request.method == 'POST' :
            code = int(request.form['code'])
            #name = request.form['name']
            #su = int(request.form['su'])
            #dan = int(request.form['dan'])

            # 레코드 삭제
            conn, cursor = db_conn()
            sql = f"delete from goods code={code}"

            cursor.execute(sql)  # 레코드 추가
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e :
        return render_template("/app04/error.html", error_info=e)

# 프로그램 시작점
if __name__ == "__main__" :
    app.run()  # application 실행