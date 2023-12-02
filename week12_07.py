# week12_07.py
# p.385

list_score = [10, 20, 30, 40, 50, 60]
try: 

    num1 = input("분자:")
    num1 = int(num1) 
    # "1.1" > 정수 는 안됨. 
    # "1.1" > float("1.1") > int(1.1) => 1 으로 변환해야함.
    num2 = input("분모:")
    num2 = int(num2)

    result = num1 // num2 
    print(result)

    print(list_score[result])
except ValueError as ex: 
    # ex의 정보는 주로 로그 파일에 저장한다.
    print(type(ex))
    print(ex)
    print("정수만 입력")
except IndexError as ex: 
    # ex의 정보는 주로 로그 파일에 저장한다.
    print(type(ex))
    print(ex)
    print(f"결과가 {len(list_score)}보다 크면 안돼")
except ZeroDivisionError as ex:
    print(type(ex))
    print(ex)
    print(f"분모가 0이면 안돼")
except Exception as ex: 
    # ex의 정보는 주로 로그 파일에 저장한다.
    print(type(ex))
    print(ex)
    print("예외 발생")
    print("비정상 종료")
