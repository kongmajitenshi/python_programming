# week13\score.py
class Score1:
    def __init__(self) -> None:
        self.kor = 0
        self.eng = 0
        self.math = 0


class Score2:
    def __init__(self, kor = 0, eng = 0, math = 0) -> None:
        self.kor = kor
        self.eng = eng
        self.math = math


class Score3:
    def __init__(self, kor = 0, eng = 0, math = 0) -> None:
        self.scores = dict()
        self.scores["kor"] = kor
        self.scores["eng"] = eng
        self.scores["math"] = math

    def __str__(self) -> str:
        if len(self.scores) > 0 :
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"
        else:
            return "0"
        

class Score4:
    def __init__(self, *scores) -> None: # * : 가변 매개변수 -> 데이터를 하나의 list로 만들어줌
        self.scores = dict()
        for score in scores:
            self.scores[score] = 0

    def __str__(self) -> str:
        if len(self.scores) > 0 :
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"
        else:
            return "0"
        

class Score5:
    def __init__(self, **scores) -> None: # ** : 키워드 가변 매개변수 ~> dictonary로 만들어줌. key와 value 모두 넣어줘야함.
        self.scores = scores

    def __str__(self) -> str:
        if len(self.scores) > 0 :
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"
        else:
            return "0"
        
# 절차지향언어 : C언어(기능과 값이 분리되어있음)
# 객체지향언어 : C++, 파이썬, 자바, JS, C# 등... (기능과 값이 한번에 담겨있음 => class)
class Score:
    def __init__(self, **scores) -> None: # ** : 키워드 가변 매개변수 ~> dictonary로 만들어줌. key와 value 모두 넣어줘야함.
        self.scores = scores
    

    def get_average(self) -> float: # -> 이 화살표는 그냥 가이드임. return 타입이 이거다~ 하고.
        s = sum(self.scores.values()) 
        l = len(self.scores)
        if l > 0:
            return s / l
        else:
            return 0.0
        

    def add_subject(self, subject, score=0):
        if None == self.scores.get(subject):
            self.scores[subject] = score
            return True
        return False


    def __str__(self) -> str:
        if len(self.scores) > 0 :
            avg = self.get_average()
            return f"평균:{avg:0.1f}"
        else:
            return "0"