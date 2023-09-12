# 태양고 학생들이 시합을 나갑니다. 총 준비된 칼은 10자루 입니다.
# 시합을 참여 하는 학생 수를 입력 하여 남아 있는 칼이 얼마인지를 전역 변수와 지역 변수를 이용해 구현 합니다.
knife = 10
def game(player):
    global knife                            # 전역변수로 선언된 변수를 함수내에서 사용하고자 할 때는 global 키워드가 필요함.
    knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")

def game2(player, knife):
    knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")


player = int(input("경기에 참여하는 선수가 몇명 입니까? "))
# game(player)
game2(player, knife)