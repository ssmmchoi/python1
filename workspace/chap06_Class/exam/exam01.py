'''
step01_Class01 관련 문제 
 문1) Rectangle 클래스를 작성하시오.
 <처리조건>
1. 멤버변수 : 가로(width), 세로(height) 
2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화  
3. 멤버함수(area_calc) : 사각형의 넓이를 구하는 메서드 
          사각형 넓이 = 가로 * 세로 
4. 멤버함수(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
  5. 기타 나머지는 출력 예시 참조         
   
       << 출력 예시 >>       
    사각형의 넓이와 둘레를 계산합니다.
    사각형의 가로 입력 : 10
    사각형의 세로 입력 : 5
    ----------------------------------------
    사각형의 넓이 : 50
    사각형의 둘레 : 30
    ----------------------------------------
'''

class Rectangle :
    w = h = 0

    def __init__(self, width, height):
        self.w =width
        self.h = height

    def area_calc(self):
        return self.w * self.h
    def circum_calc(self):
        return (self.w + self.h) * 2

print("사각형의 넓이와 둘레를 계산합니다.")
width = int(input("사각형의 가로 입력 :"))
height = int(input("사각형의 세로 입력 :"))
rec1 = Rectangle(width, height)
print('-'*30)
print("사각형의 넓이 :", rec1.area_calc())  # 넓이 : 200
print("사각형의 둘레 :", rec1.circum_calc())  # 둘레 : 60
print('-'*30)






def outer_deco(display) :
    def inner(self):
            print('-'*30)
            display(self)
            print('-'*30)
    return inner


class Rectangle2 :
    w = h = 0

    def __init__(self, width, height):
        self.w =width
        self.h = height

    def area_calc(self):
        return self.w * self.h
    def circum_calc(self):
        return (self.w + self.h) * 2

    @outer_deco
    def display(self):
        print("사각형의 넓이 :", self.area_calc())
        print("사각형의 둘레 :", self.circum_calc())


print("사각형의 넓이와 둘레를 계산합니다.")
width = int(input("사각형의 가로 입력 :"))
height = int(input("사각형의 세로 입력 :"))
rec1 = Rectangle2(width, height)
rec1.display()