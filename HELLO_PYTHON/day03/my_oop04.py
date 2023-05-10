class LeeJY:
    def __init__(self):
        self.cnt_company=20
        
    def seat(self):
        self.cnt_company+=1

class Bin:
    def __init__(self):
        self.amount_oil = 10000
        
    def dig(self):
        self.amount_oil *= 2

class KimJeungUn:
    def __init__(self):
        self.cnt_nuclear = 30
    def aoji(self):
        self.cnt_nuclear += 2
    
    # 다중상속
class KimJiWan(LeeJY, Bin, KimJeungUn):
    
    # 다중 상속해서 여러 클래스의 메소드 가져올려면 생성자에서 각 클래스 생성자를 호출
    def __init__(self):
        LeeJY.__init__(self)
        Bin.__init__(self)
        KimJeungUn.__init__(self)
        
kjw = KimJiWan()    
print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)
kjw.seat()
kjw.dig()
kjw.aoji()
print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)

    