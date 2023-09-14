# 세 자리수 정수 입력 받아 가장 큰 수 출력하기.

a = b = c = 0
def num_split(input):
    global a, b, c
    a = input // 100
    b = input % 100 // 10
    c = input % 100 % 10

def compare_num():
    if a > b:
        if a < c: return a
        else: return c
    else:
        if b > c: return b
        else: return c

n = int(input())
num_split(n)
print(compare_num())