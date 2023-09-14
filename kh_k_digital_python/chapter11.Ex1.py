# [문제] 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성하시오.
# [입력] 첫째 줄에 n이 주어진다. 다음 줄부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다.
#       이 수는 0보다 크고, 10,000보다 작다. 목록은 0으로 끝난다.
# [출력] 목록에 있는 수가 n의 배수인지 아닌지를 구한 뒤 예제 출력처럼 출력한다.
# [예제] 1 is NOT a multiple of 3.
#       7 is NOT a multiple of 3.
#       99 is a multiple of 3.
#       777 is a multiple of 3.

n = int(input())
ls = []                     # 빈 리스트 생성.
while True:                 # 0이 입력되기 전까지 반복 수행.
    x = (int(input()))      # 리스트에 들어갈 수.
    if x == 0:
        break               # 0이 입력되면 while문 탈출.
    else:
        ls.append(x)
for e in ls:
    if e % n == 0:
        print(f"{e} is a multiple of {n}.")
    else:
        print(f"{e} is NOT a multiple of {n}.")