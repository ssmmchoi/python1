'''
문자열 처리
 - 문자열(string) : 문자들의 순서(index)의 집합
 - indexing / slicing 가능
 - 문자열 = 상수이면, 수정 불가
'''

# 1. 문자열 처리

# 1) 문자열 유형
lineStr = "this is one line string"  # 한 줄 문자열
print(lineStr)
multiStr = '''this
is multi line
string'''
print(multiStr)

multiStr2 = 'this\nis multi line\nstring'
print(multiStr2)

# sql문 : 부서번호
deptno = int(input('부서번호 입력 :'))
20
query = f"""select * from emp
where deptno = {deptno}
order by sel desc"""
print(query)

deptno = int(input('부서변호 입력 : '))
30
query = """select * from emp
where deptno = {}
order by sel desc""".format(deptno)
print(query)

deptno = int(input('부서번호 입력 : '))
30
query = """select * from emp
where deptno = %d
order by sel desc""" %(deptno)
print(query)

deptno = int(input('부서번호 입력 : '))
query = """select * from emp
where deptno = """, format(deptno, "2d"), "\norder by sel desc"
print(query)

# 2) 문자열 연산(+, *)
print('Python' + " program")  # Python program  결합연산자
print('python' + 37)  # type error
print('python' + '37')  # python37
print('='*30)  # ==============================

'''
object.member변수 or object.member() 함수 p.51
int.member
str.member
'''

# 3. 문자열 처리 함수
print(lineStr, type(lineStr))
print('문자열 길이 : ', len(lineStr))  # 문자열 길이 :  23
print(lineStr.upper())  # THIS IS ONE LINE STRING
print(lineStr.swapcase())
print(lineStr.count("x"))  # 0
print('t의 글자수 : ', lineStr.count("t"))  # t의 글자수 :  2

# 접두어 : 시작문자열
print(lineStr.startswith("this"))  # True
print(lineStr.startswith("that"))  # False

# slit : 토큰 생성
words = lineStr.split(' ')
print(words)  # ['this', 'is', 'one', 'line', 'string']
lineStr.split(sep=' ')  # ['this', 'is', 'one', 'line', 'string']
print('단어 개수 : ', len(words))  # 단어 개수 :  5
' '.join(words)  # 'this is one line string'
lineStr.index("i")  # 2
lineStr.rfind("i")  # 20
lineStr.replace("i", "o") # 'thos os one lone strong'
sentence = " ".join(words)
print(sentence)

# 문단 -> 문장
print(multiStr)
sentences = multiStr.split('\n')
print(sentences)  # ['this', 'is multi line', 'string']
print('문장 개수(길이?) : ', len(sentence))  # 문장 개수(길이?) :  3
multiStr2 = " ".join(sentences)
print(multiStr2)

# 4) indexing/slicing
print(lineStr[0])  # t
print(lineStr[-1])  # g

print(lineStr[0:4])  # this
print(lineStr[4])
print(lineStr[-6:])  # string

# join : "구분자".join(str)
print(sentence)

para = ','.join(sentences)
print(para)


# 2. escape 문자 처리
'''
escape 문자 : 명령어 이외 특수문자(', ", \n, \t, \b)
'''
print("\nescape 문자")
#
# escape 문자
print("\\nescape 문자")  # \nescape 문자
print(r"\nescape 문자")  # \nescape 문자

# C:\python\work\test
print("C:\python\work\test")  # C:\python\work	est \t를 텝 키로 인식
print(r"C:\python\work\test")  # C:\python\work\test
print("C:\python\work\\test")  # C:\python\work\test







