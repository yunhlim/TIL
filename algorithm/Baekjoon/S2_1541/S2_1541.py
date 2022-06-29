string = input()
num = ''
result = 0
minus = 0
for c in string:
    if c in '-+':
        if minus:
            result -= int(num)
        else:
            result += int(num)
        num = ''
    else:
        num += c
    if c == '-':
        minus = 1
else:
    if minus:
        result -= int(num)
    else:
        result += int(num)
print(result)