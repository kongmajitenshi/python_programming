my_major = "컴퓨터정보"
my_major += " 1학년"
my_major += " 파이선프로그래밍" # +=로 붙이는건 문자열을 새롭게 만드는 것임.
print(my_major)


mymajor = "컴퓨터정보"

print(mymajor[:]) # 시작 끝 지정 안해줌 = 처음부터 끝까지.
print(mymajor[0:5:2]) # 0~4 까지 두 칸 씩 점프 = 컴(퓨)터(정)보
print(mymajor[0:5:1]) # 0~4 까지 한 칸 씩 점프(그대로)

# 슬라이싱
print(mymajor[0:3]) # 0번 인덱스 부터 3번 전까지.
print(mymajor[1:3])
print(mymajor[2:3]) # 2번만 뽑힘.
print(mymajor[:3]) # 시작점 지정 안해줌 = 처음부터
print(mymajor[3:5])
print(mymajor[3:]) # 종료점 지정 안해줌 = 끝까지
print(mymajor)

# 인덱싱
print(mymajor[-1])
print(mymajor[0])
print(mymajor[1])
print(mymajor[2])
print(mymajor[3])
print(mymajor[4])
# print(mymajor[5]) 얘가 에러가 남. 범위 벗어나면 오류남.
print(mymajor)

# print("=-" * 30)
#
# print(20 + 20)
# print("나이:" + "20")
# print("나이:" + 20)
# 파이썬은 반드시 타입이 같아야함.