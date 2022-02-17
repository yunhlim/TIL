# [SWEA] 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 [D2]

## 📚 문제

> ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
>
> 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
>  
>
> 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
>  
>
> | G    | O    | F    | F    | A    | K    | W    | F    | S    | M    |
> | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
> | O    | Y    | E    | C    | R    | S    | L    | D    | L    | Q    |
> | U    | J    | A    | J    | Q    | V    | S    | Y    | Y    | C    |
> | J    | A    | E    | Z    | N    | N    | Z    | E    | A    | J    |
> | W    | J    | A    | K    | C    | G    | S    | G    | C    | F    |
> | Q    | K    | U    | D    | G    | A    | T    | D    | Q    | L    |
> | O    | K    | G    | P    | F    | P    | Y    | R    | K    | Q    |
> | T    | D    | C    | X    | B    | M    | Q    | T    | I    | O    |
> | U    | N    | A    | D    | R    | P    | N    | E    | T    | Z    |
> | Z    | A    | T    | W    | D    | E    | K    | D    | Q    | F    |
>
> **[입력]**
>
> 첫 줄에 테스트 케이스 개수 T가 주어진다. 1≤T≤50
>
> 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
>
> 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
>
> **[출력]**
>  
>
> 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

회문을 판별하는 문제이다. row 방향으로 회문을 판별할 때에는 슬라이싱을 활용해 문자열이 같은지 확인한다.

col 방향으로 회문을 판별하는 것이 약간 까다롭다.

col 방향으로 판별할 때에는 슬라이싱을 할 수 없으니 전치행렬로 만들어서 구하거나, for문으로 값을 하나씩 가져와 넣어주는 방법이 있다. 두 번쨰 방법을 활용하여 col 방향일 경우의 회문도 판별한다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxN 글자판, M 길이의 회문
    arr = [input() for _ in range(N)]  # NxN 글자판

    def rev_str():  # 찾았을 때 찾는 작업을 그만 두기 위해 함수에 넣어 return 해준다.
        for i in range(N):
            for j in range(N - M + 1):  # N개 중 M 길이의 회문을 판별하기 위한 시행은 N-M+1번
                # row 방향
                if arr[i][j:j + M] == arr[i][j:j + M][::-1]:  # row 방향으로 회문 확인
                    print(f'#{tc} {arr[i][j:j + M]}')
                    return  # 종료

                # col 방향
                for k in range(M // 2): # 회문인지 판별
                    if arr[j + k][i] != arr[j + M - k - 1][i]:  # 회문이 아니면 break
                        break
                else:   # 회문일 경우
                    print(f'#{tc} ', end='')
                    for l in range(M):
                        print(arr[j + l][i], end='')
                    print()
                    return  # 종료

    rev_str()

```

## 🔍 결과 : Pass