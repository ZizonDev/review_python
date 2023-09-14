# 입력으로 들어오는 수의 평균을 구해서 반환 후 출력 하기.

def aver_func(input):
    return sum(input) / len(input)

input = list(map(int, input("정수 입력 : ").split()))
print(aver_func(input))