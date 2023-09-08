# a*b*c 에서 0~9가 몇 번 쓰였는지 숫자의 개수 구하기
# 선생님 풀이
a, b, c = map(int, input("3개의 정수 입력 : ").split())     # a,b,c를 map으로 묶어서 한 번에 정수형으로 입력받겠다.
total_val = str(a * b * c)                               # 결과 a*b*c를 문자열로 변환.
for i in range(10):                                      # i는 0부터 9까지 10번 돌면서 몇 번 나왔는지 count한다.
    print(total_val.count(str(i)))


# print(ord('0'))     # 48
# print(ord('1'))     # 49
# print(ord('9'))     # 57

# a = int(input())
# b = int(input())
# c = int(input())
# n = [a*b*c]
# for i in range(0, len(n)):
#     print(list.find(0))
