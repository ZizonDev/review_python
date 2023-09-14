# Class Method : 클래스 변수를 사용하기 위한 함수.
# 클래스 메소드는 함수를 정의할 때 첫 번째 인자로 클래스를 넘겨받는 cls가 필요하며, 이를 이용해 클래스 변수에 접근한다.

class Person:
    count = 0                   # 클래스 변수
    def __init__(self):         # __로 시작하는 변수는 외부에서 접근할 수 없다. (private와 유사.)
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성되었습니다.")

james = Person()
maria = Person()

Person.print_count()

# 접근 제한자와 getter, setter
class TV:
    cnt = 0 # 클래스 맴버
    def __init__(self, name, isOn, channel, volume):
        self.__name = name              # __로 시작하는 변수는 외부에서 접근할 수 없다. (private와 유사.)
        self.__isOn = isOn              # 직접 접근해도 에러는 나지 않지만 값이 바뀌지는 않을 것이다.
        self.__channel = channel
        self.__volume = volume
        TV.cnt += 1
    def set_on(self, isOn):             # 그래서 바꾸려면 getter, setter 필요.
        self.__isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.__channel = cnl
        else :
            print("채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.__volume = vol
    def get_on(self):
        return self.__isOn
    def get_channel(self):
        return self.__channel
    def get_volume(self):
        return self.__volume
    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.__name}")
        print(f"전원 : {power[self.__isOn]}")
        print(f"채널 : {self.__channel}")
        print(f"볼륨 : {self.__volume}")

lg_tv = TV("LG", True, 10, 20)
sam_tv = TV("LG", True, 10, 20)
lg_tv.__name = "SAMSUNG"            # 변경 안 됨. because of __
lg_tv.__isOn = False                # 변경 안 됨. because of __
lg_tv.set_channel(999)
lg_tv.view_tv()
print(TV.cnt)
