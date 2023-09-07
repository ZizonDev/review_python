# 문자열 추가하기
"""
2개의 문자열을 포인터 변수 s와 k에 입력 받고, 양의 정수를 정수형 변수 n에 각각 입력 받아
s 문자열의 뒤부터 n개 문자를 k 문자열 앞에 끼워 넣는 코드 만들기
"""
# ex) s : seoul
#     k : korea
#     n : 2
#     결과 : ulkorea

s = input()
k = input()
n = int(input())
v = len(s) - n
p = s[v:]
print(p+k)


# 선생님 풀이
ss = input("s 문자열 : ")
kk = input("k 문자열 : ")
nn = int(input("정수 입력 : "))
print(ss[-nn:] + kk)