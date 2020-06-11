'''
json 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일 형식 : {key:value, key2:value2}, {key:value, key2:value2}
    >>  {key:value, key2:value2}
        {key:value, key2:value2}  >> 이런 행열구조로 바뀜
 - 활용 예 : 서로 다른 플랫폼(java, python)에서 파일 공유

 - json 모듈
   1. encoding : file save : python object(list, dict) -> json file 저장할 때 : 인코딩 제공
   2. decoding : file read : json file -> python object
'''

import json

# 1. encoding : object -> 문자열
'''
python object -> json 문자열 -> file save
형식) json.dumps(object)
'''
user = {'id' : 1234, 'name' : '홍길동'}  # dict(key:value 형식)
print(type(user))  # <class 'dict'>

json_str = json.dumps(user, ensure_ascii=False)  # unicode -> ascii 인코딩 안함
print(json_str)  # {"id": 1234, "name": "홍길동"}  # 일반적인 string에서 따옴표는 쌍따옴표
print(type(json_str))  # <class 'str'>

# 2. decoding : 문자열 -> object
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''
py_obj = json.loads(json_str)
print(py_obj)  # {'id': 1234, 'name': '홍길동'}  # 하쥐만 딕셔너리에서는 홑따옴표
print(type(py_obj))  # <class 'dict'>

# 3. json file read/write

# 1) json file read : decoding
import os
print(os.getcwd())  # C:\ITWILL\Work\3_Python-I\workspace
# file = open

file = open('./chap07_FileIO/data/usagov_bitly.txt', mode='r', encoding='utf-8')
data = file.readlines()  # 전체 내용을 줄 단위 읽기(list)
file.close()
print(data)

# decoding : json 문자열 -> load라는 멤버에 의해서 -> python object
rows = [json.loads(row) for row in data]  # row {'key':value...} 가 한 줄씩 들어옴
print(len(rows))  # 3560

for row in rows[1:10] :
    print(row)  # {'a': 'GoogleMaps/RochesterNY' ...}...
    print(type(row))  # <class 'dict'> -> python object


# json object -> DataFrame
import pandas as pd
rows_df = pd.DataFrame(rows)
print(rows_df.info())
print(rows_df.head())
#                                                    a   c  ...  _heartbeat_   kw
# 0  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...  US  ...          NaN  NaN
# 1                             GoogleMaps/RochesterNY  US  ...          NaN  NaN
# 2  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...  US  ...          NaN  NaN
# 3  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...  BR  ...          NaN  NaN
print(rows_df.take())


# 2) json file write : json encoding
file = open('./chap07_FileIO/data/json_text.txt', mode='w', encoding='utf-8')
print(type(rows))  # <class 'list'>  : python object

for row in rows[:100]  : # row = {key:value,...} : dict
    json_str = json.dumps(row)  # dict -> json 문자열
    file.write(json_str)  # file save
    file.write('\n')  # 줄바꿈
print('file 저장 완료 ~~~')

# 3) json file read : json decoding
file = open('./chap07_FileIO/data/json_text.txt', mode='r', encoding='utf-8')
data = file.readlines()
print(len(data))  # 100

# json decoding
rows = [json.loads(row) for row in data]  # json 문자열 -> python object
# 딕셔너리 형태라 읽기 불편하므로 data frame으로 변환
rows_df = pd.DataFrame(rows)
print(rows_df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 18 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   a            97 non-null     object
#  1   c            78 non-null     object
#  2   nk           97 non-null     float64
#  3   tz           97 non-null     object
#  4   gr           78 non-null     object
#  5   g            97 non-null     object
#  6   h            97 non-null     object
#  7   l            97 non-null     object
#  8   al           94 non-null     object
#  9   hh           97 non-null     object
#  10  r            97 non-null     object
#  11  u            97 non-null     object
#  12  t            97 non-null     float64
#  13  hc           97 non-null     float64
#  14  cy           78 non-null     object
#  15  ll           78 non-null     object
#  16  _heartbeat_  3 non-null      float64
#  17  kw           5 non-null      object
# dtypes: float64(4), object(14)
# memory usage: 14.2+ KB
# None