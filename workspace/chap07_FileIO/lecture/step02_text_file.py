'''
텍스트 파일 입출력
형식)
    open(file, mode='r', 'w', 'a', 'r+')   default mode는 'r'
'''

import os  # 파일 경로 확인에 사용


try :
    print('현재 경로 :', os.getcwd())
    # file = open()
except :
    pass
finally :
    pass
# 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace


# 절대경로 방식으로 파일 읽기
try :
    print('현재 경로 :', os.getcwd())
    # file open : 절대경로 방식
    file = open(os.getcwd() + '/chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close
except Exception as e:
    print('예외 정보 :', e)
finally :
    pass


# 상대 경로 방식으로 파일 읽기
try :
    print('현재 경로 :', os.getcwd())
    # 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace
    # file open : 상대경로 방식 : . 앞쪽은 기본 경로로 인식 : .은 현재 디렉토리, ..는 상위 디렉토리
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close
except Exception as e:
    print('예외 정보 :', e)
finally :
    pass


# 2. 파일 쓰기(덮어쓰기)
try :
    print('현재 경로 :', os.getcwd())
    # 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace
    # file open : 상대경로 방식 : . 앞쪽은 기본 경로로 인식 : .은 현재 디렉토리, ..는 상위 디렉토리
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close

    file2 = open('./chap07_FileIO\\data/ftest2.txt', mode='w')
    file2.write('my first text~~')
    file2.close()
except Exception as e:
    print('예외 정보 :', e)
finally :
    pass


# 3. 파일 쓰기(추가)
try :
    print('현재 경로 :', os.getcwd())
    # 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace
    # file open : 상대경로 방식 : . 앞쪽은 기본 경로로 인식 : .은 현재 디렉토리, ..는 상위 디렉토리
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close

    file2 = open('./chap07_FileIO\\data/ftest2.txt', mode='w')
    file2.write('my first text~~')
    file2.close()

    file3 = open('./chap07_FileIO\\data/ftest2.txt', mode='a')
    file3.write('\nmy second text~~')
    file3.close()

except Exception as e:
    print('예외 정보 :', e)
finally :
    pass
# 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace
# my first text~~
# my second text~~


'''
file.read() : 전체 문서 한 번에 읽기
file.readline() : 전체 문서에서 한 줄로 읽기
file.readlines() : 전체 문서를 줄 단위로 읽기
'''
# 4. readLine
print('$$$')
try :
    print('현재 경로 :', os.getcwd())
    # 현재 경로 : C:\ITWILL\Work\3_Python-I\workspace
    # file open : 상대경로 방식 : . 앞쪽은 기본 경로로 인식 : .은 현재 디렉토리, ..는 상위 디렉토리
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close

    file2 = open('./chap07_FileIO\\data/ftest2.txt', mode='w')
    file2.write('my first text~~')
    file2.close()

    file3 = open('./chap07_FileIO\\data/ftest2.txt', mode='a')
    file3.write('\nmy second text~~')
    file3.close()

    file4 = open('./chap07_FileIO\\data/ftest2.txt')
    row = file4.readline()
    print('row :', row)
    file4.close()

except Exception as e:
    print('예외 정보 :', e)
finally :
    pass


# 5. readlines() : 전체 문장을 준단위 읽기
try :
    print('현재 경로 :', os.getcwd())
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close

    file2 = open('./chap07_FileIO\\data/ftest2.txt', mode='w')
    file2.write('my first text~~')
    file2.close()

    file3 = open('./chap07_FileIO\\data/ftest2.txt', mode='a')
    file3.write('\nmy second text~~')
    file3.close()

    file4 = open('./chap07_FileIO\\data/ftest2.txt')
    row = file4.readline()
    print('row :', row)
    file4.close()

    file5 = open('./chap07_FileIO\\data/ftest2.txt')
    rows = file5.readlines()
    print('rows =', rows)

    for row in rows :  # 'my first text~~\n'
        for sent in row.split('\n') :  # 'my first text~~', ''
            if sent :
                print(sent)
except Exception as e:
    print('예외 정보 :', e)
finally :
    pass


# string.strip() : 문장 끝 불용어(공백, \n,\t, 기타) 제거
try:
    print('현재 경로 :', os.getcwd())
    file = open('./chap07_FileIO\\data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file close

    file2 = open('./chap07_FileIO\\data/ftest2.txt', mode='w')
    file2.write('my first text~~')
    file2.close()

    file3 = open('./chap07_FileIO\\data/ftest2.txt', mode='a')
    file3.write('\nmy second text~~')
    file3.close()

    print('readLine')
    file4 = open('./chap07_FileIO\\data/ftest2.txt')
    for i in range(2) :
        row = file4.readline()
        print('row :' + str(i+1) , row)#.strip하면 공백 제거
    file4.close()

    file5 = open('./chap07_FileIO\\data/ftest2.txt')
    rows = file5.readlines()
    print('rows =', rows)

    for row in rows:  # 'my first text~~\n'
        for sent in row.split('\n'):  # 'my first text~~', ''
            if sent:
                print(sent)

    print('strip 함수')
    for row in rows :
        print(row.strip())  # 불용어 제거

    str_text = 'agsgs234\n \t\r'
    print('str_text :', str_text.strip())  # str_text : agsgs234

except Exception as e:
    print('예외 정보 :', e)
finally:
    pass



# 6. with
try:
    file5 = open('./chap07_FileIO\\data/ftest2.txt')
    rows = file5.readlines()
    print('rows =', rows)

    for row in rows :
        for sent in row :
            if sent :
                print(sent)

    print('strip 함수')
    for row in rows :
        print(row.strip())

    str_text = 'agsgs234\n \t\r'
    print('str_text :', str_text.strip())  # str_text : agsgs234
    file5.close()

    with open('..\\data/ftest3.txt', mode='w', encoding='utf-8') as file6 :  # 이렇게 쓸때와
        file6.write('파이썬 파일 작성 연습')
        file6.write('\n파이썬 파일 작성 연습2')

    with open('..\\data/ftest3.txt', mode='r', encoding='utf-8') as file7 :  # 읽을 때 같은 인코딩
        print(file7.read())



except Exception as e:
    print('예외 정보 :', e)
finally:
    print('~~종료~~')

