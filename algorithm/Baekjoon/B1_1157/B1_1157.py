message = input()
dic = {}
for c in message:
    if c >= 'a':
        c = chr(ord(c) - ord('a') + ord('A'))
    dic[c] = dic.get(c, 0) + 1

arr = []
for k, v in dic.items():
    arr.append([v, k])

arr.sort(reverse=True)

if len(arr) > 1 and arr[0][0] == arr[1][0]:
    print("?")
else:
    print(arr[0][1])
