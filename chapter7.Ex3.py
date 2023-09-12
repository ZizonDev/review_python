#중복 값 제거한 로또 번호 만들기
import random

numbers = set()
while True :
    number = random.randrange(1, 46)
    numbers.add(number)
    if len(numbers) == 6 : break;

print(numbers)