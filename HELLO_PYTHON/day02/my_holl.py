# 홀/짝을 입력하시오 홍
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random

rnd = int(random()*10)
com = "";
if rnd >= 5:
    com = "홀"
else:
    com = "짝"
a = input("홀/짝을 입력하시오")
print("나 : " + a)
print("컴 : " + com)
result = ""
if a == com:
    result = "승리"
else:
    result = "패배"

print("결과 : " + result)