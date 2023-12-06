class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

    def __str__(self):
        return f"이름:{self.name} 국어:{self.kor} 영어:{self.eng} 수학:{self.math} 평균:{self.avg():.2f}"
    
    def avg(self):
        return (self.kor + self.eng + self.math) / 3
    
    def file_content(self):
        return f"{self.name}, {self.kor}, {self.eng}, {self.math}\n"