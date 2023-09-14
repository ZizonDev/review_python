# 반복문 : 조건이 참인 동안 계속 수행되는 반복문.
n = int(input("정수를 입력하세요 : "))
sum = 0             # 쓰레기 값을 처리하기 위해 sum은 반드시 초기화 되어야 함.
while n:            # python은 정수값이 0이 아니면 참으로 간주함.
    sum += n        # n을 계속 더해줘.
    n -= 1          # 1부터 n까지 더해줘. python은 증감 연산자가 없음에 유의.
print(sum)

while True:
    age = int(input("나이를 입력하세요 : "))
    if 0 <age < 200: break
    else: print("나이 입력 범위가 벗어났습니다.")

# for 요소 in 시컨스 : 시퀀스의 각 요소를 순회하는 데 사용. (= java의 향상된 for 문과 비슷함.)
fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]
print(fruits[3][1][0])
for e in fruits:
    print(e[0])

str1 = "서울시 강남구 역삼동 KH정보교육원"
for e in str1:
    print(e, end="/")
print()
# for 변수 in range(시작값, 종료값, 증감값):
num = int(input("정수를 입력하세요 : "))
sum = 0
for i in range(1, num+1):     # 1부터 n+1 미만까지. 1 이상 n 이하
    sum += i
print(sum)

# for문을 역순으로 반복하기
for i in range(10, -1, -1):    # 10부터 0까지 출력, -1씩 감소하면서.
    print(i)

# 이중 for문
n = int(input("정수를 입력하세요 : "))
for i in range(0, n):
    for j in range(0, n):
        print("*", end=' ')
    print()
