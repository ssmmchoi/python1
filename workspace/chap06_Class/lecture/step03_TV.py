'''
기본(default) 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.
 - 묵시적 생성자
 - 개체만 생성하는 역할
'''

class default_cost :
    # 생성자 생략
    # def __init__(self):
    #   pass

    def data(self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        re = self.x * self.y  # re는 지역변수
        return re

obj = default_cost()  # 기본 생성자
obj.data(10, 20)  # data 생성
obj.mul()  # 200
print('mul =', obj.mul())  # mul = 200

print('default cost =', obj)



# TV class 정의
class TV :  # class = 변수(명사, 자료) + 메소드(동작, 자료처리하는 기능)
    # 멤버변수 선언 : 자료 저장
    channel = volume = 0
    power = False  # off(False) -> on(True)
    color = None  # null

    # 기본 생성자
    def __init__(self):
        pass

    # 멤버 메서드
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power)  # 반전(T <-> F)
    def changeColor(self):
        self.color = input("색상 변경 :")

    # 멤버변수 초기화 메서드
    def data(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # TV 정보 출력 메서드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}'.format(self.power,
                                                          self.channel, self.volume, self.color))
# 객체 생성
tv1 = TV()
tv1.display()  # 전원 : False, 채널 : 0, 볼륨 : 0, 색상 : None  # 초기상태

tv1.data(5, 10, 'black')
tv1.channelUp()  # 5 -> 6
tv1.volumeUp()  # 10 -> 11
tv1.display()  # 전원 : False, 채널 : 6, 볼륨 : 11, 색상 : black  # changed!


'''
문) tv2 객체를 다음과 같이 생성하시오.
    단계1) 전원 : False, 채널 : 1, 볼륨 : 1, 색상 : 파랑색
    단계2) 전원 : True, 채널: 10, 볼륨 : 15
    단계3) tv2 객체 정보 출력
'''

tv2 = TV()
# [단계1]
tv1.data(1, 1, 'blue')
tv1.display()  # 전원 : False, 채널 : 1, 볼륨 : 1, 색상 : blue
# [단계2]
tv2.changePower()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.channelUp()
tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp()
tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp(); tv2.volumeUp()
tv2.volumeUp()
tv2.changeColor()
# [단계3]
tv2.display()  # 전원 : True, 채널 : 10, 볼륨 : 15, 색상 : blue





### 기본 생성자가 아닌 경우
class TV :  # class = 변수(명사, 자료) + 메소드(동작, 자료처리하는 기능)
    # 멤버변수 선언 : 자료 저장
    channel = volume = 0
    power = False  # off(False) -> on(True)
    color = None  # null

    # 기본 생성자
    def __init__(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # 멤버 메서드
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power)  # 반전(T <-> F)
    def changeColor(self):
        self.color = input("색상 변경 :")


    # TV 정보 출력 메서드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}'.format(self.power,
                                                          self.channel, self.volume, self.color))


tv1 = TV(5, 10, '파랑색')
tv1.display()  # 
