# week03_04_id.py
# id() 변수가 알고 있는 값의 위치 찾기

a = 1
print(a, id(a))

b = 1
print(b, id(b)) # 1을 만들고 a가 가리킴, 후에 1을 새로 만들지 않고 b가 기존의 1을 가리킴.

a = 1.1
print(a, id(a)) # 1.1을 만들고 a가 가리킴. 그래서 주소가 변함.

a = "인하"
print(a, id(a))
