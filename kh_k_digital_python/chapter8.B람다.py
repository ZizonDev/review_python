 # 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현 한 것.
 # python에서는 lambda를 통해 이름이 없는 함수를 만들 수 있다.
def add(a, b):
    return a + b

print(add(1, 2))

print((lambda a, b: a+b)(1, 2))

def call_times(func):
    for i in range(10):
        func()

def print_hello():
    print("Hello^^")

call_times(print_hello)


def power(n):
    return n * n

square = lambda x: x * x  # 함수의 형태이지만 이름이 없다

input = [1,2,3,4,5]

output_a = list(map(square, input)) # 람다 함수를 직접 넣어도 됨
print(output_a)

# 리스트에 람다 합수를 넣는 것도 가능 합니다.
my_list = [lambda a, b : a * b, lambda a, b: a + b]
print(my_list[0](5,2))
print(my_list[1](5,2))

# 함수로 만들어서 map이나 filter의 인자로 넣는 방법
def odd(n) :
    return  n % 2 == 1
def even(n) :
    return  n % 2 == 0

# 람다를 변수로 받아 map이나 filter의 인자로 넣는 방법
lambda_add = lambda x: x % 2 == 1
lambda_even = lambda x: x % 2 == 0

print("입력 :", end=" ")
number = list(map(int, input().split())) # 여러개의 데이터를 입력 받아서 리스트 구성
odd = list(filter(lambda_add, number))
even = list(filter(even, number))

print(f"홀수 : {odd}")
print(f"짝수 : {even}")