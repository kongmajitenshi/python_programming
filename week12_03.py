# week12_03.py
# p.369

list_score = [10, 20, 30, 40, 50, 60]
try: # 실행하고자 하는 코드 블록

    num1 = input("분자:")
    num1 = int(num1) 

    num2 = input("분모:")
    num2 = int(num2)

    result = num1 // num2 
    print(result)

    print(list_score[result])
except: # 실행중 문제가 발생하면 처리하는 코드 블록
    print("예외 발생")
    print("비정상 종료")
else: # p.369
    print("정상 종료")