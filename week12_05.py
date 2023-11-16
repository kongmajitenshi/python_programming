# week12_05.py
# p.371

list_score = [10, 20, 30, 40, 50, 60]
while True:
    try: # 실행하고자 하는 코드 블록
        num1 = input("분자:")
        num1 = int(num1) 

        num2 = input("분모:")
        num2 = int(num2)

        result = num1 // num2 
        print(result)

        print(list_score[result])
        break
    except: # 실행중 문제가 발생하면 처리하는 코드 블록. except문 실행 되어도 코드가 종료되지 않음.
        print("예외 발생")
        print("비정상 종료")
    # else: # else문이 실행이 되지 않음. 필요없는 코드.
        # print("정상 종료")
    # finally: # finally문이 실행 되어도 while문 밖으로 빠져나가지 않음 > 아예 밖에다 print("완전종료") 하는게 나음.
        # print("완전 종료")