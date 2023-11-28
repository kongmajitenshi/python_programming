# 202344018 김대희

import datetime

class Car:
    def __init__(self, number) -> None:
        self.number = number
        self.intime = datetime.datetime.now()
        self.outtime = None

    
    def set_out(self):
        self.outtime = datetime.datetime.now()


    def is_out(self):
        if self.outtime != None:
            return True # 출차 시 True
        else:
            return False # 출차 X 시 False
        

    def cal_price(self, hour=2000):
        if self.is_out() == True:
            totaltime1 = self.outtime - self.intime
            totaltime1 = (totaltime1.total_seconds() / 3600)
            price1 = totaltime1 * hour
            return int(price1)
        else:
            self.nowtime = datetime.datetime.now()
            totaltime2 = self.nowtime - self.intime
            totaltime2 = (totaltime2.total_seconds() / 3600)
            price2 = totaltime2 * hour
            return int(price2)
        
            
    def __str__(self) -> str :
        intime = self.intime.strftime("%Y-%m-%d %H:%M:%S")
        if self.outtime == None:
            return f"입차: {intime}, 차령번호: {self.number}, 주차중"
        else:
            return f"입차: {intime}, 출차:{self.outtime.strftime('%Y-%m-%d %H:%M:%S')}, 차량번호: {self.number}"