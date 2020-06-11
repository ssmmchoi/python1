'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

try :
    file = open("../data/zipcode.txt", mode='r', encoding='utf-8')
    lines = file.readline() # 첫줄 읽기 
    dongs = [] # 서울시 동 저장 list

    cnt=0
    while lines :
        cnt += 1
        addr = lines.split('\t')
        if addr[1] == '서울' :
            dong = addr[3].split()  # 공백으로 split
            dongs.append(dong[0])

        lines = file.readline()

    dongs = (set(dongs))  # set으로 중복제거 >> list로 변환

    print('주소 개수 :', cnt)
    print('서울시 전체 동 개수 =', len(dongs))

    print('-'*50)
    print(dongs)
    print('-'*50)
    # 내용채우기  
    file.close()

except Exception as e :
    print('예외발생 :', e)
    
finally:
    print('종료!!!!!!!!')