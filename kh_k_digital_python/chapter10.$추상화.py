# 추상화 : 부모 클래스에서 선언한 메소드에 대해서 반드시 상속 받은 클래스에서 기능을 구현 해야 하는 특성.
# 추상 메소드가 포함된 부모 클래스는 객체로 만들 수 없고 단지 상속을 주기 위해서만 존재.
# 상속은 부모도 실체가 있고 자식도 실체가 있는 반면, 추상화는 부모의 실체가 없음. 즉, 부모의 객체화가 발생할 수 없다.
from abc import *                            # abc : abstract package의 이름.
class NetworkAdapter(metaclass=ABCMeta):     # NetworkAdapter라는 추상 클래스 선언.
    @abstractmethod
    def connect(self):
        pass                                 # 추상 메소드는 구현부가 없어야 하므로 pass로 구현하지 않겠다를 명시해 줌.

class WiFi(NetworkAdapter):
    def __init__(self, company):             # 생성자 만들기.
        self.company = company
    def connect(self):                       # 부모로부터 상속 받은 추상 메소드 반드시 구현해야 함.
        print(f"{self.company} Wi-Fi에 연결하였습니다.")

class FiveG(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} 5G에 연결하였습니다.")

network = input("연결할 네트워크 선택 [1]WiFi [2]5G : ")
if network == "1":
    adapter = WiFi("KT MegaPass")
    adapter.connect()
elif network == "2":
    adapter = FiveG("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")
