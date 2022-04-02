def f(a, b):
    return a ** 3 + a * a * b + a * b * b + b ** 3


n = int(input())
s = 0
e = 10 ** 6

min_result = 100000000000000000000
while s <= e:
    result = f(s, e)
    if result >= n:
        min_result = min(min_result, result)
        e -= 1
    else:
        s += 1

print(min_result)