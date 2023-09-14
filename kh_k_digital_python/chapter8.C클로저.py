# 클로저 : 함수 안에 내부 함수(inner function)를 구현 하고 그 내부 함수를 반환하는 함수
# 이 때 외부 함수는 자신이 가진 변수값 등을 내부 함수에 전달하여 실행되도록 한다.
def calc() :
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

import time

def perform_operation(x, y, callback):
    result = 0
    for e in range(x) :
        result += e + x + y
        time.sleep(1)
    callback(result)  # 콜백 함수 호출

# 콜백 함수 정의
def callback_function(result):
    print(f"Operation result is: {result}")

# perform_operation 함수를 호출하면서 콜백 함수를 전달
perform_operation(10, 20, callback_function)