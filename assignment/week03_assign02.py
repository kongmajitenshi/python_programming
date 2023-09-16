num1 = input("문자 입력: ")
num1 = int(num1)

num2 = input("문자 입력: ")
num2 = int(num2)

num3 = input("문자 입력: ")
num3 = int(num3)

sum = num1 + num2 + num3
avg = round(sum / 3, 2)

print("1st:", num1)
print("2nd:", num2)
print("3rd:", num3)
print(num1,",",num2,",",num3,"의 평균은",avg,"입니다.")

