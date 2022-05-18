# [Baekjoon] 1107. 리모컨 [G5]

## 📚 문제 : [리모컨](https://www.acmicpc.net/problem/1107)

## 📖 풀이

1. 버튼을 눌러서 먼저 가장 가까운 채널로 이동해야 한다.(이동하지 않는 경우가 가장 가깝다면 이동하지 않는다. 시작위치는 100이다.)
2. 위나 아래 버튼을 눌러 이동한다.

결국 1번인 가장 가까운 번호를 찾는 것이 핵심이다.

이동할 숫자보다 크거나 같은 수 중 가장 작은 값과, 작거나 같은 수 중 가장 큰 값을 비교해 더 작은 이동 횟수를 출력하면 된다.

위 경우에서 숫자 번호를 누르지 않는 경우가 있다.

따라서 숫자 번호를 눌러서 이동하는 경우와 누르지 않고 +, - 버튼만 누르는 경우로 나눌 수 있다.

먼저 숫자 번호를 누르지 않는 경우의 누르는 버튼 횟수를 cnt에 입력한다.

그리고 이동하고 싶은 채널에서 +, - 방향으로 1씩 이동해가면서 누를 수 있는 번호가 있는지 찾는다.

이 때 -인 경우를 먼저 확인한다. 왜냐하면 +로 움직인 경우랑 -로 움직인 경우가 둘 다 되는 경우 채널의 길이가 -가 더 짧으면 -로 이동해야하기 때문에 - 방향으로 움직인 걸 확인한 후 + 방향도 확인한다.

채널이 + 방향으로는 한 없이 갈 수 있지만 - 채널은 없으므로 0보다 작아지는 경우는 - 방향을 보지 않는다.

그냥 +, - 버튼만 누르는 경우가 현재 이동한 후 +, - 버튼을 눌러야하는 횟수보다 작으면 숫자 버튼으로 이동하지 않은 횟수를 바로 출력한다.

## 📒 코드

```python
n = int(input())
m = int(input())
arr = set(input().split()) if m else set()
move = 0
cnt = abs(n - 100)          # 숫자버튼을 이용하지 않는 경우 눌러야하는 횟수
while True:
    if cnt < move:          # 숫자버튼을 이용한 경우가 절대로 답이 될 수 없을 때
        break
    # 이동하고 싶은 채널에서 거리를 1씩 늘려가며 확인한다.
    if n - move >= 0 and not set(str(n - move)) & arr:  
        # - 방향 채널의 길이가 + 방향의 채널의 길이보다 작을 수 있다.
        # 0보다 작아지진 않는다.
        cnt = len(str(n - move)) + move             # 채널의 번호를 누르고 이동하는 경우
        break
    elif not set(str(n + move)) & arr:
        cnt = len(str(n + move)) + move
        break
    move += 1       # 거리를 +1

print(cnt)
```

## 🔍 결과

![image-20220518164929567](README.assets/image-20220518164929567.png)