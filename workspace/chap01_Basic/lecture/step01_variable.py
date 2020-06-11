'''
변수(variable)
 - 형식) 변수명 = 값 or 수식 or 변수명
 - 자료를 저장하는 메모리 이름
 - type 선언 없음(R과 동일)
'''


# 1. 변수와 자료
var1 = "Hello python"
var2 = 'Hello python'  # string type : both "", '' able
print(var1)  # Line skip
print(var2)
# 변수 자료명 확인
print(type(var1))  # <class 'str'> : string(문자 타입)
print(type(var1), type(var2))  # <class 'str'> <class 'str'>

var1 = 100
print(var1)
print(var1, type(var1))  # 100 <class 'int'>(정수형)

var3 = 150.25
print(var3, type(var3))  # 150.25 <class 'float'>(실수형)

var4 = True
print(var4, type(var4))  # True <class 'bool'> (부울리언 자료형) True & False

width = 10
height = 20
area = width*height
print(area, type(area))  # 200 <class 'int'>

# 2. 변수명 작성규칙(p.11 참조)

_num10 = 10
_NUM10 = 20
print(_num10, _NUM10)  # 10 20 대소문자 구분됨
print(id(_num10), id(_NUM10))  # 140706770287968 140706770288288 : 변수가 저장된 메모리의 소속

# 키워드 확인
import keyword  # 모듈 임포트  C:\Python37\Lib 에 존재(R에서 library로 패키지를 로드하는 과정에 해당)
keyword.kwlist  # 키워드 반환
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
# 'raise', 'return', 'try', 'while', 'with', 'yield']
py_keyword = keyword.kwlist
print("파이선 키워드 :", py_keyword)  # 위와 같음.
print("len =", len(py_keyword))  # len = 35 : 위 키워드 목록의 개수가 35개라는 뜻 - 얘네는 변수명으로 사용 X

# 낙타체
korScore = 90  # 변수 = 상수
matScore = 85
engScore = 75

tot = korScore + matScore + engScore  # 변수 = 수식
print("tot =", tot)  # tot = 250


# 3. 참조변수 : 메모리 객체(값)를 참조하는 주소 저장 변수
x = 150   # 객체의 주소가 x에 저장
y = 45.23
y2 = y  # 변수 복제
x2 = 150  # 기존 객체가 있으면, 동일 주소 반환(효율적 메모리 사용)

print(x, y, y2, x2)  # 150 45.23 45.23 150
print(id(x), id(x2), id(y), id(y2))  # 140706770292448 140706770292448 2788792504560 2788792504560




