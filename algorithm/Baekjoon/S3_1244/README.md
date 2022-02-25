# [Baekjoon] 1244. 스위치 켜고 끄기 [S3]

## 📚 문제

https://www.acmicpc.net/problem/1244

---

남자와 여자 두가지를 함수로 나눠서 작성한다.

남자인 경우는 입력받은 번호의 배수들을 전부 스위칭한다.

여자는 입력받은 수를 중심으로 좌우 대칭으로 같을 때 영역을 넓혀가며 스위칭한다.

좌우 대칭으로 같은게 없으면 입력받은 수만 스위칭한다.

스위칭 할 땐 `1 ^ num` xor 연산자를 활용해서 바꿔준다.

마지막에 출력할 때 20개씩 잘라서 출력해야한다.

따라서 배열을 하나 새로 만들고 거기다가 20개씩 담아 출력하고,

마지막에 나머지를 출력시키고 종료한다.

## 📒 코드

```python
N = int(input())    # 스위치 개수
arr = [0] + list(map(int, input().split()))     # 스위치 상태 받아오기, padding으로 1번부터

def man(num):   # 남자는 배수 바꾸기
    for i in range(num, N + 1):
        if i % num == 0:            # 배수인지 확인
            arr[i] = 1 ^ arr[i]     # 바꿔준다.

def woman(num): # 여자는 대칭인 만큼 바꾸기
    arr[num] = 1 ^ arr[num]         # 입력받은 수는 무조건 바꾼다.
    di = 1
    while (num-di > 0) and (num+di < N + 1) and (arr[num-di] == arr[num+di]):   # 인덱스 안넘는지 확인, 대칭인지도 확인
        arr[num-di] = 1 ^ arr[num-di]
        arr[num+di] = 1 ^ arr[num+di]
        di += 1     # 더 옆으로 가능한지 확인하기 위해 바꿔준다.

M = int(input())    # 사람 수
for _ in range(M):
    gen, idx = map(int, input().split())
    if gen == 1:
        man(idx)    # 남자일 때
    else:           
        woman(idx)  # 여자일 때

del arr[0]          # padding 제거
cnt = 0
result = []         # 나눠서 출력해야하니 배열하나 새로 초기화
for v in arr:
    cnt += 1
    result.append(v)
    if cnt == 20:   # 20개씩 잘라서 출력
        print(*result)
        result = []
        cnt = 0
if result:          # 나머지 출력
    print(*result)
```

## 🔍 결과

![image-20220225203613942](README.assets/image-20220225203613942.png)