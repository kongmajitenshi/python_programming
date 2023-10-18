# p072.py
bibim = {
    '양념' : '고추장',
    '고명' : ['버섯', '계란', '콩나물', '시금치', '육회']
}

print(f"비빔밥의 양념은{bibim['양념']}, 고명은", ",".join(bibim['고명']),"입니다.")

fav_fruits = {
    'kim' : ['딸기','오렌지'],
    'choi' : ['청포도','무화과'],
    'lee' : ['복숭아','귤','배'],
    'park' : ['키위','자두']
}

for name, fruits in fav_fruits.items() :
    print(f"{name}이 좋아하는 과일은 아래와 같다.")
    for fruit in fruits :
        print(f"\t{fruit}")

# for idx, name in enumerate(fav_fruits) :
#     print(f"{name}이 좋아하는 과일{fruit}이 있다.")
