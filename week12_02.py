# week12_2.py
# p.366

try: # 실행하고자 하는 코드 블록
    pass
except: # 실행중 문제가 발생하면 처리하는 코드 블록
    pass

list_score = [10, 20, 30, 40, 50, 60]

num1 = input("분자:")
num1 = int(num1) 

num2 = input("분모:")
num2 = int(num2)

result = num1 // num2 
print(result)

print(list_score[result]) 