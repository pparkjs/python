class Animal:
    
    def __init__(self):
        self.age = 1
    
    def birthHappy(self):
        self.age += 1

# 자바의 main 역할로 이렇게 하면 import 한곳에서 이거 실행 안됨
if __name__ == '__main__':
    ani = Animal()
    print(ani.age)
    ani.birthHappy()       
    print(ani.age)