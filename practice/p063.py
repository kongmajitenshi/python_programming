uncom_users = ['김', '최', '이', '박']
com_users = []

while uncom_users :
    current_user = uncom_users.pop()
    valid = input(f"유효 유저:{current_user} (y/n)").strip().lower() # 공백제거 + 모두 소문자로
    if valid == 'y' :
        com_users.append(current_user)

print("확인한 유저 목록")
for users in com_users :
    print(f"     {users}")
                         
