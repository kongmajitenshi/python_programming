# week05_03_datetime.py
import datetime # 이 datetime은 '모듈'이다.

now = datetime.datetime.now() # 모듈.클래스.메소드

print(now.year) # 2023
print(now.month) # 09
print(now.day) # 30 (30일에 코드 썼음)

print(now.hour)
print(now.minute)
print(now.second)

if now.hour < 12 :
    print("오전")
else :
    print("오후")