# [SWEA] 5789. 현주의 상자 바꾸기 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm&categoryId=AWYygN36Qn8DFAVm&categoryType=CODE&problemTitle=%ED%98%84%EC%A3%BC%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

머리가 아파 .. 문제를 읽는데 한참 걸렸다.

생각보다 문제는 쉽다.

들어오는 N의 정수개만큼 상자가 순차적으로 출력되어야 하므로 리스트에 담는다.

인덱스를 0이 아니라 1부터 주기 위해 N+1개의 리스트로 만든다.

인덱스와 값을 묶는 카운트 배열을 만드는 것이 핵심이다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split()) # N: 정수의 개수, Q: 변경 횟수
    num_lst = [0 for _ in range(N+1)] # 0번 상자를 추가해준다. 쓰진 않는다.
    for i in range(1, Q+1):
        L, R = map(int,input().split())
        for j in range(L,R+1):  # L번부터 R번 상자 순회
            num_lst[j] = i  # 상자들에 i를 담는다.

    print(f'#{tc} ', end='')
    print(*num_lst[1:])
```

## 🔍 결과 : **Pass**