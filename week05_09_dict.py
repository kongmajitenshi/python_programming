# week05_09_dict.py
infos = {
    "20230001":{"name":"kim inha", "age":21 },
    "20230002":{"name":"choi comsung", "age":22, "major":"컴정" }
}

# p.256
for key, value in infos.items() : # key와 value 모두 뽑아줌. 선 key, 후 value 뽑아줌.
    print(key, value)
print()


# p.226
for value in infos.values() : # 값만 뽑아줌.
    print(value)
print()

for key in infos.keys():
    print(infos[key])
print()

for key in infos.keys():
    print(key)
print()

for key in infos:
    print(key)