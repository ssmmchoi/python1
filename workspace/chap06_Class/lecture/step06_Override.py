'''
1. 메서드 재정의(method override)
 - 부모의 원형 메서드 -> 자식에서 원형 메서드를 다시 작성하는 문법
 - 상속관계에서만 나오는 용어
 - 인수, 내용 -> 수정 대상

2. 다형성
- 상속관계에서만 나오는 용어
- 한 가지 기능 -> 2개 이상 겨로가 생성(+ -> 덧셈, 결합)
- 부모 객체 -> (자식1, 자식2)멤버 호출
'''

# 1. 메서드 재정의(method override)

# 부모 클래스
class Super :  # 멤버 2개
    data = None  # 멤버 변수

    # 기본 생성자 : 최소한의 조건으로 객체만 생성

    # 원형 멧드 : 원형 메서드
    def superFunc(self):
        pass  # 내용 없음.

# 자식1
class Sub1(Super) :
    # data
    # def superFunc

    def superFunc(self, data):  # 수정 override
        self.data = data
        print("자식 1 :data = {}".format(data))

sub1 = Sub1()
sub1.superFunc('20200414')  # 자식 1 :data = 20200414

# 자식2
class Sub2(Super) :
    #data
    #def superFunc(self):

    def superFunc(self, data):  # 수정 -> override
        self.data = data
        print("자식2 : data = {}".format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100)  # 자식2 : data = 10000








# 2. ekgidtjd
sup = Super()
sub1 = Sub1()
sub2 = Sub2()

sup = sub
sup.superFunc(100)  # 자식 1 :data = 100
sup=sub2
sup.superFunc(100)  # 자식2 : data = 10000
