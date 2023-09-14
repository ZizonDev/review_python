# - 현재 시간 및 날짜 가져오는 내장 함수 사용
# - 전역 변수 사용
# - 함수의 리턴값 사용
# - 시리얼넘버란? 제품의 고유번호이며 유일한 값입니다. 형식 : "iPad+화면크기+네트워크+날짜+만든횟수"

from datetime import datetime

make_cnt = 0 #생산 댓수 확인용
def choice_pad():
    print("<< iPad Pro 구입하기 >>")
    print("[1]구입하기, [2]종료하기")
    sel = input("메뉴를 선택 하세요 : ")
    if sel == "1" : return sel
    else : return "2"
def select_screen():
    while True :
        print("[1]11인치, [2]12.9인치")
        sel = input("디스플레이를 선택 하세요 : ")
        if sel == "1" or sel == "2": return sel
def select_color():
    while True :
        print("[1]스페이스그레이, [2]실버")
        sel = input("컬러를 선택 하세요 : ")
        if sel == "1" or sel == "2": return sel
def select_memory():
    while True :
        print("[1]128GB, [2]256GB, [3]512GB, [4]1TB")
        sel = input("용량을 선택 하세요 : ")
        if sel == "1" or sel == "2" or sel == "3" or sel == "4": return sel
def select_network():
    while True:
        print("[1]Wi-Fi, [2]Wi-Fi+Cellular")
        sel = input("네트워크를 선택 하세요 : ")
        if sel == "1" or sel == "2": return sel
def select_name_service():
    print("[1]각인 서비스 신청, [2]신청 안함")
    sel = input("각인 서비스를 선택 하세요 : ")
    if sel == "1" : name = input("이름을 입력 하세요 : ")
    else : name = "NONE"
    return name
def make_ipad(screen, color, memory, network, name):
    global make_cnt
    make_cnt = make_cnt + 1
    print_screen = ("", "11인치", "12.9인치")
    print_color = ("", "스페이스그레이", "실버")
    print_memory = ("", "128", "256", "512", "1024")
    print_network = ("", "Wi-Fi", "Wi-Fi+Cellular")
    serial_screen = (screen == "1") and "11" or "13"
    serial_network = (network == "1") and "W" or "C"
    serial_date = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day)
    serial_number = "iPad"+serial_screen+serial_network+serial_date+str(make_cnt)
    print("iPad Pro가 출고 되었습니다.")
    print("="*34)
    print(f"화면 크기 : {print_screen[int(screen)]}")
    print(f"제품 색상 : {print_color[int(color)]}")
    print(f"제품 용량 : {print_memory[int(memory)]}GB")
    print(f"네트워크 : {print_network[int(network)]}")
    print(f"이름 : {name}")
    print(f"시리얼넘버 : {serial_number}")
    print("-"*34)


while True :
    is_conti = choice_pad()
    if is_conti == "1":
        sel_screen = select_screen()
    else :
        print("iPad Pro 구입을 종료 합니다.")
        break
    sel_color = select_color()
    sel_memory = select_memory()
    sel_network = select_network()
    name = select_name_service()
    make_ipad(sel_screen, sel_color, sel_memory, sel_network, name)