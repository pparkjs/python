# 출력할 단수를 입력하시오 4
# 4*1=4 
# 4*2=8 

# 4*9=36 

num = int(input("출력할 단수를 입력하시오"))

for i in range(1, 9+1):
    print("{} * {} = {}".format(num, i, num*i))