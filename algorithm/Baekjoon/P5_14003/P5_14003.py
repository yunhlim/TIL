def binary_search(x):   # 매개변수 탐색(이진 탐색)
    s, e = 0, len(lis) - 1
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        if lis[mid] == x:   # 같은 수가 있다면 return
            return mid
        elif lis[mid] > x:  # 큰 수 중 가장 작은 수를 매개변수 탐색
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]  # 시작부분을 넣어준다.
rnk = [0 for _ in range(n)] # arr의 각 수의 lis에서의 순서를 담아준다.
for i in range(1, n):
    num = arr[i]
    if lis[-1] < num:       # lis 값들보다 크면 맨 오른쪽에 삽입
        lis.append(num)
        rnk[i] = len(lis) - 1   # lis에서의 순서를 담아준다.
    elif lis[-1] > num:     # lis의 가장 큰 수보다 작으면 크거나 같은 값들 중 가장 작은 수와 바꾼다.
        index = binary_search(num)
        lis[index] = num
        rnk[i] = index          # index의 위치를 담아준다.
    else:
        rnk[i] = len(lis) - 1   # 같은 경우는 순서가 맨 뒤 값이랑 동일

prv = len(lis) - 1
result = []
for i in range(n)[::-1]:    # rnk를 거꾸로 세며 역순으로 값을 담는다.
    if rnk[i] == prv:
        result.append(arr[i])
        prv -= 1
        if prv < 0:         # 다 담았으면 종료한다.
            break

print(len(result))          # 길이를 출력
print(*result[::-1])        # 역순으로 담은 result를 다시 뒤집고 출력한다.