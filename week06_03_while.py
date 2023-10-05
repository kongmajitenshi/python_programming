# week06_03_while.py

# p.244

infos = {"123": ["kim inha", 22], "124": ["kim inha", 21]}

# while True :
#    number = input("school number:").strip() # strip()으로 양쪽공백제거
#    if not(number in infos) :
#        print(f"can not find \"{number}\"")
#        continue
#    else :
#        print(f"name:{infos[number][0]}")
#        break

while True :
    number = input("school number:").strip() # strip()으로 양쪽공백제거
    if number in infos :
        print(f"name:{infos[number][0]}")
    else :
        print(f"can not find \"{number}\"")
    yesorno = input("continue to find? (Y, N)").strip()
    if yesorno.upper() != "Y" :
        break

print("\n"*10)


while True :
    number = input("school number:").strip() # strip()으로 양쪽공백제거
    if number in infos :
        print(f"name:{infos[number][0]}")
        break
    else :
        print(f"can not find \"{number}\"")
        yesorno = input("continue to find? (Y, N)").strip()
        if yesorno.upper() != "Y" :
            break

print("\n"*10)


number = input("school number:").strip() # strip()으로 양쪽공백제거
if number in infos :
    print(f"name:{infos[number][0]}")

print("\n"*10)


# p.240
fruits = ["딸기", "귤", "키위", "키위", "복숭아"]

target = "키위"
while target in fruits : 
    fruits.remove(target)
print(fruits)
print("\n")

i = 0
while i < len(fruits) :
    print(f"{i+1}:{fruits[i]}")
    i += 1