'''
우편번호 검색
[우편번호]\t[도/시]\t[구]\t[동]
135-806	서울	강남구	개포1동 경남아파트		1
[우편번호]\t[도/시]\t[구]\t[동]\t[세부주소]
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
'''

import os
print(os.getcwd())
# C:\ITWILL\Work\3_Python-I\workspace

try :
    file = open('./chap07_FileIO/data/zipcode.txt', mode='r', encoding='utf-8')
    line = file.readline()
    print(line)
    print(line.split('\t'))  # 토큰 단위로

except Exception as e :
    print('예외 발생 :', e)
finally:
    print('~~ 종료 ~~')
# ﻿135-806	서울	강남구	개포1동 경남아파트		1
#
# ['\ufeff135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']
# ~~ 종료 ~~

import os
print(os.getcwd())

try:
    dong = input('동을 입력하세요 :')
    file = open('../data/zipcode.txt', mode='r', encoding='utf-8')
    line = file.readline()

    while line :  # null == False : 문장 종료
        addr = line.split(sep='\t')

        if addr[3].startswith(dong) :
            print('[' + addr[0] + ']', addr[1], addr[2], addr[3], addr[4])

        line = file.readline() # 두번째 ~ n번째 줄 주소 읽음

    file.close()
except Exception as e:
    print('예외 발생 :', e)
finally:
    print('~~ 종료 ~~')




