from random import random
def getHollJJak():
    rnd = random()
    ret = ""
    if rnd > 0.5: 
        ret = "홀"
    else:
        ret = "짝"
    return ret

com = getHollJJak()
print(com)
