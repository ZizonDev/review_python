# 문자와 아스키 코드
# chr : 유니코드(한글, 알파벳, ...) 값을 입력받아 그 코드에 해당하는 문자를 출력함.
# ord : 문자의 유니코드 값을 돌려주는 함수.
for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end=" ")
print()

for i in range(65, 91):
    print(chr(i), end=" ")
print()