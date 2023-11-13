# week11_03_file.py
import os

if os.path.exists("c:\\test_q\\test01.txt"):
    file = open("c:\\test_q\\test01.txt", "r")

    # 세 번째 방식
    data = file.read()
    print(data.split("\n"))

    # 두 번째 방식
    # lines = file.readlines() # map()이나 리스트내포로 \n 제거해주면 됨
    # lines = [line.strip() for line in lines] # split()은 리스트로 반환. map() split() strip() 구별해보기
    # print(lines)

    # 첫 번째, 고전적인 방식
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     line = line.strip() # 좌우공백, 탭, 줄바꿈 등 제거 C#에선 trim()이라 함.
    #     print(line)

    file.close()