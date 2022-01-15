scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0
index = 0
try:
    while True:
        under80s = 0
        index = 0

        while True:
            if scores[index] < 80:
                scores.pop(index)
                break
            else:
                index += 1
except IndexError:
    pass
index = 0
try:
    while True:
        total += scores[index]
        index += 1
except IndexError:
    pass
print(total)