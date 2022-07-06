def recur(cur, total, sub_set):     # 부분수열의 합을 담는다.
    if cur == right:
        sub_set[total] = sub_set.get(total, 0) + 1
        return

    recur(cur + 1, total, sub_set)
    recur(cur + 1, total + arr[cur], sub_set)
    

n, m = map(int, input().split())
arr = list(map(int, input().split()))
mid = n // 2

# 절반으로 나눠 왼쪽 부분수열의 합
left_dict = {}
left, right = 0, mid
recur(left, 0, left_dict)
left_lst = []
for key, cnt in left_dict.items():
    left_lst.append([key, cnt])

# 절반으로 나눠 오른쪽 부분수열의 합
right_dict = {}
left, right = mid, n
recur(left, 0, right_dict)
right_lst = []
for key, cnt in right_dict.items():
    right_lst.append([key, cnt])

left_lst.sort()
right_lst.sort()

cnt = 0
s, e = 0, len(right_lst) - 1
while s < len(left_lst) and e >= 0:
    if left_lst[s][0] + right_lst[e][0] > m:
        e -= 1
    elif left_lst[s][0] + right_lst[e][0] == m:
        cnt += left_lst[s][1] * right_lst[e][1]
        s += 1
    else:
        s += 1
if m == 0:      # 0이 답인 경우는 부분집합의 크기가 0인 걸 제외
    cnt -= 1
print(cnt)