'''
step02 문제
'''

''' 
문3) 지방(fat), 탄수화물(carbohydrate), 단백질(protein)            
       칼로리의 합계를 계산하는 프로그램을 작성하시오.
    조건1> 지방, 탄수화물, 단백질의 그램을 키보드로 입력받음 
    조건2> dict에 저장된 3개 데이터 이용 총 칼로리 계산
               총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4              

   <<화면출력 결과>>
  지방의 그램을 입력하세요 : 25
  탄수화물의 그램을 입력하세요 : 520
  단백질의 그램을 입력하세요 : 45
  총칼로리 : 2,485 cal
'''
fat = int(input("지방의 그램을 입력하세요 : "))
print(fat)  # 25
carbohydrate = int(input("탄수화물의 그램을 입력하세요 : "))
print(carbohydrate)  # 520
protein = int(input("단백질의 그램을 입력하세요 : "))
print(protein)  # 45
print(fat*9 + protein*4 + carbohydrate*4)

print("총칼로리 : ", format(fat*9 + protein*4 + carbohydrate*4, "3,d"), "cal")  # 총칼로리 :  2,485 cal