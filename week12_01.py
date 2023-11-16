# week12_01.py
list_score = [10, 20, 30, 40, 50, 60]

num1 = input("분자:")
num1 = int(num1) # ValueError: invalid literal for int() with base 10: 'hi' 

num2 = input("분모:")
num2 = int(num2)

result = num1 // num2 # ZeroDivisionError: integer division or modulo by zero (분모에 0 넣었을 때 발생)
print(result)

print(list_score[result]) # IndexError: list index out of range (result가 5보다 클 때 발생)