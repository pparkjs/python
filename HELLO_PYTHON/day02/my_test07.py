# 가위/바위/보를 선택하세요 가위
# 나:가위
# 컴:바위
# 결과:패배
from random import random

arr = ["가위", "바위", "보"]

my = input("가위/바위/보를 선택하세요")
com = int(random() * 3)
result = ""
if arr[com] == my:
    result = "비김"
elif my == "가위" and arr[com] == "보" or my == "바위" and arr[com] == "가위" or my == "보" and arr[com] == "바위":
    result = "승리"
else:
    result = "패배"

print("나 : " + my)
print("컴 : " + arr[com])
print("결과 : " + result)