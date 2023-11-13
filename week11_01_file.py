# week11_01_file.py

try:
    # 열기
    # file = open("c:\\test_a\\test01.txt", "a") # \\를 두 개 넣은 이유 > 하나만쓰면 아스키코드처럼 쓰여짐. 그래서 두 개 씀.
    # file = open(r"c:\test_a\test01.txt", "w")
    # file = open("c:/test_a/test01.txt", "w")
    file = open("c:\\test_a\\test01.txt", "w")

    # 작업

    # print(file)
    file.write("김인하\n")
    file.write("컴퓨터정보\n")
    file.write("1학년\n")
    file.write("이인하|컴퓨터시스템|2학년\n")

    # 닫기
    file.close()
except: # 어디서든지 에러가 나면 except로 점프.
    print("ERROR")
# try - except 는 세트임.

