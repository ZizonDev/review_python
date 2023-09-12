# 두번째 수 찾기. 찾는 2번째 수가 없으면 -1 반환

def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i+1
            else: cnt += 1
    return -1

ls = list(map(int, input("리스트 입력 : ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls, n))