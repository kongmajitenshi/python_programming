# car.py
import os
from datetime import datetime as dt

dir_name = "c:\\202344018\\parking_system\\"
datetimeformat = "%Y-%m-%d %H:%M:%S"
car_list = []

def filename(number):
    return dir_name + "/" + number + ".txt"

def isfolder():
    return os.path.isdir(dir_name)

def mkfolder():
    if not isfolder():
        os.mkdir(dir_name)

def isfile(number):
    return os.path.isfile(filename(number))

def strtotime(data):
    data = data.strip()
    return dt.strptime(data, datetimeformat) # 문자열 > 시간

def timetostr(data):
    return dt.strftime(data, datetimeformat) # 시간 > 문자열

def searchnumber(number):
    for index, car in enumerate(car_list):
        if car['number'] == number:
            return index
        
def deletefile(number):
    if isfolder() and isfile(number):
        os.remove(filename(number))

def readfile():
    if isfolder():
        file_list = os.listdir(dir_name)
        for file in file_list:
            with open(dir_name + "/" + file, "r") as f:
                lines = f.readlines()
                if len(lines) == 2:
                    try:
                        number = lines[0].strip()
                        intime = strtotime(lines[1])
                        car_list.append({'number':number, 'intime':intime})
                    except:
                        continue

def writefile(car_info):
    mkfolder()
    with open(filename(car_info['number']), "w") as f:
        f.write(car_info['number'])
        f.write('\n')
        f.write(timetostr(car_info['intime']))
        f.write('\n')

def gettime(intime):
    return int((dt.now() - intime).total_seconds() / 60) # 분당

def getprice(parkingtime):
    return parkingtime * 100 # 분당 100원

def showcar():
    for index, car in enumerate(car_list):
        print(f"[{index:2}] {car['number']} {timetostr(car['intime'])}")

def doin(number):
    car_info = {'number':number, 'intime':dt.now()}
    car_list.append(car_info)
    writefile(car_info)
    return car_info

def doout(index):
    parkingtime = gettime(car_list[index]['intime'])
    price = getprice(parkingtime)

    deletefile(car_list[index]['number'])
    del car_list[index]

    return parkingtime, price