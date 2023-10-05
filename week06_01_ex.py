# week06_01_ex.py

name = input("이름: ")
age = int(input("나이: "))

# way 3 - f-string in python, usually 보간법 
intro = f"이름:{name+'님'} 작년 나이:{age-1}" # 중괄호 안에 수식도 넣기 가능.
print(intro)
print(end="\n")

# way 2 - use 'formmt()' method of srting
intro = "이름:{0} 나이:{1}".format(name, age) # 순서는 내 임의로 지정 가능. 중복 사용 가능.
print(intro)
print(end="\n")

# way 1 - traditional
intro = "이름:%s 나이:%d" % (name,age)
print(intro)
print(end="\n")

intro = "이름:name 나이:age"
print(intro)
print(end="\n")

# 원시방법
print("name:" + name + " age:" + str(age))
print("이름:", name, " 나이:", age, sep="") # sep="" 은 데이터 사이사이 구분자. septorater? " " 공백문자열, "" 빈문자열