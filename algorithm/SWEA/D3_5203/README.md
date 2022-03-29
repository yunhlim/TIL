# [SWEA] 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT

---

## 📖 풀이

플레이어 1과 플레이어 2 각각 입력받은 숫자를 담을 카운팅 배열을 선언한다.

값이 들어오면 카운팅 배열의 값이 3이 되면 triplet이니 결과를 출력하고, 3이 아니고 3개 이상 들어온 경우 run이 되는지 체크한다.

run_check 함수를 만들어서 현재 입력받은 값 기준으로 run이 되는지 확인한다.

## 📒 코드

```python
def run_check(x, arr):  # run 체크
    if 0 < x < 9:
        if arr[x - 1] and arr[x + 1]:
            return True
    if 0 <= x < 8:
        if arr[x + 1] and arr[x + 2]:
            return True
    if 1 < x <= 9:
        if arr[x - 1] and arr[x - 2]:
            return True
    return False


t = int(input())
for tc in range(1, 1 + t):
    arr = list(map(int, input().split()))
    player = [[0 for _ in range(10)] for _ in range(2)]
    result = 0
    for i in range(12):
        p = i % 2       # 플레이어 선택
        player[p][arr[i]] += 1
        if player[p][arr[i]] == 3:  # triplet 체크
            result = p + 1
            break
        if i >= 5:      # 3개 이상 들어온 경우
            if run_check(arr[i], player[p]):    # run 체크
                result = p + 1
                break
    print(f'#{tc} {result}')
```

## 🔍 결과

![image-20220329151654345](README.assets/image-20220329151654345.png)

처음에 카운팅 배열을 사용하지 않고, 입력받은 값을 리스트로 저장 후 run을 확인하는 방법을 사용하니 자꾸 Fail이 떴다.

보니까 같은 값이 여러 개 들어오는 경우, run 처리를 잘못해줘 틀렸던 것이다. 따라서 run 처리하기 쉽게 카운팅 배열을 사용해 해결했다.