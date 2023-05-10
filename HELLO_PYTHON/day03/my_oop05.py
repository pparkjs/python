class Biden:
    def __init__(self):
        print("생성자")
    def ira(self):
        print("ira")
    def __del__(self):
        print("소멸자") # 자바에서는 가비지 컬렉션이 알아서 메모리 차면 청소해줌
        
b = Biden()
b.ira()