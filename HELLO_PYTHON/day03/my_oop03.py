from day03.my_oop01 import Animal

class Human(Animal):
    def __init__(self):
        # super().__init__()이라는 코드가 다른 클래스의 속성 및 메소드를
        # 자동으로 불러와 해당 클래스에서도 사용이 가능하도록 해줍니다.
        super().__init__()
        self.tools = ["반지"]
        
    def farming(self, tool):
        self.tools.append(tool)
        
    def __str__(self):
        ret = str(self.tools)
        return ret
        
hum = Human()
print(hum.age)
print(hum)
hum.birthHappy()
hum.farming("돌도끼")
print(hum.age)
print(hum)