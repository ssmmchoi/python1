'''
csv, escel file read/write
 - 칼럼 단위로 작서된 파일 유형

cmd에서 외부 라이브러리 설치
 pip install 패키지명(ex. pandas...)
'''

import pandas as pd  # as 별칭
import os
print(os.getcwd())  # C:\ITWILL\Work\3_Python-I\workspace

# 1. csv file read
spam_data = pd.read_csv('./chap07_FileIO/data/spam_data.csv', header=None, encoding='ms949')
print(spam_data)
#       0                        1
# 0   ham    우리나라    대한민국, 우리나라 만세
# 1  spam      비아그라 500GRAM 정력 최고!
# 2   ham               나는 대한민국 사람
# 3  spam  보험료 15000원에 평생 보장 마감 임박
# 4   ham                   나는 홍길동
print(spam_data.info())   # similar to 'str()' in R
''' <class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):     ## 칼럼명(0,1)
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5 non-null      object
 1   1       5 non-null      object
dtypes: object(2) '''

# 2. x, y 변수 선택
target = spam_data[0]  # DF[칼럼명]
'''
0     ham
1    spam
2     ham
3    spam
4     ham
Name: 0, dtype: object''' #벡터 형태로 나옴
texts = spam_data[1]
print(texts)
print(target[0])  # ham

# 3. target -> dummy
target = [1 if x == 'spam' else 0 for x in target]
print(target)  # [0, 1, 0, 1, 0]

# 4. text 전처리(5장 step02)

def clean_text(texts) :
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)
    # 5. 영문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4)
    # 5. 공백 제거
    texts_re6 = ' '.join(texts_re5.split())

    return texts_re6

clean_texts = [clean_text(text) for text in texts]
print('텍스트 전처리 후')
print(clean_texts)
# 텍스트 전처리 후
# ['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']

######################################################################################################################
### bmi.csv
######################################################################################################################
bmi = pd.read_csv('./chap07_FileIO/data/bmi.csv', encoding='utf-8')
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 
 1   weight  20000 non-null  int64 
 2   label   20000 non-null  object  >>> string 같은 것
dtypes: int64(2), object(1)
memory usage: 468.9+ KB
None
'''
print(bmi.head())  # 5개
print(bmi.tail())

# 칼럼을 가져오는 두 가지 방식 : DF['칼럼명'], DF.칼럼명
height = bmi['height']
print(height)
weight = bmi['weight']
label = bmi.label
print(label)

print(len(height), len(weight), len(label))  # 20000 20000 20000

print('키 평균 :', height.mean())  # 키 평균 : 164.9379
print('몸무게 평균 :', weight.mean())  # 몸무게 평균 : 62.40995

# max()/min() : builtin
max_h = max(height)  # 190
max_w = max(weight)  # 85
min_h = min(height)
min_w = min(weight)

print('정규화')
height_nor = height / max_h
weight_nor = weight / max_w

print(height_nor.mean())  # 0.8680942105263159
print(weight_nor.mean())  # 0.734234705882353


# 범주형 변수 : label
label_cnt = label.value_counts()  # 범주 빈도수
print(label_cnt)
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''






# 2. excel file read
'''
pip install xlrd >> to venv
별도 import 과정은 필요하지 않음
'''
excel = pd.ExcelFile('./chap07_FileIO/data/sam_kospi.xlsx')
print(excel)  # <pandas.io.excel._base.ExcelFile object at 0x000002AA5758B948> : object info

kospi = excel.parse('sam_kospi')   # 파싱 : 엑셀을 처리할 수 있도록.
print(kospi)  # 내용
print(kospi.info())  # 정보
# RangeIndex: 247 entries, 0 to 246
# Data columns (total 6 columns):




# 3. csv file save
kospi['Diff'] = kospi.High - kospi.Low # 파생변수 생성. High-Low
print(kospi.info())
# RangeIndex: 247 entries, 0 to 246
# Data columns (total 7 columns):

# CSV file 저장
kospi.to_csv('./chap07_FileIO/data/kospi_df.csv', encoding='utf-8', index=None)
kospi_df = pd.read_csv('./chap07_FileIO/data/kospi_df.csv', encoding='utf-8')
print(kospi_df.head())
'''
         Date     Open     High      Low    Close  Volume   Diff >> 추가된 컬럼!
0  2015-10-30  1345000  1390000  1341000  1372000  498776  49000
1  2015-10-29  1330000  1392000  1324000  1325000  622336  68000
2  2015-10-28  1294000  1308000  1291000  1308000  257374  17000
3  2015-10-27  1282000  1299000  1281000  1298000  131144  18000
4  2015-10-26  1298000  1298000  1272000  1292000  151996  26000
'''