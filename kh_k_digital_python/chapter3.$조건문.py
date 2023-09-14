# 제어문 : 조건문과 반복문을 의미. 순차적인 흐름을 제어하는 목적으로 사용된다.
# python은 switch문이 없고, 조건 뒤 수행문을 쓸 때 콜론을 쓴다. 또한 중간에 else if를 elif로 표기한다.
# python에서는 조건에 따른 수행문의 들여쓰기가 꼭 맞아야 한다. 다만 수행문이 한줄이면 조건의 콜론 뒤에 바로 붙여쓰는 것 정도는 허용함.
n = int(input("정수를 입력하세요 : "))
if n > 100:
    print(f"{n}은 100보다 큰 수입니다.")
elif n < 100:
    print(f"{n}은 100보다 작은 수입니다.")
else:
    print(f"{n}은 100입니다!!!")

# 조건문에서 문자열 비교하기
season = input("현재 계절을 입력하세요 : ")
if season == "spring":
    print(f"{season}은 봄입니다.")
elif season == "summer":
    print(f"{season}은 여름입니다.")
elif season == "fall" or season == "autumn":
    print(f"{season}은 가을입니다.")
elif season == "winter":
    print(f"{season}은 겨울입니다.")
else:
    pass

while True:         # True 대신 1이나 -1을 넣어도 참으로 인지한다. python은 0, "", None만 거짓으로 잡기 때문.
    season = input("현재 계절을 입력하세요 : ")
    if season == "spring":
        print(f"{season}은 봄입니다.")
        break
    elif season == "summer":
        print(f"{season}은 여름입니다.")
        break
    elif season == "fall" or season == "autumn":
        print(f"{season}은 가을입니다.")
        break
    elif season == "winter":
        print(f"{season}은 겨울입니다.")
        break
    else:
        print("계절을 잘못 입력하셨습니다.")

