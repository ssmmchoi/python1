# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(len(texts), type(texts))  # 3 <class 'list'>

from re import sub  # gsub()
# from package.module import class or function
# from module import class or function

# 1. 소문자 변경
print('소문자 변경')
for text in texts :
    print(text.lower())

texts_re = [text.lower() for text in texts]
print("texts_re1 :", texts_re)  # texts_re1 : ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,a124&***$?']

# 2. 숫자 제거
texts_re2 = [sub('[0-9]', '', text) for text in texts_re]
print('text_re2 :', texts_re2)  # text_re2 : ['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,a&***$?']

# 3. 문장 부호 제거
punc_str = '[.,;:?!]'
texts_re3 = [sub(punc_str, '', text) for text in texts_re2]
print('text_re3 :', texts_re3)  # text_re3 : ['afabasabag', 'abtta $$a', 'uysfsfaa&***$']

# 4. 특수문자제거
spec_str = '[@$&*]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('text_re4 :', texts_re4)  # text_re4 : ['afabasabag', 'abtta a', 'uysfsfaa']

# 5. 공백 제거 'abtta a' >> ''.join('abtta','a')
texts_re5 = [''.join(text.split()) for text in texts_re4]
print('text_re5 :', texts_re5)  # text_re5 : ['afabasabag', 'abttaa', 'uysfsfaa']










