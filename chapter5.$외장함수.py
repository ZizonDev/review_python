# 외장함수 : python이 기본적으로 제공하지만, import가 필요하다.

# 난수 생성 (random -> randint(), randrange())
import random
# randint(0, 4) : 0 이상 4 이하의 임의의 정수 반환
for i in range(10):
    rand1 = random.randint(0, 4)
    print(rand1)
print("="*10)
# randrange(0, 4) : 0 이상 4 미만의 임의의 정수 반환
for i in range(10):
    rand2 = random.randrange(0,4)
    print(rand2)

# 현재 시간 가져오기 (datetime)
from datetime import datetime   # datetime 안에 datetime 포함 여러 함수 존재... 그 중 datetime만 가져오겠다.
print(datetime.today())         # 현재 날짜 가져오기
print(datetime.today().year)    # 현재 연도 가져오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 수학 계산을 위한 함수 (Math)
import math
print(math.sin(60))
print(math.cos(60))
print(math.tan(60))
print(math.log(math.e))         # log는 자연로그 cf)log2, log10도 있음
print(math.ceil(100.1))         # 올림
print(math.floor(100.9999))     # 내림
print(round(100.5656))          # 반올림 (math의 외장함수가 아님!!!)
