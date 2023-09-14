class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # + 연산에 사용되는 __add__ 오버라이딩. 객체끼리의 덧셈 연산 재정의.
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, other):           # * 연산에 사용되는 __mul__ 오버라이딩. 객체끼리의 곱셈 연산 재정의.
        return Vector2D((self.x * other.x)+100, (self.y * other.y)+100)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(100 * 200)            # python에 내장된 기본 정수 연산자 * 가 사용됨.
print(100.1 * 200.1)        # python에 내장된 기본 실수 연산자 사용.

v3 = v1 + v2
print(v3.x, v3.y)           # 4, 6이 출력됨. 위에서 오버라이딩한 __add__가 사용됨.
v4 = v1 * v2
print(v4.x, v4.y)           # 103, 108이 출력됨. 위에서 오버라이딩한 __mul__이 사용된 것임.