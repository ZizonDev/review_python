# 다중 상속 : 여러 부모로 부터 상속을 받는 것.
# 인간으로부터 상속 받아 직장인과 학생을 생성한다.
# 개발자는 공부, 일 모두 하는 특성이 있으므로 학생과 직장인으로부터 상속 받는다. (개발자는 인간인 동시에 학생, 직장인 특성도 갖는 다중 상속 받음.)
# 파이썬에서는 생성자에서 상속의 모호성을 허용하지 않으므로 문제가 발생하지 않는다.

class Person:
    def __init__(self, eat):
        self.eat = eat
        print("인간입니다.")
    def set_eat(self):
        print(f"{self.eat} 식사를 합니다.")

class Student(Person):
    def __init__(self, eat, study):
        Person.__init__(self, eat)
        self.study = study
        print("학생입니다.")
    def set_study(self, study):
        self.study = study
        print("공부를 합니다.")
class Worker(Person):
    def __init__(self, eat, work):
        Person.__init__(self, eat)
        self.work = work
        print("직장인입니다.")
    def set_work(self, work):
        self.work = work
        print("일을 합니다.")
class Developer(Student, Worker):
    def __init__(self, eat, study, work):
        Student.__init__(self, eat, study)
        Worker.__init__(self, eat, work)
        print("개발자입니다.")

dev = Developer(1, 1, 1)
dev.eat = "점심"
dev.set_eat()
dev.set_study(1)
dev.set_work(1)