'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
print(message)

# 문1) 첫 번째 형식
dummy = [1 if m == 'spam' else 0 for m in message]
print(dummy)  # [1, 0, 1, 0, 1]

dummy = []
dummy = [dummy.append(1) if m=='spam' else dummy.append(0) for m in message]
print(dummy)    ######### error...  # [None, None, None, None, None]



# 문2) 두 번째 형식
spam_list = [m for m in message if m == 'spam']
print(spam_list)  # ['spam', 'spam', 'spam']