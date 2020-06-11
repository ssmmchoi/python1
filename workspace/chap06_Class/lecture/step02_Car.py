'''
동적 멤버 변수 생성
 - 필요한 경우 트겅 함수에서 멤버변수 생성
   self : 클래스의 멤버를 호출하는 역할
   self.멤버변수
   self.멤머베서드()
'''

class Car :
    # 멤버 변수
    door = cc= 0
    name = None  # same as Null

    # 생성자 : 객체 + 초기화
    def __init__(self, door, cc, name):
        # self.멤버변수 = 매개변수
        self.door = door  # 동적 멤버변수 생성
        self.cc = cc  # 동적 멤버변수 생성
        self.name = name  # 동적 멤버변수 생성

    # 멤버 메서드 : 자료 처리
    def info(self):
        self.kind = ""  # 동적 멤버변수
        if self.cc >= 3000 :   # 동적멤버 변수. 이것도 클래스의 멤버변수이므로 클래스 밖에서 참조가능
            self.kind = "대형"
        else :
            self.kind = "소형"
        self.display()  # 얘도 맴버이므로 멤버메소드를 이렇게 호출할 수 있음.

    def display(self) :
        print('%s는 %d cc이고(%s), 문짝은 %d개 이다.' %(self.name, self.cc, self.kind, self.door))

# 객체1 생성 : 생성자() -> object생성
car1 = Car(4, 2000, '소나타')
# car1.member or car1.member()
print('자동차 명 :', car1.name)  # 자동차 명 : 소나타
car1.info()  # 소나타는 2000 cc이고(소형), 문짝은 4개 이다.

# 객체2
car2 = Car(4, 3000, '그랜저')
print('자동차 명 :', car2.name)
car2.info()




