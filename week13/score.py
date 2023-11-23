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