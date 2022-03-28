# [Algorithm] 재귀 응용(순열, 중복없는 순열, 조합)

재귀를 활용하는 기본적인 3가지 예시이다.

기본 템플릿으로 외워둬야 한다!

나중에 백트래킹을 할 때에도 기본 베이스에서 응용하여 활용한다.

---

## 📌 순열(중복있는 순열)

재귀를 활용한 대표적인 예시로 순열이 있다.

`nPm`으로 표현한다.

반복문을 활용해 순열을 표현할 때는 n개의 순열은 n개의 for문을 중첩해서 활용해야 한다.

5자리의 순열을 반복문으로 표현하려면 for문은 5중 for문을 활용해야 한다.

### 📒 반복문 코드

```python
'''
5자리 2진수를 전부 나타내는 코드
'''
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    print(str(i) + str(j) + str(k) + str(l) + str(m))
```

이러한 반복문을 재귀함수로 간단하게 표현할 수 있다.

### 📒 순열 재귀 코드

```python
def recur(cur):
    if cur == 5:
        print(''.join(map(str,result)))
        return
    for i in range(2):
        result[cur] = i
        recur(cur + 1)


result = [0, 0, 0, 0, 0]
recur(0)
```

순열의 기본 뼈대를 구성하는 형식으로 재귀의 호출 횟수가 원하는 수면 끝내고 아니면 재귀를 다음 횟수로 진행하는 방법이다.

---

## 📌 중복없는 순열

중복없는 순열은 순열과의 차이가 이전 값을 기억해 중복된 값을 제거해야 한다.

visited 배열을 선언해 중복된 값을 확인하며 재귀 호출한다.

중복없는 0, 1, 2, 3, 4로 구성된 5자리 수를 출력해본다.

### 📒 중복없는 순열 코드

```python
def recur(cur):
    if cur == 5:
        print(*result)
        return
    for i in range(5):
        if visited[i]:
            continue
        visited[i] = 1
        result[cur] = i
        recur(cur + 1)
        visited[i] = 0


result = [0, 0, 0, 0, 0]
visited = [0, 0, 0, 0, 0]
recur(0)
```

중복있는 순열과 차이는 visited로 방문 여부를 체크하는 것이다.

이 때 중요한 점은 recur()를 거친 후 visited를 초기화 시켜줘야 한다.

왜냐하면 계속호출하며 여러 순열을 출력해야하는데, visited에 1로 바꿔준 후 다시 0으로 바꿔주지 않으면 다른 순열을 구할 때 영향을 미친다.

따라서 현재 바꿔주는 값이 이후로 영향을 미치는 경우에 재귀호출 앞 뒤로 visited를 바꿔준 후 초기화하는 걸 생각해야 한다.

---

## 📌 조합

조합은 중복된 케이스를 보지 않는 집합 연산자를 생각하면 쉽다.

`nCm`을 생각하면 된다.

조합은 2가지 방법으로 표현할 수 있다.

첫번째 방법은 재귀함수 안의 반복문의 시작점을 바꿔주는 것이다.

무조건 순서가 작은 순부터 중복없는 순열로 뽑으면 된다.

즉, 순서를 임의로 만들어 뽑으면 중복되는 경우가 없어진다.

0~4 중 3개를 뽑아 만들 수 있는 조합의 수를 찾아보자!

### 📒 조합1 코드

```python
def recur(cur, start):
    if cur == 3:
        print(*result)
        return
    for i in range(start, 5):
        result[cur] = i
        recur(cur + 1, i + 1)


result = [0, 0, 0]
recur(0, 0)
```

다음과 같이 시작점을 기억해두고, 시작점 이상부터 골라주면 된다.

어차피 순서대로 뽑으니 중복된 경우가 나올 수가 없다.



### 🍗 조합을 나타내는 2번째 방법이 더 중요하다.

첫번째부터 뽑을 수 있는지 없는지 2가지로 나타낼 수 있다.

따라서 선택, 미선택으로 다음 재귀를 호출한다.

여기서는 0~4 중 0, 1, 2, 3, 4 각각을 뽑고 안 뽑고로 생각하여 호출한다.

### 📒 조합2 코드

```python
def recur(cur, cnt):
    global result
    if cur == 5:
        if cnt == 3:
            print(*result)
        return
    result.add(cur)
    recur(cur + 1, cnt + 1)
    result.remove(cur)
    recur(cur + 1, cnt)


result = set()
recur(0, 0)
```

각각 뽑고 안 뽑고를 생각하여 넣어줄 수 있다.

조합을 해결할 때 자주 활용하게되는 템플릿이다.