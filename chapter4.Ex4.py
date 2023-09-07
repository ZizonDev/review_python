name = input("이름 입력 : ")
while 1:
    age = int(input("나이 입력 : "))
    if 0 < age < 200: break
    else:
        print("나이 입력 범위가 벗어났습니다.")
while 1:
    gender = input("성별 입력 : ")
    if gender=='m'or'M': gender = "남성"
    elif gender=='f'or'F': gender = "여성"
    else: print("성별을 잘못 입력하셨습니다.")
while 1:
    job = int(input("직업 입력 [1]학생 [2]회사원 [3]주부 [4]무직 : "))
    if job == 1: job = "학생"
    elif job == 2: job = "회사원"
    elif job == 3: job = "주부"
    elif job == 4: job = "무직"
    else: print("직업을 다시 선택하세요.")

print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {job}")
