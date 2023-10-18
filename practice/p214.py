# p214.py
numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers :
#     if number >= 100 :
#         print(f"100 이상의 수 : {number}")

for number in numbers :
    if number % 2 == 0 :
        print(f"{number}은 짝수입니다.")
    else :
        print(f"{number}은 홀수입니다.")

print("-------------------------")

for num in numbers :
    if num / 100 >= 1 :
        print(f"{num}은 3자릿수 입니다")
    elif num / 10 >= 1 :
        print(f"{num}은 2자릿수 입니다")
    else :
        print(f"{num}은 1자릿수 입니다")