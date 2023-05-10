# 첫수를 입력하세요 1
# 끝수를 입력하세요 10
# 배수를 입력하시오 5
# 1에서 10까지의 5의 배수의 합은 15입니다.

first = int(input("첫수를 입력하세요"))
end = int(input("끝수를 입력하세요"))
mul = int(input("배수를 입력하세요"))
sum = 0;
for i in range(first, end+1):
    if i % mul == 0:
        sum += i

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다".format(first, end, mul, sum))

