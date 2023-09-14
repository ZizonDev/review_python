# 선생님 풀이
# 회원 정보 함수로 출력하기 (Sol 2)

def input_age():
    while True:
        age = input("나이를 입력하세요 : ")
        if age.isdigit():  # isdigit : 입력받은 문자열(age)이 숫자로 구성되어 있는 지 확인.
            age = int(age)
            if 0 < age < 200: return age
        print("나이가 잘못 입력되었습니다.")

def input_gender():
    while True:
        gender = input("성별을 입력하세요 : ")
        if gender == 'M' or gender == 'm':
            return "남성"
        elif gender == 'F' or gender == 'f':
            return "여성"
        print("성별이 잘못 입력되었습니다.")

def input_job():
    while True:
        job = input("직업을 선택하세요. [1]학생 [2]주부 [3]회사원 [4]무직 : ")
        if job.isdigit():
            job = int(job)
            if 0 < job < 5:
                return job
        print("직업이 잘못 입력되었습니다.")

def print_info(name, age, gender, job):
    job_str = "", "학생", "회사원", "주부", "무직"
    print("="*5, " 회원 정보 ", "="*5)
    return "="*10 + "\n" + f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {job_str[job]}\n"


member_info = "member.txt"
fd = open(member_info, "wt", encoding="utf-8")    # file description & write text(쓰기 위해 파일 오픈) cf) 읽기 위해 오픈하려면 "r"(read)

# 함수는 선언 이후 호출해야 동작한다.
while True:
    name = input("이름을 입력하세요 (종료하려면 quit): ")
    if name == "quit": break
    age = input_age()
    gender = input_gender()
    job = input_job()
    rst = print_info(name, age, gender, job)
    fd.write(rst + "\n")        # 회원 정보를 파일에 저장하고 싶음.
fd.close()


# 회원 정보 출력하기 (Sol 1)
# name = input("이름을 입력하세요 : ")
# while True:
#     age = input("나이를 입력하세요 : ")
#     if age.isdigit():                   # isdigit : 입력받은 문자열(age)이 숫자로 구성되어 있는 지 확인.
#         age = int(age)
#         if 0 < age < 200: break
#     print("나이가 잘못 입력되었습니다.")    # age가 숫자가 아닌 경우 잘못 입력했다는 메세지 출력하도록. (들여쓰기 중요!!!)
# while True:
#     gender = input("성별을 입력하세요 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
#         break
#     print("성별이 잘못 입력되었습니다.")
# while True:
#     job = input("직업을 선택하세요. [1]학생 [2]주부 [3]회사원 [4]무직 : ")
#     if job.isdigit():
#         job = int(job)
#         if 0 < job < 5: break
#     print("직업이 잘못 입력되었습니다.")
#
# if gender == 'M' or gender == 'm': gender_str = "남성"
# else: gender_str = "여성"
#
# job_str = "", "학생", "주부", "회사원", "무직"       # 튜플은 list와 거의 유사하나, list와 다르게 튜플은 내용을 바꿀 수 없다.
#
# print("="*3, " 회원 정보 ", "="*3)
# print(f"""이름 : {name}
# 나이 : {age}
# 성별 : {gender_str}
# 직업 : {job_str[job]}""")


