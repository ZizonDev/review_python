# 키는 cm 단위로 입력 받습니다.
# 체중에 대한 출력은 소수점 이하 두 자리까지 출력 합니다.

def std_weight(height, gender):
    if gender == "남성":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남성"
weight = round(std_weight(height / 100, gender), 2) # 반올림 함수, 사사오입과 약간 다르게 동작
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")