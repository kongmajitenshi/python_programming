# week05_07_dict.py
infos = {
    "20230001":{"name":"kim inha", "age":21 },
    "20230002":{"name":"choi comsung", "age":22, "major":"컴정" }
}

infos["20230003"] ={}
infos["20230003"]["name"] = "yi comsi"
infos["20230003"]["major"] = "컴시"

infos["20230004"] = {
    "name" : "wange junja",
    "major" : "전자"
} # 딕셔너리에는 KeyError가 존재함.

print(infos)

test_dict = {1:"uno", 2:"two", 3:"three"}

test_dict[5] = "five"
print(test_dict)

test_dict[1] = "one"
print(test_dict)

del test_dict[2]
print(test_dict)
