num = input()
units = [0]*10

for idx in num:
    for i in range(10):
        if int(idx) == i:
            units[i] += 1

print(*range(10))
print(*units)