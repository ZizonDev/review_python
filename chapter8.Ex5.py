# 함수로 입력 받은 수가 짝수 인지 홀수 인지 결과 출력하기.
def check_even_odd(n) :
    if n % 2 == 0 :
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")

n = int(input("정수 입력 : "))
check_even_odd(n)