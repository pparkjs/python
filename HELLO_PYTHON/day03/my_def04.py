def add_min_mul_div_nam(a,b):
    return a+b,a-b,a*b,a/b,a%b

a,b,c,d,e = add_min_mul_div_nam(4,3)

print(a,b,c,d,e)

a = add_min_mul_div_nam(4,3)

# 튜플 ( 배열하고 비슷하지만 작은 배열처럼 쓴다 )
print(a)