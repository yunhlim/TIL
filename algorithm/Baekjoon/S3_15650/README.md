# [Baekjoon] N과 M (2) [S3]

## 📚 문제

https://www.acmicpc.net/problem/15650

---

## 📖 풀이

오름차순으로 중복없는 순열이니 조합 문제이다.

재귀를 활용해 쉽게 해결한다.

배열에 담아 출력시킨다.

## 📒 코드

```python
def recur(cur, cnt):
    if cnt == m:
        print(*arr)
        return
    elif cur == n:
        return

    arr[cnt] = cur + 1
    recur(cur + 1, cnt + 1)   
    recur(cur + 1, cnt)
    

n, m = map(int, input().split())
arr = [0 for _ in range(m)]

recur(0, 0)
```

## 🔍 결과

![image-20220318171952204](README.assets/image-20220318171952204.png)