n = int(input())
m = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(m):
    pick = arr[i]
    for j in range(len(result)):
        if result[j][1] == pick:
            result[j][0] += 1
            break
    else: 
        if len(result) == n:
            mmin = sorted(result)[0][0]
            for j in range(len(result)):
                if mmin == result[j][0]:
                    result.pop(j)
                    result.append([1, pick])
                    break
        else:
            result.append([1, pick])

result = list(map(lambda x: x[1], result))
print(*sorted(result))