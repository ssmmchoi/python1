'''
1. pickle file load
2. 텍스트 전처리
3. word count
'''

# 1. pickle file load
file = open('./chap08_Crawling/data/new_crawling.pickle', mode='rb')
new_crawling = pickle.load(file)
print(type(new_crawling))  # <class 'list'>
print(new_crawling)

# 2. 텍스트 전처리
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
    # 5. 공백 제거
    texts_re5 = ' '.join(texts_re4.split())

    return texts_re5


clean_news = [clean_text(news) for news in new_crawling]
print(new_crawling[:5], clean_news[:5])


# 3. word count
word_count = {}  # 빈 set
for texts in clean_news :
    for word in texts.split() :
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# 2음절 이상 단어만 선택  # dict 로 나옴
word_count2 = word_count.copy()  # 객체 복제
for word in word_count.keys() :  # 키값 생략하면 키값 넘어옴
    if len(word) < 2 :
        del word_count2[word]
print(word_count2)


# 5. top10, top5 추출
'''
pip install collections-extended
'''
from collections import Counter  # 객체를 생성해주는 클래스
count = Counter(word_count2)
help(Counter)
print(count)

top5 = count.most_common(5)
print(top5)  # [('none', 19), ('코로나', 4), ('[바로잡습니다]', 4), ('지급', 3), ('수출', 3)]

# 불용어 제거
del count['none']
del count['[바로잡습니다]']

top5 = count.most_common(5)
print('top5')
print(top5)  # [('코로나', 4), ('지급', 3), ('수출', 3), ('고용', 3), ('소득', 3)]

top10 = count.most_common(10)
print(top10)  # [('코로나', 4), ('지급', 3), ('수출', 3), ('고용', 3), ('소득', 3), ('기여도는', 3), ('만원', 3), ('이사장', 3), ('트럼프', 3), ('재난지원금', 2)]


# list(dict) : [(), ()] 튜플을 데이타프레임으로
import pandas as pd
top10_df = pd.DataFrame(top10)
print(top10_df)
#        0  1
# 0    코로나  4
# 1     지급  3
# 2     수출  3
# 3     고용  3
# 4     소득  3
# 5   기여도는  3
# 6     만원  3
# 7    이사장  3
# 8    트럼프  3
# 9  재난지원금  2
top10_df = pd.DataFrame(top10, columns=['word', 'count'])
print(top10_df)
#      word  count
# 0    코로나      4
# 1     지급      3
# 2     수출      3
# 3     고용      3
# 4     소득      3
# 5   기여도는      3
# 6     만원      3
# 7    이사장      3
# 8    트럼프      3
# 9  재난지원금      2

'''
그래프로 시각화
pip install matplotlib
'''

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
'''위 세 줄은 한글이 안깨지도록 폰트를 임포트하는 과정'''

# 선 그래프 plt.plot(DataFrame['x축에 갈 칼럼'], DataFrame['y축에 갈 칼럼']
plt.plot(top10_df['word'], top10_df['count'])
plt.title('top10 word count')
plt.show()

# 막대 프래프
plt.bar(top10_df['word'], top10_df['count'])
plt.title('top10 word count - 세로 막대 차트')
plt.show()


