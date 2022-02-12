numbers = []
for i in range(100,301):
    ones = i % 10
    tens = i % 100 //10
    hundreds = i // 100
    if (hundreds % 2 == 0) and (tens % 2 == 0) and (ones % 2 == 0):
        numbers.append(i)

print(*numbers, sep = ',')