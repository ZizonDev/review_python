# 산술 연산자 : 사칙연산자(+ , -, *, /,) + //(몫) + **(제곱) + %(나머지)
i = 10      # python은 값이 대입될 때 자료형이 결정됨. python은 자료형 키워드가 없기 때문.
j = 3
print(f"덧셈 : {i + j}")      # f가 없으면 그냥 문자열 출력이 되는 것임. f를 넣으면 변수 대입 가능해짐.
print(f"뺄셈 : {i - j}")
print(f"곱셈 : {i * j}")
print(f"나눗셈 : {i / j}")
print(f"나머지 : {i % j}")
print(f"몫 : {i // j}")
print(f"제곱 : {i ** j}")
test = "Python!!!~~~!!!"
print(test + "hello")
print(str(111) + test)
print(test * 3)             # 문자열 test 3번 반복하겠다는 의미

print(f"증감 연산자 test : {--i}")   # python에 증감 연산자는 없다. --i 해도 원래의 값 10이 나옴.
i += 1
print(f"증감 연산자 : {i}")

# 간단한 예제 1 ; python에서는 변수를 상수로 만드는 방법 X, 관례 상 변수 이름을 모두 대문자로 표시하면 상수로 간주한다.
TAX_RATE = 0.10           # 세율은 상수이므로 대문자로 표현하는 것이 좋음. 다만 python에서는 상수가 없다. 나중에 바꿔줄 수 있음ㅋ
#TAX_RATE = [0.10]        # [] list, () tuple : 튜플은 요소 값을 바꿀 수 없게 함.
#TAX_RATE[0] = 0.12       # 하면 에러 뜸 즉 상수인 TAX_RATE 바꿀 수 없게 억지로 할 수는 있음.
income = int(input("당신의 수입을 입력하세요 : "))
print(f"당신이 내야 할 세금은 {income * TAX_RATE:.2f} 입니다.")     # :.2f -> 소수점 이하 두 자리까지 출력

# 관계 연산자 : AND(&&) -> and , OR(||) -> or , NOT(!) -> not
x = 10
y = 20
z = 30
result1 = x > 0 and x > y
print(result1)                      # False 반환
result2 = x > 10 or y > 10
print(result2)                      # True
result3 = not( x > 0 or x > y )
print(result3)                      # False
print(result1, result2, result3)    # python에서는 공백이 기본임. 공백을 여러개 주고 싶으면 , sep="\t" 추가
print(result1, result2, result3, sep="\t")

# 다항(삼항) 연산자 : (조건) and ~~ or ~~    -> 조건이 참인 경우 and 뒤가 수행, 조건이 거짓이면 or 뒤 수행
num = int(input("정수 입력 : "))
result = (num % 2 == 0) and "짝수" or "홀수"        # if 람다식 이용 : e => (e % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {result}입니다.")

# 이진수 입력받기 [0b] -> 0, 1 (binary)
number = 0b101010101
# 8진수 입력받기  [0o] -> 0,1,2,3,4,5,6,7 (octal)
number = 0o1234567
#16진수 입력받기  [0x] -> 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f (hexadecimal)
number = 0xffffff




