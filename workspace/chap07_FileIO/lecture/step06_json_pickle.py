'''
json 파일 2가지 형식

1. 중괄호 : {key:value, ...}, {key:value, ...}
    >> json.loads(row)
2. 대괄호 : [{key:value, ...}, {key:value, ...}]
    >> json.load(row)
'''

import json
import pandas

# 1번 형식 : 중괄호 : {key:value, ...}, {key:value, ...}

# 2번 형식 : 대괄호 : [{key:value, ...}, {key:value, ...}]
file = open("./chap07_FileIO/data/labels.json", mode ='r', encoding='utf-8')
#print(file.read())  # [{row}, {row}, ...]

rows = json.load(file)
print(len(rows))  # 30
print(rows)
# [{'id': 76811, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug', 'name': 'Bug', 'color': 'e10c02',
# 'default': False}, {'id': 76812, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Enhancement',
# 'name': 'Enhancement', 'color': '4E9A06', 'default': False}, {'id': 127681, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Refactor',
# 'name': 'Refactor', 'color': 'FCE94F', 'default': False}, ...

for row in rows[:5] :
    print(row)
    print(type(row))

file.close()

# list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
print(rows_df.head())



# 3. pickle
'''
python object(list, dict) -> file(binary) -> python object(list, dict)
특정 형식에 국한되지 않고 모든 자료를 형태그대로 저장 가능. 광범위함
'''
import pickle
'''
save : pickle.dump(data, file)  : file에 data를 저장
load : pickle.load(file)
'''

# 1) pickle save
print('type =', type(rows))  # type = <class 'list'>

file = open("./chap07_FileIO/data/rows_data.pik", mode='wb')  # mode='wb' : binary 형식으로 write
pickle.dump(rows, file)  # list -> binary
print('pickle file saved')

# file reload

# 2) pickle load
file2 = open("./chap07_FileIO/data/rows_data.pik", mode='rb')  # 읽기 모드
rows_data = pickle.load(file2)
print(rows_data)
print(type(rows_data))  # <class 'list'>








