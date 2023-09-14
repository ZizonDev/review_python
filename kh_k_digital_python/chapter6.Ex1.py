# 무작위 수를 공백을 기준으로 입력 받아 홀수와 짝수로 리스트에 나누어 담고 출력하기.
num = list(map(int, input().split()))
odd = []
even = []
for i in range(len(num)):
    if num[i] % 2 == 0:
        even.append(num[i])
    else:
        odd.append(num[i])
print(odd)
print(even)

# lambda 이용한 방법.
numbers = list(map(int, input().split()))
odds = list(filter(lambda e: e % 2 != 0, numbers))
evens = list(filter(lambda e: e % 2 == 0, numbers))
print(odds)
print(evens)

# 선생님 풀이
n = list(map(int, input().split()))
o = []
e = []
for i in n:
    if e % 2 == 0: e.append(i)
    else: e.append(i)
print(f"홀수 : {o}")
print(f"짝수 : {e}")

# 선생님 풀이 2 나랑 똑같음 오예
# map : 전달 받은 값을 함수 내부에서 가공 후 전달 받은 값의 개수 그대로 반환. (입력 변수의 개수 == 출력 개수)
# filter : 전달 받은 값을 함수 내부에서 가공하는 것은 동일. but 함수 조건에 부합하는 값만 출력. (입력 변수의 개수와 출력 개수가 다를 수 있다.)