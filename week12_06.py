# week12_06.py
# p.383

list_score = [10, 20, 30, 40, 50, 60]
try: 

    num1 = input("분자:")
    num1 = int(num1) 

    num2 = input("분모:")
    num2 = int(num2)

    result = num1 // num2 
    print(result)

    print(list_score[result])
except Exception as ex: 
    # ex의 정보는 주로 로그 파일에 저장한다.
    print(type(ex))
    print(ex)
    print("예외 발생")
    print("비정상 종료")
