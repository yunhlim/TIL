# [SWEA] 1859. 백만 장자 프로젝트 [D2]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=1859&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

처음에 풀어보았던 풀이는 리스트에서 맨 앞에 껄 하나씩 꺼내서 남아있는 리스트와 비교해 더 큰 값이 리스트 안에 존재한다면 물건을 사고 현재 값이 가장 클 경우에는 가지고 있는 물건을 다 파는 식으로 코드를 작성했다.

## 📒 1차 코드

```python
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    p_arr = list(map(int, input().split())) # 날짜별 가격을 담은 배열
    coin = 0    # 이익
    cnt = 0     # 산 개수
    for i in range(N):  # 날짜가 지날 때마다 돈다.
        np = p_arr[0]   # 오늘 가격
        del p_arr[0]    # 배열에서 오늘 가격을 제외
        for p in p_arr:
            if np < p:
                coin -= np
                cnt += 1
                break
        else:
            coin += np * cnt
            cnt = 0
    print(f'#{tc} {coin}')
```

## 🔍 결과 : 시간 초과

테스트 입력을 돌려보니 시간초과가 난다. 현재 배열의 길이가 100만으로 주어져 이걸 계속 확인하면 O(n<sup>2</sup>)이니 

100만 X 100만으로 => 약 1조 번의 연산량이 필요하다.  엄청난 많은 수의 연산량이 필요해 시간이 부족해질 수 밖에 없다. 따라서 다른 방법을 생각해보았다.

---

표로 적어서 한 번 확인해본다.

|      |  1   |  1   |  4   |  1   |  3   |  1   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 판매 |  4   |  4   |  4   |  3   |  3   |  1   |
| 차익 |  3   |  3   |  0   |  2   |  0   |  0   |

다음과 같이 작성할 수 있다. 최대값인 경우 그 값도 판다고 생각하자, 그러면 차익은 0이니 안 파는거나 다름없다.

그러면 뒤에서부터 MAX 값을 구해서 현재의 가격과 차이를 새로운 변수에 계속 더해주면 된다.

## 📒 최종 코드

```python
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    p_arr = list(map(int, input().split())) # 날짜별 가격을 담은 배열
    p_max = 0   # 가격의 최댓값
    coin = 0 # 이익
    for i in range(N-1, -1, -1):    # 뒤에서부터 최대값을 찾아 현재 값과 차이를 담아준다.
        if p_max < p_arr[i]:    # 최댓값이 나오면 업데이트해주고 차이는 0으로 적어준다.
            p_max = p_arr[i]
        else: coin += p_max - p_arr[i]
    print(f'#{tc} {coin}')
```

## 🔍 결과 : Pass