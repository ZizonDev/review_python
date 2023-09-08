# 중복 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = []     # 빈 리스트 생성하기
while True:
    rand = random.randrange(1, 46)      # 1이상 46미만에서 임의의 정수값 생성
    if rand not in ls:                            # rand 값이 ls에 포함되지 않으면...(중복 값 제외)
        ls.append(rand)                           # append : add와 유사한 기능.
    if len(ls) == 6:
        break
print(ls)