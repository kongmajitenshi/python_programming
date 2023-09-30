# week05_06_dict.py Dictionary 딕셔너리

a = "string"
a[0] # "s"

b = [1,2,3] # 여기서의 대괄호는 리스트라는 표시.
b[0] # 1

c = { 1:"one", 2:"two"}
c[1] # "one" 군집형 계열의 요소에 접근 시에는 대괄호 사용. 리스트와는 연관 x 

infos = {
    "20230001":{"name":"kim inha", "age":21 },
    "20230002":{"name":"choi comsung", "age":22, "major":"컴정" }
}
print(infos["20230002"]["major"])



infos = { 1: ["kim inha", 21], 2: ["choi comsung", 22] }

print(infos[2][1])


a = infos[2]
b = a[0]
c = b.split(" ")
d = c[0]
print(a, b, c, d)
# p.216
info_a = {
    "name": "Kim inha",
    "age" : 21
}

info_b = {
    "name" : "Choi comjung",
    "age" : 22
    # height : 170 이라고 사용 시 변수 height 내부의 값을 key로 사용함. key는 지정하지 않는 변수 사용 불가능
}

print(info_a["name"]) # 딕셔너리에 접근 할 때도 대괄호 사용하는 이유?
print(info_b['age'])

test_dict = { # value는 중복 가능, key는 중복 불가능.
    "one": 1, # "one" 을 찾으면 value를 1으로
    "two": 2, 
    "three": 3,
}
print(test_dict)

test_dict = dict()
print(test_dict, type(test_dict))

test_dict = {} # 딕셔너리는 {중괄호} 사용함.
print(test_dict, type(test_dict))