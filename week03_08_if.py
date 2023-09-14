# week03_08_if.py
# p.183

height = float(input("키: "))
if height < 120.0:
    pass # pass는 아무것도 실행하지 않고 말 그대로 pass 하는 것. 
else:
    pass


# p.163 
if True : 
    print("참")
    print("트루")
    if 10 < 100:
        print("참참참")

if False :
    print("거짓") # 문법상 문제는 없지만 False 이므로 평생 7번줄 실행 x 라서 흐릿함


a = 10
if a % 2 == 0: 
    print("통과")