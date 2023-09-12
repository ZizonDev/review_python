# terminal에서 pip install simple-colors 입력 후 진행.
from simple_colors import *  # 화면 출력에 컬러 넣기.
import threading             # thread 기능을 위해 import.
import time                  # sleep을 걸기 위해 import.
import random                # 데미지를 random하게 발생시키기 위해 import.

class Unit:                  # 생성할 캐릭터의 부모 클래스.
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp     # physical power
        self.mPower = mp     # magical power
        self.pHit = ph       # 물리 적중률
        self.mHit = mh       # 마법 적중률
        self.hp = hp
        self.isAlive = True

class Character(Unit):       # Unit을 상속 받아 Character 클래스 생성.
    def __init__(self, pp, mp, ph, mh, hp, um, job):
        Unit.__init__(self, pp, mp, ph, mh, hp)     # 부모의 생성자 호출.
        self.ultimate = um                          # 궁극기(ultimate) 특성 추가.(오버라이딩)
        self.job = job                              # 직업 특성 추가.(오버라이딩)
    def p_attack(self):
        return self.pPower * self.pHit
    def m_attack(self):
        return self.mPower * self.mHit
    def attack_ultra(self):
        return self.ultimate
    def is_alive(self):
        return self.isAlive
    def set_damage(self, damage):
        if self.hp > damage:
            self.hp -= damage
            print(f"남아 있는 {green(self.job)}의 체력은 {blue(self.hp)} 입니다.")
            self.isAlive = True
        else:
            print(f"{green(self.job)}가 죽었습니다. 게임을 종료 합니다.")
            self.isAlive = False

# thread에서 실행할 함수
def wizard_th(dummy):
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    while True:
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False:
            break
        val = random.randrange(0, 2)
        ul = random.randrange(0, 18)
        if val == 0:
            print(f"{blue('물리공격')} >> {warrior.job}에게 {yellow(wizard.p_attack())} 데미지를 입혔습니다.")
            warrior.set_damage(wizard.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {warrior.job}에게 {yellow(wizard.m_attack())} 데미지를 입혔습니다.")
            warrior.set_damage(wizard.m_attack())
        if ul == 1:
            print(f"{red('궁극기 발동')} >> {warrior.job}에게 {red(wizard.attack_ultra())} 데미지를 입혔습니다.")
            warrior.set_damage(wizard.attack_ultra())

# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점

    name1 = input("전사는 강력한 체력의 물리 공격형 캐릭터 (이름 입력) : ")
    name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) :  ")

    warrior = Character(8, 2, 0.8, 0.5, 150, 40, name1)  # 물공, 마공, 물적, 마적, 체력, 궁극기
    wizard = Character(2, 20, 0.5, 0.9, 60, 55, name2)  # 물공, 마공, 물적, 마적, 체력, 궁극기
    x = threading.Thread(target=wizard_th, args=(1,))
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    x.start()  # sub thread 시작 (main과 sub_thread가 동시에 돌아가는 상황.)
    while True:
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False:
            break
        val = random.randrange(0, 2)    # 물리 공격이거나 마법 공격인 경우.
        ul = random.randrange(0, 12)    # 궁극기 데미지를 랜덤하게 발생시킴.
        if val == 0:
            print(f"{blue('물리공격')} >> {wizard.job}에게 {warrior.p_attack()} 데미지를 입혔습니다.")
            wizard.set_damage(warrior.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {wizard.job}에게 {warrior.m_attack()} 데미지를 입혔습니다.")
            wizard.set_damage(warrior.m_attack())
        if ul == 1:
            print(f"{red('궁극기 발동')} >> {wizard.job}에게 {red(warrior.attack_ultra())} 데미지를 입혔습니다.")
            wizard.set_damage(warrior.attack_ultra())
