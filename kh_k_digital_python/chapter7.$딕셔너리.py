coffee_menu = {"Americano": 2500, "Espresso":2500, "Latte":4000, "Moca":4500}
tea_menu = {"Black tea": 4000, "Green tea": 4000, "Milk tea":3500}
food_menu = {"Cake":5000, "Bakery":6000, "Icecream":7000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["Americano"])         # 키로 값 확인하기.
print(coffee_menu.get("Americano"))     # get 함수로 값 확인하기.
for key in coffee_menu:                 # 딕셔너리 내부의 key가 'key'라는 키워드로 자동 할당됨.
    print(key, ":", coffee_menu[key])

dict = {"정경수":90, "고유림":88, "나희도":89}
dict.update({"정경수":77, "유재석":90})
print(dict)

dict1 = {"자바": 80, "PHP": 90, "HTML": 70}

print(dict1.keys())                     # 자바, PHP, HTML 출력.
print(dict1.values())                   # 80, 90, 70 출력.
print(dict1.items())                    # (key, value) 출력.

print('HTML' in dict1)                  # True
print('파이썬' in dict1)                 # False

print(dict1.get("파이썬"))               # None 출력 됨.

