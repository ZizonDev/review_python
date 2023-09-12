# 함수 : 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램 (여러 번의 호출로 반복되는 코드를 줄일 수 있음)
# 함수는 매개변수를 가질 수 있으며, 반환값을 가질 수 있습니다.
# 재사용 및 관리, 수정이 편리 합니다.
# 다른 개발자가 함수의 내부를 몰라도 입력과 출력만 알려 함께 개발을 진행 할 수 있는 장점이 있습니다.

# 매개변수는 넘겨주지만 리턴값이 없는 구조의 함수. (반복 호출)
def name_card(name, addr, phone) :
    print(f"주소 : {addr}")
    print(f"전화번호 : {phone}")
    print(f"이름 : {name}")
    print("-"*30)

name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
name_card("가을", "수원시 권선구 권선동", "010-1234-1111")

# 매개변수를 넘겨주고, 리턴값을 받는 구조의 함수.
# 계좌 개설
def open_acount(name):
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name

def deposit(balance, input):
    print(f"{input}입 입금 되었습니다. 잔액은 {balance + input}입니다.")
    return balance + input

def withdraw(balance, input):
    if balance >= input:
        print(f"출금 되었습니다. 잔액은 {balance - input}입니다.")
        return balance - input
    else:
        print(f"출금이 실패 했습니다. 잔액은 {balance}입니다.")
        return balance

balance = 0                         # 외부에서 선언된 변수 이지만 인수로 넘겨줘서 결과를 리턴 받음
name = open_acount("정경수")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}의 잔액은 {balance}입니다.")

# 순차 검색하는 함수
# 순차 검색과 이진 검색
### Python 순차 검색 횟수
def search_list(a, x):
    for i in range(0, len(a)):
        if x == a[i]: return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 33))
print(search_list(v, 18))
print(search_list(v, 900))

# 함수 선언 시 year, age, school에 기본값을 정의할 수 있다.
def profile(name, year = 2, age = 18, school = "태양고"):
    print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")

profile("나희도")
profile("고유림")
profile("백이진", None, 22)

# 가변 매개변수
# 함수의 매개 변수 앞에 *을 붙이면 lang에 몇 개를 입력하든 함수 내에서 튜플로 인식한다.
def profile(name, age, *lang) :
    print(f"이름 : {name}, 나이 : {age}", end= " ")
    for e in lang :
        print(e, end= " ")
    print()

profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
profile("조세호", 38, "Python", "Java", )
profile("유재석", 48, "Python", "Java", "C", "C++",)
