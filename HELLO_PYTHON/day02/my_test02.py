# 첫수를 입력하시오 5
# 끝수를 입력하시오 7
# 5에서 7까지 합은 18 입니다.

first = int(input("첫수를 입력하시오"))
end = int(input("끝수를 입력하시오"))
sum = 0

for i in range(first, end+1):
    sum += i
print("{}에서 {}까지 합은 {}입니다.".format(first, end, sum))
