#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

import os
print(os.getcwd())  # C:\ITWILL\Work\3_Python-I\workspace

file = open("./chap07_FileIO/data/ftest.txt", mode = 'r')
print(file.read())
# programming is fun
# very fun!
# have a good time
# mouse is input device
# keyboard is input device
# computer is input output system

try :
    file = open("./chap07_FileIO/data/ftest.txt", mode='r')
    row(file.readlines())
    sents = []
    for row in rows :
        sents.append(row.strip())  # \n제거

    words=[]
    for row in rows :
        for word in row.split(' ') :
            words.append(word.strip())  # 불용어 제거?

    print('문단 내용')
    print(sents)
    print('문장수 :', len(sents))
    print('단어 내용')
    print(words)
    print('단어 수 :', len(words))

except Exception as e :
    print('예외발생 :', e)
finally:
    file.close()
    print('~~종료~~')
