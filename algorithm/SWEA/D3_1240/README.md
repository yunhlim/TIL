# [SWEA] 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=%EB%8B%A8%EC%88%9C+2%EC%A7%84+%EC%95%94%ED%98%B8%EC%BD%94%EB%93%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

암호 코드를 먼저 찾고, 검증코드가 맞는지 찾아 출력한다.

암호 코드의 시작점을 찾는 함수를 만든다.

배열이 들어오면 앞 뒤로 0이 채워져서 나타난다.따라서 뒤부터 0이 아닌 값이 있는지 확인한다. 행에 0이 아닌 값이 없으면 다음 행을 탐색한다.

이 때 배열이 50x100으로 재귀로 한 칸씩 확인해도 가능하니 재귀호출하는 방법을 사용한다.

암호의 시작점을 찾았으면, 해독하는 함수를 만들어 값을 넣어준다.

해독하는 함수는 암호의 길이만큼 슬라이싱으로 자르고, 딕셔너리에 대치되는 값을 찾아 넣어준다.

> “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.

구한 8자리의 수를 문제에 나와있는 계산 방법인 위의 계산을 통해 암호코드를 검증한 후 출력한다.

## 📒 코드

```python
def find_code(x, y):        # 암호 위치를 찾는다.
    if y < 6:               # y 값이 6보다 작아지면 다음 행 탐색
        y = m - 1
        x += 1
    if arr[x][y] != '0':    # 0이 아닌 수가 나오면 암호를 찾은 것이다.
        return x, y - 55   # 암호의 시작점을 반환
    else:
        return find_code(x, y - 1)  # 0이 나오면 다음 열을 탐색


def solve_code(x, y):           # 암호 시작점을 받아 해독한다.
    code = arr[x][y:y + 56]     # 암호의 길이 56
    result = [0]                # 시작부분에 padding을 넣어준다.
    for i in range(8):          # 딕셔너리에 적은 코드와 같으면 그 값인 숫자로 넣어준다.
        result.append(d[code[0 + i * 7:(i + 1) * 7]])
    odd_sum, even_sum = 0, 0
    for i in range(1, 9):
        if i % 2:               # 홀수일 때와 짝수일 때 각각의 합을 찾는다.
            odd_sum += result[i]
        else:
            even_sum += result[i]

    if (odd_sum * 3 + even_sum ) % 10:  # 계산 후 10으로 나누어 떨어지는지 판별
        return 0
    else:
        return sum(result)


d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,\
'0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    print(f'#{tc} {solve_code(*find_code(0, m - 1))}')
```

## 🔍 결과

![image-20220323190438092](README.assets/image-20220323190438092.png)