# 데코레이터 : 이미 만들어진 함수의 앞과 뒤에 기능을 추가할 때 사용.
import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_deco
def for_sum():
    sum = 0
    for i in range(1, 100):
        sum += i
    print(sum)

# 첫번째 방법
# test = datetime_deco(for_sum)
# test()

# 두번째 방법
for_sum()