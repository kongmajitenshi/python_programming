# week13\student.py #패턴을 외우는게 좋음
# 학생 정보를 관리하는 class
# class == 자료형을 만들 때 사용하는 문법
# self 매개변수 : 호출한 당사자, 호출한 값(데이터), 호출한 인스턴스(객체, object)(데이터+기능)
# i = int(1) ~> i는 int형 값을 가리키고 있다.
# i는 int형 인스턴스를 가리키고 있다. <- 이게 더 정확한 표현. 

class Student1:
    pass

class Student2: # Student1 에도 def __init__(self) 가 존재함. 생략된 것 뿐. 즉, 구조는 같음.
    def __init__(self): # __init__(self) -> None 가 기본.
        pass

class Student3: 
    def __init__(self) -> None: # init은 initionalize의 약자. 초기화. self = 만들어진 값 자체를 의미함.
        self.name = "" # stu3이 호출하면 stu3=self가 됨. 즉, self는 날 부른놈임.
        self.number = ""
        self.major = ""

class Student4: 
    def __init__(self, name, number, major="") -> None: 
        self.name = name
        self.number = number
        self.major = major

    # print()호출 시 아래 메소드 호출.
    # 모든 클래스에는 __str__()가 있음.
    # 기본 정의 된 값을 재정의하여 원하는 문자열로 바꾼 것.
    def __str__(self) -> str :
        return f"{self.name}/{self.number}/{self.major}"