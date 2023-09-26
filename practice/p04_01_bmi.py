weight = float(input("너의 무게는(kg)?"))
height = float(input("너의 키는(m)?"))

bmi = round(weight / height**2, 2)

if 90<bmi<=110 :
    print("BMI:",bmi,"(정상)")
elif bmi<=90 :
    print("BMI:",bmi,"(저체중)")
elif 110<bmi<=120 :
    print("BMI:",bmi,"(과체중)")
elif 120<bmi<=140 :
    print("BMI:",bmi,"(비만)")
elif 140<bmi :
    print("BMI:",bmi,"(고도비만)")
