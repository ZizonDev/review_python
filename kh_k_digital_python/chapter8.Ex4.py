# 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
# 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# 이미 예매가 완료된 좌석은 재구매할 수 없다.
# 한 좌석당 예매 가격은 12000원이다.
# 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

def print_seat(seat):
    for i in seat:
        if i == 0:
            print("[ ]", end=" ")
        else:
            print("[V]", end=" ")
    print()


def tot(seat):  # 매출계산함수
    count = 0
    for i in seat:
        if i == 1:
            count += 1
    return count * 12000


def select_seat(seat):  # 좌석 선택 함수
    print_seat(seat)
    index = int(input("좌석번호를 입력하세요: ")) - 1
    if seat[index] == 0:
        seat[index] = 1
    else:
        print("이미 예약된 좌석입니다")
    return seat


def run():
    total = 0  # 총 매출액
    seat = [0, 0, 0, 0, 0, 0, 0]
    while True:
        print("[1]예매하기")
        print("[2]종료하기")

        sel = int(input("메뉴를 선택하세요: "))
        if sel == 1:
            # 예매함수
            seat = select_seat(seat)
        else:
            # 가격출력하는 함수
            total = tot(seat)
            print("총 매출액 : {}원".format(total))
            break


run()