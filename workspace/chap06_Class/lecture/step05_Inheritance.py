'''
클래스 상속(Inheritance)
 - 기존 클래스(부모)를 이용하여 새로운 클래스(자식)를 생성하는 문법
 - 부모클래스 정의 -> 자식클래스 생성
 - 상속 대상 : 맴버(o) + 생성자(x) : 생산자는 상속 대상이 아님
   형식) class 자식클래스(부모클래스):  # class new_class(old_Class)
            맴버(변수+메서드)
            생성자

self vs super()
 - self.member : 현재 자신의 맴버를 호출
 - super().member : 부모클래스의 멤버를 호출

'''

# 부모클래스 : old class
class Super :  # member 3개
    # 멤버변수(데이터 저장)
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 멤버 메서드(데이터 처리)
    def display(self):
        print("이름 : {}, 나이 : {}".format(self.name, self.age))

# 정의된 부모 클래스에 object 생성
super = Super("부모", 55)
# object.member
super.display()


# 자식클래스 :
class Sub(Super) :
    # name = None
    # age = 0
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):  # 2개 -> 3개 확장
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

# object
sub = Sub("자식", 22, "남자")
# object.member
sub.display()



# 자식클래스 2 :
class Sub(Super) :
    # name = None
    # age = 0
    gender = None

    def __init__(self, name, age, gender):
        # 2차 : 부모 생성자 호출 : 부모 맴버를 초기화
        Super.__init__(self, name, age) # : ver3.7
        #super().__init__(name,age) : super라는 객체를 이미 만들어놓았기 때문에 중복되어 호출에 문제생김
        # self.name = name
        # self.age = age
        self.gender = gender
    def display(self):  # 2개 -> 3개 확장
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

# object
sub = Sub("자식", 22, "남자")
# object.member
sub.display()


# 부모클래스 super을 없애고 다시
sup = Super("부모", 55)
del super

class Sub(Super) :
    # name = None
    # age = 0
    gender = None

    def __init__(self, name, job, gender):
        # 2차 : 부모 생성자 호출 : 부모 맴버를 초기화
        super().__init__(name,job)
        # self.name = name
        # self.age = age
        self.gender = gender
    def display(self):  # 2개 -> 3개 확장
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

sub2 = Sub("유관순", 22, "독립열사")
sub2.display()  # 이름 : 유관순, 나이 : 22, 성별 : 독립열사





# 1. 부모 클래스 정의
class Parent :
    # member
    name = job = None

    #initiator
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # member method
    def display(self):
        print("name : {}, job : {}".format(self.name, self.job))

p = Parent("HongGilDong", "civil")
p.display()  # name : HongGilDong, job : civil

# 자식 클래스1
class Children1(Parent) :
    gender = None

    def __init__(self, name, job, gender):
        Parent.__init__(self, name, job)  # 부모 생성자 호출(초기화)
        self.gender = gender  # 자식의멤버 초기화

    def display(self):  # 내용 확장하기
        print("이름 : {}, 직업 : {}, 성별 : {}".format(self.name, self.job, self.gender))

c1 = Children1("이순신", "군인", "남자")
c1.display()  # 이름 : 이순신, 직업 : 군인, 성별 : 남자


'''
문제
Parent -> Children2
이름 : 유관순
직업 : 독립열사
성별 : 여자
'''

class Children2(Parent) :
    gender = None

    def __init__(self, name, job, gender):
        Parent.__init__(self, name, job)
        self.gender = gender

    def display(self):
        print("이름 : {}\n직업 : {}\n성별 : {}".format(self.name, self.job, self.gender))

c2 = Children2("유관순", "독립열사", "여자")
c2.display()