# [Baekjoon] 2004. 조합 0의 개수 [S2]

## 📚 문제

https://www.acmicpc.net/problem/2004

---

0의 개수를 찾는 문제이다.

0의 개수는 10의 개수이니 2와 5로 나누어서 생각한다.

nCm은 `n! / (n-m)! * m!`로 나타낼 수 있다.

> n!에 곱해진 2의 개수 - (n-m)!에 곱해진 2의 개수 - (m)!에 곱해진 2의 개수
>
> n!에 곱해진 5의 개수 - (n-m)!에 곱해진 5의 개수 - (m)!에 곱해진 5의 개수

2의 개수와 5의 개수의 최소값을 출력하면 10의 개수이다.

m!에 곱해진 소수 k의 개수를 찾기 위해서는 k로 나누면서 생각할 수 있다.

m을 k로 나누는 연산을 반복해서 찾을 수 있다. m//k는 k의 개수이고 m//k//k는 k^2의 개수이다. 이를 반복하여 총 k가 몇개인지 찾는다.

## 📒 코드

```python
def f_cnt(num, k):  # num!에 곱해진 소수 k의 개수
    num //= k
    cnt = num
    while num >= k:
        num //= k
        cnt += num
    return cnt

n , m = map(int, input().split())
arr = [[n, n-m, m], [0, 0, 0], [0, 0, 0]]   # n, n-m, m 일 때 각 팩토리얼의 2의 개수와 5의 개수

for i in range(3):
    arr[1][i] = f_cnt(arr[0][i], 2)         # n, n-m, m의 2의 개수
    arr[2][i] = f_cnt(arr[0][i], 5)         # n, n-m, m의 5의 개수
two = arr[1][0] - arr[1][1] - arr[1][2]     # n의 2의 개수에서 나머지를 빼준다.
five = arr[2][0] - arr[2][1] - arr[2][2]    # n의 5의 개수에서 나머지를 빼준다.

print(min(two, five))       # 2와 5 중 최소의 개수를 출력
```

## 🔍 결과

![image-20220226183638078](README.assets/image-20220226183638078.png)