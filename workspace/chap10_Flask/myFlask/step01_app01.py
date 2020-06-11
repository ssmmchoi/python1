'''
1. templates 파일 작성
 - 사용자 요청과 서버의 응답을 작성하는 html file
2. static 파일 작성
 - 정적 파일 : image file, js, css 등
'''

from flask import Flask, render_template  # html 페이지 호출

# flask application
app = Flask(__name__)  # 생성자 -> object(app)

@ app.route('/')  # 기본 url : http://127.0.0.1:5000/
def index() :  # 호출 함수
    return render_template('./app01/index.html')  # 호출할 html 페이지

@app.route('/info')  # http://127.0.0.1:5000/info
def info() :
    return render_template('./app01/info.html')

if __name__ == "__main__" :
    app.run()