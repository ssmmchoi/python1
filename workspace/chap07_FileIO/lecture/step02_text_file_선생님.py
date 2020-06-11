'''
텍스트 파일 입출력
형식)
   open(file, mode='r', 'w', 'a')
'''

import os # 파일 경로

try :
    # 1. 파일 읽기
    print('현재 경로 :', os.getcwd())
    # 현재 경로 : C:\ITWILL\3_Python-I\workspace
    # file open : 절대경로
    '''
    file = open(os.getcwd() + '/chap07_FileIO\\data/ftest.txt',
                mode='r')
    print(file.read()) # file 사용 
    file.close() # file close
    '''
    # file open : 상대경로 (.:현재 디렉터리, ..:상위 디렉터리
    file = open('../data/ftest.txt') # mode='r'
    #print(file.read())  # file 사용
    file.close()  # file close

    # 2. 파일 쓰기
    file2 = open('../data/ftest2.txt', mode='w')
    file2.write("my first text~~")
    file2.close()

    # 3. 파일 쓰기(내용 추가)
    file3 = open('../data/ftest2.txt', mode='a')
    file3.write("\nmy second text~~")
    file3.close()

    '''
    file.read() : 전체 문서 한 번에 읽기
    file.readline() : 전체 문서에서 한 줄 읽기  
    file.readlines() : 전체 문서를 줄 단위 읽기 
    '''

    # 4. readline()
    print('readline')
    file4 = open('../data/ftest2.txt')
    for i in range(2) :
        row = file4.readline()
        print('row :' + str(i+1), row.strip())
    file4.close()

    # 5. readlines() : 전체 문장을 줄단위 읽기
    file5 = open('../data/ftest2.txt')
    rows = file5.readlines() # list 반환
    print('rows')
    print(rows) # ['my first text~~\n', 'my second text~~']

    for row in rows : # 'my first text~~\n'
        for sent in row.split('\n') : # 'my first text~~' ''
            if sent :
                print(sent)

    # string.strip() : 문장 끝 불용어(공백, \n\t 기타) 제거
    print('strip 함수')
    for row in rows :
        print(row.strip())

    str_text = "agsgs234\n \t\r"
    print('str_text :', str_text.strip()) # str_text : agsgs234
    file5.close()

    # 6. with
    with open("../data/ftext3.txt", mode='w', encoding="utf-8") as file6 :
        file6.write("파이썬 파일 작성 연습")
        file6.write("\n파이썬 파일 작성 연습2")

    with open("../data/ftext3.txt", mode='r', encoding="utf-8") as file7 :
        print(file7.read())

except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    print('~~종료~~')


