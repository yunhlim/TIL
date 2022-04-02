a, b = map(int, input().split())
total = a ** 2 + b ** 2
print(a/(total ** (1/2)), b/(total ** (1/2)))