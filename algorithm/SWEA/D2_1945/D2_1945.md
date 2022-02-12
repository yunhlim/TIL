# [SWEA] 1945. 간단한 소인수분해 [D2]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

소인수가 2, 3, 5, 7, 11로 주어진 정수 N이 입력으로 들어온다.

정수를 소인수로 나누어 각각의 개수를 찾아주면 된다.

따라서 for문을 순회하면서 소인수로 나누어 떨어지면 소인수의 개수를 증가시키고, 그 때의 몫을 다시 나누어주는 걸 반복한다.

## 📒 코드

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = [2,3,5,7,11]
    cnt_lst = [0,0,0,0,0]
    for i in range(5):
        while N % num_lst[i] == 0:
            cnt_lst[i] += 1
            N //= num_lst[i]
    print(f'#{tc} ', end='')
    print(*cnt_lst)
```

## 🔍 결과

![image-20220210194332340](D2_1945.assets/image-20220210194332340.png)