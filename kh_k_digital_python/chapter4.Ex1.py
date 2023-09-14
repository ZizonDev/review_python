# # 구구단 찍기
for i in range(2, 10):      # 2단부터 9단까지
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")
    print()

# # 홀수 / 짝수 나누어 찍기
n = int(input("정수 입력 : "))
for i in range(0, n):
    for j in range(0, n):
        if j % 2 == 0: print("짝", end=' ')
        else: print("홀", end=' ')
    print()

# n * n 크기의 행렬 출력하기 (1~n*n까지 순차적으로)
n = int(input("정수 입력 : "))
for i in range(1, n*n + 1):
    print(f"{i:<3}", end=' ')
    if i % n == 0: print()

# n = int(input("정수 입력 : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         sum += j
#         print(sum, end = ' ')
#         if sum % n == 0: print()
