import datetime

# 학번:
# 이름:
# 자리번호

menu = """======================
0. while문을 이용하여 정수 5개를 받아서
  최소값과 최대값을 구한다.(min/max 함수 이용)

1. 입력(수입/지출)
2. 일별 현황
3. 달별 현황
4. 연별 현황
5. 종료
======================"""

"""
아래는 기본으로 주어지는 데이터 입니다
housekeepingbook의 key는 연도를 의미
해당 키에 아래 리스트를 추가한다.
m : 월
d : 일
type : 수입('1') , 지출('2')
money : 금액
content : 내역
"""

housekeepingbook = dict()
housekeepingbook[2018] = list()
housekeepingbook[2018].append(
    {"m": 10, "d": 5, "type": "1", "money": 2000000, "content": "월급"}
)
housekeepingbook[2018].append(
    {"m": 10, "d": 15, "type": "2", "money": 340000, "content": "카드"}
)
housekeepingbook[2018].append(
    {"m": 11, "d": 5, "type": "1", "money": 2000000, "content": "월급"}
)
housekeepingbook[2018].append(
    {"m": 11, "d": 15, "type": "2", "money": 77000, "content": "카드"}
)
housekeepingbook[2018].append(
    {"m": 12, "d": 5, "type": "1", "money": 2200000, "content": "월급"}
)
housekeepingbook[2018].append(
    {"m": 12, "d": 15, "type": "2", "money": 450000, "content": "카드"}
)
housekeepingbook[2018].append(
    {"m": 12, "d": 17, "type": "2", "money": 35000, "content": "통신비"}
)
print(housekeepingbook)
now = datetime.datetime.now()  # 오늘 날짜시간
year = now.year  # 오늘 연도
month = now.month  # 오늘 월
day = now.day  # 오늘 일


def register(reg_type):
    if reg_type == 1 :
        pass
    elif reg_type == 2 :
        pass
    # 1,2 중 하나가 입력되면
    # 금액과 내역을 입력받아
    # 1번이 입력되면 수입 type으로 데이터 저장
    # 2번이 입력되면 지출 type으로 데이터 저장


def searchDay(ymd):
    pass
    #'연 월 일'을 입력받아
    # 해당 연도,월,일의 입력상황을 예시와 같이 출력한다.
    # 내역/수입/지출 순서로


def searchMonth(ym):
    pass
    #'연 월'을 입력받아
    # 해당 연도, 월의
    # 수입별 총건수와 총 수입액과 지출별 총건수와 총 지출액을 출력한다.


def searchYear(y):
    pass
    # 해당 연도의
    # 수입 중에 가장 최소 금액과 최대 금액을 출력한다.
    # 지출 중에 가장 최소 금액과 최대 금액을 출력한다.


while True:
    print(menu)
    temp = input(">> ")

    if temp == "":
        continue

    selNo = int(temp)

    if selNo == 0:
        # while문을 이용하여 정수 5개를 받아서 최소값과 최대값을 구한다.(min/max 함수 이용)
        while True :
            i = 0
            # num = list()
            # for a in range(0,5,1) :
            # num = list(map(int, input("정수 5개 입력 : ").split()))
            num = [int(x) for x in input("정수 5개 입력: ").split()]
            # num.append(int_num)
            print("max:", max(num[0:5]), "min:", min(num[0:5]))
            break

    elif selNo == 1:
        temp = input("수입(1) 지출(2) 선택:")
        if register(temp) != 1 or 2:
            print("입력 오류")
        else :
            register(temp)

    elif selNo == 2:
        temp = input("연 월 일:")
        searchDay(temp)

    elif selNo == 3:
        temp = input("연 월:")
        searchMonth(temp)

    elif selNo == 4:
        temp = input("연:")
        searchYear(temp)

    elif selNo == 5:
        break

print("좋은 하루 되세요")
