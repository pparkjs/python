
for i in (9, 7, 3, 2):
        print("{} 단".format(i))
        for j in range(1, 9+1):
            if j == 5:
                continue
            print("{} * {} = {}".format(i,j,i*j))
        print("-----------\n")
    


# 이중 for문은 왠만해서 쓰지 말라 메소드로 이용해서 해라
def showdan(dan):
    print("{}*{}={}".format(dan,1,dan*1))
    print("{}*{}={}".format(dan,2,dan*2))
    print("{}*{}={}".format(dan,3,dan*3))
    print("{}*{}={}".format(dan,4,dan*4))
    print("{}*{}={}".format(dan,5,dan*5))
    print("{}*{}={}".format(dan,6,dan*6))
    print("{}*{}={}".format(dan,7,dan*7))
    print("{}*{}={}".format(dan,8,dan*8))
    print("{}*{}={}".format(dan,9,dan*9))

showdan(9)
showdan(7)
showdan(3)
showdan(2)