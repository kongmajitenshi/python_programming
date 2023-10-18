# p071.py

'''리스트의 딕셔너리'''
alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'red', 'points':15}
alien_2 = {'color': 'blue', 'points':20}
aliens = [alien_0, alien_1, alien_2]

for idx in range(len(aliens)) :
    print(f"{idx+1}번 외계인 색상:{aliens[idx]['color']}")

for idx, alien in enumerate(aliens) :
    print(f"{idx+1}번 외계인 점수:{alien}")

'''딕셔너리의 딕셔너리'''
students = {'12210001' : {'name' : 'kim', 'major' : 'com'},
            '12210011' : {'name' : 'choi', 'major' : 'nur'},
            '12210111' : {'name' : 'lee', 'major' : 'edu'}
            }

for num, stu in students.items() :
    print(f"학번:{num}")
    print(f"이름:{stu['name']}")
    print(f"학과:{stu['major']}")
    print("----")