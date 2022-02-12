# [SWEA] 1208. [S/W 문제해결 기본] 1일차 - Flatten [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=Flatten&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

가로길이가 총 100이니 상자가 세워지는 공간이 100인 리스트를 만든다.

상자 리스트에 상자를 다 담아주고 상자를 옮겨주는 덤프 작업을 시작한다.

가장 높은 곳에서 가장 낮은 곳으로 옮겨주려면 max와 min 값을 찾는다.

여기서 같은 최댓값이 여러 개 나오면 가장 앞에 나오는 걸 선택하게 작성하는데 사실 필요 없다.

그렇지만 문제 요구사항에 있으므로 그렇게 작성한다.

상자가 제일 높은 곳과 낮은 곳을 찾았으면 평탄화 작업을 진행한다.

가장 높은 곳은 1을 빼고 가장 낮은 곳은 1을 더한다.

max와 min의 차이가 0 or 1이 되면 평탄화가 완료된다고 하니 최대, 최소의 차이가 2미만일 때 반복문을 그만두는 조건을 평탄화 하기 전에 추가한다.

## 📒 코드

```python
T = 10
for tc in range(1, T+1):
    N = int(input())    # 덤프 횟수
    box_cnt_lst = list(map(int, input().split()))   # 박수 개수 담은 list
    for _ in range(N):
        max_cnt = box_cnt_lst[0]  # 최대 상자 수
        min_cnt = box_cnt_lst[0]  # 최소 상자 수
        max_idx = 0  # 최대 상자가 있는 인덱스의 값
        min_idx = 0  # 최소 상자가 있는 인덱스의 값
        for i in range(100):
            if max_cnt < box_cnt_lst[i]:
                max_idx = i
                max_cnt = box_cnt_lst[i]
            elif min_cnt > box_cnt_lst[i]:
                min_idx = i
                min_cnt = box_cnt_lst[i]
        if max_cnt - min_cnt < 2:
            break
        box_cnt_lst[max_idx] -= 1
        box_cnt_lst[min_idx] += 1
    print(f'#{tc} {max_cnt - min_cnt}')
```

## 🔍 결과: **Fail**

10개의 케이스 중 하나가 오답이다..

---

중간에 평탄화가 완료되면 평탄화 하기 위한 작업을 하지 않기 때문에 상관없지만, 평탄화가 끝나고 최대 최소가 바뀔 수 있으니 평탄화가 끝난 후 최대 최소를 구하는 작업을 넣어준다.

중간에 끝나면 안해도 되니 `for else:` 구문에 넣는다.

## 📒 코드

```python
T = 10

for tc in range(1, T+1):
    N = int(input())    # 덤프 횟수
    box_cnt_lst = list(map(int, input().split()))   # 박수 개수 담은 list
    for _ in range(N):    # 평탄화 작업 + min, max 작업
        max_cnt = box_cnt_lst[0]  # 최대 상자 수
        min_cnt = box_cnt_lst[0]  # 최소 상자 수
        max_idx = 0  # 최대 상자가 있는 인덱스의 값
        min_idx = 0  # 최소 상자가 있는 인덱스의 값

        for i in range(100):    # min, max 찾고, 평탄화 작업
            if max_cnt < box_cnt_lst[i]:    # max 찾기
                max_idx = i                 # max 상자의 인덱스 값  저장
                max_cnt = box_cnt_lst[i]    # max 상자의 개수 저장
            elif min_cnt > box_cnt_lst[i]:  # min 찾기, max와 동일
                min_idx = i
                min_cnt = box_cnt_lst[i]

        if max_cnt - min_cnt < 2:   # min, max 차이가 2 이하면 평탄화 작업 중단
            break

        box_cnt_lst[max_idx] -= 1   # 평탄화 작업
        box_cnt_lst[min_idx] += 1
    else:   # 평탄화 작업을 하고 마무리 됐으니 마지막에 최대 최소를 한번 더 구한다.
        max_cnt = box_cnt_lst[0]    # 최대 최소만 구하는 작업
        min_cnt = box_cnt_lst[0]
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if max_cnt < box_cnt_lst[i]:
                max_idx = i
                max_cnt = box_cnt_lst[i]
            elif min_cnt > box_cnt_lst[i]:
                min_idx = i
                min_cnt = box_cnt_lst[i]

    print(f'#{tc} {max_cnt - min_cnt}')
```

## 🔍 결과 : **Pass**