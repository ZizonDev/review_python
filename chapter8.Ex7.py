# 소수의 합구하기. (입력 받은 수 미만의 소수의 합을 구해서 출력 하기)

def prime_function(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0: is_prime = False
    if is_prime : return n
    else : return 0

n = int(input("정수 입력 : "))
sum = 0
for i in range(2, n) :
    sum += prime_function(i)
print(sum)
