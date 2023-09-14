# week03_06_input.py / printf("", ..) < f 는  포맷의 f임 / scanf("%d %f") < d는 정수형으로, f는 실수형으로 

age = input("나이: ")
age = int(age)
print(age + 1) # 이렇게 짜는 것도 괜찮음. 한 눈에 들어와서. 

# age = int(input("나이: "))
# print(age + "1") # age는 정수, 1은 문자라서 에러남.
# print(int(age) + 1)
# print(age + 1)

# age = input("나이: ")
# print(age + "1") # 위는 101 나옴.
# print(int(age) + 1) # 이렇게 하면 에러가 안남. int() < 생성자(함수) age가 가리키는 문자열로 새로운 정수형 생성.
# print는 어떤 타입이든 문자열로 바꿔서 화면에 출력해줌.

# age = input("나이: ")
# print(age + 1) < age가 문자열이라서 에러가 생김.

# age = input("나이: ")
# print(age)

# input("나이: ") < 이렇게 하면 "나이: " 가 출력되고, 입력을 받음.

# input() 입력만 받음. only 문자열로 입력 받음.
