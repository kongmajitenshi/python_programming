# week05_08_dict.py

infos = {
    "20230001":{"name":"kim inha", "age":21 },
    "20230002":{"name":"choi comsung", "age":22, "major":"컴정" }
}

number = input("학번: ")
# print(infos[number]) KeyError 발생 확률 높음

info = infos.get(number, "학번이 없어요")
print(info)
print()

# info = infos.get(number)
# print(info) # Key가 없으면 None 반환
# print()


if number in infos : # infos.keys() 를 사용했었지만, 업데이트 되었음.
    print(infos[number])
else:
    print("학번이 없습니다.")