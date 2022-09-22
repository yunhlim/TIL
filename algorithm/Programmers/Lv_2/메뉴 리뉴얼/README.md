# [Programmers] Lv 2. 메뉴 리뉴얼 [2021 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

## 📖 풀이

문제가 복잡하고 잘못 생각해 오래 걸렸던 문제이다.

course 배열에 만들고 싶은 코스 요리의 개수가 들어간다.

각 손님 별로 먹은 메뉴 중 중복되는 조합을 확인해 코스 요리로 만들어줘야 한다.

따라서 각 손님을 순회하며 각각 course 배열의 개수만큼 조합을 활용해 딕셔너리에 `{메뉴: 개수}`로 담아준다.

두 손님 이상 같은 메뉴 조합을 꺼낸 경우는 개수를 + 1 해준다. 처음 나온 경우는 개수에 1을 넣어주면 된다.

각각의 개수별 코스 중 가장 많이 먹은 조합의 요리만 메뉴에 뽑아내야 한다.

개수가 많은 코스 요리가 여러 개인 경우는 다 뽑아낸다.

코스 요리를 다 뽑았으면 이제 정렬 후 출력하면 된다.

## 📒 코드

```python
def solution(orders, course):
    def recur(cur, menus):
        if len(menus) == length:
            arr[i][menus] = arr[i].get(menus, 0) + 1
            cnt_arr[i] = max(cnt_arr[i], arr[i][menus])
            return
        if cur == len(order):
            return
        recur(cur + 1, menus)
        recur(cur + 1, menus + order[cur])

    arr = [{} for _ in range(len(course))]
    cnt_arr = [0 for _ in range(len(course))]
    for i in range(len(arr)):
        for order in orders:
            order = sorted(order)
            length = course[i]
            recur(0, "")
    print(arr)

    ans = []
    for i in range(len(arr)):
        for key, value in arr[i].items():
            if value >= 2 and value == cnt_arr[i]:
                ans.append(key)
    ans.sort()
    return ans
```

