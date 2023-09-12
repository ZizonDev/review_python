menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

while True :
    print("메뉴를 선택 하세요.")
    menu = input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : ")
    if menu == "1":
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력 하세요 : ")
        if rtrv_name in menu_dic:
            print(menu_dic[rtrv_name])
        else :
            print("찾는 메뉴가 없습니다.")
    elif menu == "3":
        add_name = input("추가 할 메뉴를 입력 하세요 : ")
        if add_name not in menu_dic:
            grp = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("제품 설명 : ")
            menu_dic[add_name] = [grp, price, desc]
        else:
            print("메뉴가 이미 존재 합니다.")
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == "4":
        del_name = input("삭제 할 메뉴를 입력 하세요 : ")
        if del_name in menu_dic :
            del menu_dic[del_name]
        else :
            print("삭제 할 메뉴가 없습니다.")
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == "5" :
        print("영업을 종료 합니다.")
        break