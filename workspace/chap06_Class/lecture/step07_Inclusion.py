'''
1. private 변수 = 클래스 내의 은닉변수
   object.member : 객체를 통해 -> 은닉변수 접근할 수 없음
   getter()/setter() -> 은닉변수 접근 가능
2. class 포함관계(inclusion)
  - 특정 객체가 다른 객체를 포함하는 클래스 설계 기법
  - 두 객체 간의 통신 지원
  - ex) class A(a) -> class B(b)
'''

# 1. private 변수
class Login :  # uid, pwd -> db['hong', '1234']저장
    # 생성자
    def __init__(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd
        # self.uid = uid  #  : 멤버변수. 객체를통해 집근 가능
        # self.__private

    # getter() : 획득자(return)
    def getIdPwd(self):
        return self.__dbId, self.__dbPwd  # 변수는 없고 return만 존재
    # setter() : 지정자(인수)

    def setIdPwd(self, uid, pwd) :  # 사용자가 설정하는 대로 초기화
       self.__dbId = uid
       self.__dbPwd = pwd

login = Login('hong', 1234)

#object.member
#print(login.__dbId)  # AttributeError

# object.getter() 은닉변수 외부에서 획득
uid, pwd = login.getIdPwd()
print(uid, pwd, sep=', ')

# object.setter()
login.setIdPwd('lee', 2345)
uid, pwd = login.getIdPwd()
print(uid, pwd, sep=', ')
?????????????????????????????????????????????????????????????????????????????????????????

# Server <-> Login
class Server :
    # 기본 생성자

    # 맴버 메서드
    def send(selfself, obj):  # object 인수로 받음
        self.obj = obj  # 멤버변수 생성

    # 인증 메서드
    def cert(self, uid, upwd):  # 사용자(id/pwd)
        dbId, dbPwd = self.obj.getIdPwd()  # getter 호출
        if dbId == uid and dbPwd == upwd
            print("로그인 성공~~~")
        else :
            print('로그인 실패~~~')

server = Server()
server.send(login)  # object 넘김
server.cert('hong', '1234')  # 로그인실패~~
server.cert('lee', '2345')
