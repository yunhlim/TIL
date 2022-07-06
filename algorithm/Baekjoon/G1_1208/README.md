# [Baekjoon] 1208. 부분수열의 합 2 [G1]

## 📚 문제 : [부분수열의 합 2](https://www.acmicpc.net/problem/1208)

## 📖 풀이

부분수열 중 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하라는 문제이다.

부분수열이니 **조합**으로 구하면 된다.

2의 n제곱으로 조합으로 고르면 무조건 **시간초과**가 발생한다. 왜냐면 2의 40제곱은 1조보다 큰 수이다.

2의 20제곱은 100만 정도라 구할 수 있으므로 일단 둘로 나누어 각각 부분수열의 합을 구한다.

그리고 구한 부분수열의 합을 각각 정렬한 다음 **투포인터**로 원하는 수와 같은지 확인한다.

## 📒 코드

```python
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
```

## 🔍 결과

![image-20220706190053765](README.assets/image-20220706190053765.png)
