# [Programmers] Lv 2. 양궁대회 [2022 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [양궁대회](https://school.programmers.co.kr/learn/courses/30/lessons/92342)

## 📖 풀이

여러 실수가 겹쳐 오랫동안 헤맸던 문제이다.

**조합**으로 해결할 수 있다.

라이언이 각 점수에서 이기는 경우와 0점인 경우로 나눈다.

- 어피치가 3점이면 라이언은 4점인 경우와 0점인 경우로 나누는 것이다.

재귀를 활용해 조합을 구현한다. 라이언의 점수표를 기록하기 위한 배열을 선언해 활용한다.

조합으로 매번 배열이 완성된 경우, 라이언이 최고 점수로 이겼는지 확인해 answer 배열을 갱신해준다. 이 때 값을 복사해서 넣어야한다.

그리고 기존의 최고 점수와 같은 경우는 0점 과녁을 맞춘 횟수부터 확인해, 가장 낮은 점수를 더 많이 맞힌 경우만 값을 갱신한다.

max_score가 0이 나오는 경우는 어피치가 이긴 것이므로 [-1]을 출력해야 한다.

## 📒 코드

```python
def solution(n, info):
    def recur(cur, score, n, arr):
        nonlocal max_score, answer
        if cur == 11:               # 끝난 경우
            if n:                   # n이 남아있으면 0점에 다 넣어준다.
                arr[10] += n
            if max_score < score:
                max_score = score
                answer = arr[:]
            elif max_score == score:        # 같으면 가장 낮은 점수를 더 많이 맞힌 경우로 변경
                for i in range(11)[::-1]:
                    if answer[i] < arr[i]:
                        answer = arr[:]
                        break
                    elif answer[i] > arr[i]:
                        break
            return

        # 안 쏜 경우
        if not info[cur]:   # 이기는 사람 없음
            recur(cur + 1, score, n, arr + [0])
        else:               # 어피치가 이김
            recur(cur + 1, score - 10 + cur, n, arr + [0])

        # 쏜 경우
        cnt = info[cur] + 1     # 라이언이 이길 최소 횟수
        if n >= cnt:              # 라이언이 이김
            recur(cur + 1, score + 10 - cur, n - cnt, arr + [cnt])

    max_score = 0
    answer = [0] * 11
    recur(0, 0, n, [])
    if not max_score:           # 라이언이 우승할 방법이 없는 경우
        return [-1]
    return answer
```

