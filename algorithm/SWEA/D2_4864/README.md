# [SWEA] 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교 [D2]

## 📚 문제

>두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
>
>예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
> 
>
>ABC
>
>ZZZZZ**ABC**ZZZZZ
>
>두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
> 
>
>ABC
>
>ZZZZ**A**Z**BC**ZZZZZ
>
>문자열이 일치하지 않으므로 0을 출력.
>
> 
> 
>
>**[입력]**
> 
>
>첫 줄에 테스트 케이스 개수 T가 주어진다. (1≤T≤50)
> 
>
>다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)
>
> 
>
>**[출력]**
>
>각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

보이어 무어 알고리즘을 사용해서 풀어 보았다. 패턴 문자열의 맨 끝부터 비교하며 현재 비교하는 문자가 패턴 문자열의 끝과 같으면 거꾸로 패턴과 같은지 확인한다. 같으면 종료시키고 다르면 한 칸 전진한다. 현재 비교하는 문자가 패턴 문자열 안에 없으면 패턴의 길이만큼 이동시키고 문자열 안에 있으면 그 문자까지 이동시켜 해결해나가는 알고리즘이다.

## 📒 코드

```python
# 보이어 무어 알고리즘
T = int(input())
for tc in range(1, 1+T):
    pattern = input()   # 패턴
    string = input()    # 패턴이 있는지 확인할 문자열
    p_l = len(pattern)  # 패턴의 길이
    s_l = len(string)   # 문자열의 길이
    i = p_l - 1         # 패턴의 뒤부터 비교
    is_str = 0          # 패턴이 문자열에 존재하는지 확인

    while i < s_l:
        if string[i] == pattern[-1]:  # 패턴의 끝과 문자가 같을 때
            for j in range(p_l):    # 패턴의 끝이 같을 때 패턴과 역순으로 비교해서 다 같은지 확인
                if string[i-j] != pattern[-1-j]:    # 다르면 1만큼 이동
                    i += 1
                    break
            else:
                is_str = 1  # 패턴이 문자열에 존재
                i = s_l     # 있으니 반복문을 종료

        else:    # 문자와 패턴의 끝이 다를 때
            for j in range(1, p_l):
                if string[i] == pattern[-1-j]:  # 패턴 내의 같은 문자를 찾아 거기까지 이동
                    i += j
                    break
            else:   # 패턴 내에 없으면 패턴의 길이만큼 이동
                i += p_l

    print(f'#{tc} {is_str}')
```

## 🔍 결과 : Pass