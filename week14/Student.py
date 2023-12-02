# Student.py
import random
import datetime as dt
import os # 파일처리 할 땐 항상 신경쓰기. 파일 있나 없나 검사, 폴더인지 검사 등을 수행.

class Student:
    time_format = "%Y-%m-%d %H:%M:%S" # %Y/%m/%d 형태 혹은 %Y%m%d 형태로도 사용 가능. 시분초도 뺄 수 있음.
    # time_format은 class Student 에서 쓸거니까 클래스 내에 선언. 클래스 변수.
    # 메소드에서 클래스 변수에 접근할 땐 '클래스명.변수명' 형태로 접근해야함.
    #strftime() format.
    #strptime() 둘 다 잘 써야함. parse.
    def __init__(self, number, name, kor=0, math=0, eng=0, regdate=None) -> None: # 들어온 매개변수들은 다 지역변수.
        self.number = number # 여기서 인스턴스를 초기화해줌. 이런애들을 인스턴스부르라고 부름. self.변수명 으로 선언.
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        if regdate == None: # 지금 날짜가 등록 날짜인 경우
            day = random.randrange(-2, 3) # 시작,끝 값 주면 그 사이에 알아서 랜덤값. -2<=random<3
            self.regdate = dt.datetime.now() + dt.timedelta(days=day)
        else:
            self.regdate = regdate

    def get_sum(self):
        return self.kor+self.math+self.eng

    def get_average(self):
        return self.get_sum()/3
    
    def __str__(self) -> str :
        # return "{},{},{}".format()
        average = self.get_average()
        return f"이름:{self.name} 학번:{self.number} 평균:{average:0.1f}"

    def __gt__(self, value) -> bool: # 크다, self=나, value=너 라고 생각하면 편함 
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum() # 참이면 True, 아니면 False

    def __lt__(self, value) -> bool: # 작다
        if isinstance(value, Student):
            return self.get_sum() < value.get_sum()
        
    def __eq__(self, value) -> bool: # 같다
        if isinstance(value, Student):
            return self.get_sum() == value.get_sum() 

    def __ne__(self, value) -> bool: # 다르다
        if isinstance(value, Student):
            return self.get_sum() != value.get_sum()
        
    def make_record(self):
        str_time = dt.datetime.strftime(self.regdate, Student.time_format)
        return f"{self.number}|{self.name}|{self.kor}|{self.math}|{self.eng}|{str_time} \n" # 레코드는 줄바꿈 필수.


if __name__ == "__main__": # 시작 모듈일 때만 실행하도록. import한 경우엔 사용x 
    # student = Student()
    target_path = "c:\\202344018"
    target_file = "scores.txt"
    target_full_file = os.path.join(target_path, target_file) # 하나로 합쳐줌.
    print(target_full_file)
    students = []
    if os.path.exists(target_full_file):
        with open(target_full_file, "r") as file: # encoding은 통일해줘야함.
            for record in file: # 한줄씩 읽을 때 이렇게 쓰면 굿 
                record = record.strip()
                fields = record.split("|")
                if len(fields) == 6:
                    number = fields[0]
                    name = fields[1]
                    kor = int(fields[2])
                    math = int(fields[3])
                    eng = int(fields[4])
                    regdate = dt.datetime.strptime(fields[5], Student.time_format)
                    stu = Student(number, name, kor, math, eng, regdate)
                    students.append(stu) # 얘는 , 으로 들어가지않나?
    # 이제 어카지? 코드가 아니라 키보드로 입력을 받으면 되겠다!

    # (1) 입력할 때마다 파일에 저장, "a"
    # with open(target_full_file, "a") as file:
    #     while True:         
        #     number = input("학번:")
        #     name = input("이름:")
        #     kor = input("국어:")
        #     math = input("수학:")
        #     eng = input("영어:")

        #     student_info = Student(number,name,kor,math,eng)
        #     file.write(student_info.make_record())

        #     yesorno = input("계속?")
        #     if yesorno.upper().strip() == "Y":
            #     continue
            # else:
            #     break
        
    # (2) 입력 모두 받고 새로 받은 내용만 한 번에 저장, "a"
    with open(target_full_file, "a") as file:
        student_info_list = []
        while True:
            
            number = input("학번:").strip()
            name = input("이름:").strip()
            kor = int(input("국어:"))
            math = int(input("수학:"))
            eng = int(input("영어:"))

            student_info = Student(number,name,kor,math,eng)
            student_info_list.append(student_info)

            yesorno = input("계속 할래?")
            if yesorno.upper().strip() == "Y":
                continue
            else:
                for student_info in student_info_list:
                    file.write(student_info.make_record())
                break
    # (3) 기존+신규 모두 새로 저장, "w"
    # (1), (2), (3) 을 모두 만들어보세요~ 3 동작 모두 while문으로 돌리면 됨.
    

    # students = [
    #     Student(12345,"김인하",100,98,80),
    #     Student(12346,"이인하",100,98,80),
    #     Student(12347,"박인하"),
    # ]


    # for stu in students:
    #     print(stu.make_record())
    #     # print(stu)
    #     # print(stu.number)
    #     # print(stu.name)
    #     # print(stu.kor, stu.math, stu.eng)
    #     # print(stu.get_average())
    #     # print("-"*10)
        
    #     # print(students[0] == students[1]) 
    #         # __eq__ 선언 전: False 얘는 같은 인스턴스인가? 하고 물어보는거.
    #         # __eq__ 선언 후: get_sum() 결과값 크기 비교
    #     # print(students[0] != students[1]) # True
    #     # print(students[2] < students[1])
    #     # print(students[2] > students[1])

    # if not os.path.exists(target_path): #target_path가 존재하지 않냐? 없으면 만들려고 물어보는거.
    #     os.mkdir(target_path)

    # with open(target_full_file, "a", encoding="utf8") as file: 
    #     # encoding [cp949:한글윈도우기본인코딩/utf8:가변유니코드, 다른 언어와 호환 위해서 많이 사용]
    #     for stu in students:
    #         file.write(stu.make_record())
