# 세 자리 정수를 입력 받은 후 가장 큰 수 찾기 (ex. 123 => 3)
num = int(input("세자리 정수를 입력하세요 : "))
a = num // 100
b = num % 100 // 10
c = num % 10
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)


# 선생님 풀이
n = int(input("세 자리 정수 입력 : "))
aa = n // 100               # python에서 몫은 별도로 //로 구해야 한다. 그냥 /로하면 자료형이 없는 python에서 나눗셈을해서 소수점 자리까지 자동으로 출력된다.
bb = n % 100 // 10
cc = n % 10
if aa > bb:
    if aa > cc: print (a)
    else: print(c)
else:
    if bb > cc: print(b)
    else: print(c)
