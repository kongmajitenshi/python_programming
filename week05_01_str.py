# week05_01_str.py

data1 = 41.56789
data2 = 50.0
print(data1, data2)
print(f"{data1:.2f}") # 소수점 2자리까지
print(f"{data2:g}") # 정수로


name = input("name : ")
age = int(input("age : "))

# way3: f-string p.146 
data = f"{name}의 나이는 {age}살 입니다."
print(data)

# way2: format() 메소드 이용
data = "{0}의 나이는 {1}살 입니다.{0}은 학생입니다.".format(name,age)
print(data)

data = "{1}의 나이는 {0}살 입니다.".format(name,age)
print(data)

data = "{0}의 나이는 {1}살 입니다.".format(name,age)
print(data)

data = "{}의 나이는 {}살 입니다.".format(name,age)
print(data)

# way1 : 전통적인 파이썬 동적 문자열 생성
data = "%s의 나이는 %d살 입니다." % (name, age)
print(data)

# + 연산자 이용
# data = "name :" + name + "age :" +  str(age) # age만 정수형이라 오류 나서 str붙여줌
# print(data)

# 그냥 print()으로 나열
# print("name : ", name, "age : ", age)