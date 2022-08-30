t = int(input())
for _ in range(t):
    n = int(input())
    arr_a = list(input().split())
    arr_b = list(input().split())
    arr_c = list(input().split())
    dic = {}
    score = [0, 0, 0]
    for x in arr_a:
        dic[x] = dic.get(x, 0) + 1
    for x in arr_b:
        dic[x] = dic.get(x, 0) + 1
    for x in arr_c:
        dic[x] = dic.get(x, 0) + 1

    for x in arr_a:
        if dic[x] == 1:
            score[0] += 3
        elif dic[x] == 2:
            score[0] += 1
    for x in arr_b:
        if dic[x] == 1:
            score[1] += 3
        elif dic[x] == 2:
            score[1] += 1
    for x in arr_c:
        if dic[x] == 1:
            score[2] += 3
        elif dic[x] == 2:
            score[2] += 1

    print(*score)
