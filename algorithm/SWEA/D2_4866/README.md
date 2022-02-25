#  [SWEA] 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사 [D2]

## 📚 문제

> 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
>  
>
> 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
>  
>
> 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
>  
>
> print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
>
> 
>  
>
> **[입력]**
>
> 
> 첫 줄에 테스트 케이스 개수 T가 주어진다. 1≤T≤50
>  
>
> 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
>
>  
>
> **[출력]**
>  
>
> 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

stack 자료구조를 활용한다.

문자열을 읽으며 여는 괄호를 stack에 담는다.

닫는 괄호를 만나면 stack의 top과 확인해 같으면 stack의 top을 지운다.

여는 괄호와 닫는 괄호의 짝이 맞지 않으면 검사 실패

닫는 괄호가 나왔는데 여는 괄호가 나와도 검사 실패

문자열을 다 검사하고 stack에 괄호가 남아있으면 아직 덜 닫힌 것이니 이것도 검사 실패이다.

위 과정을 다 확인하여 답을 출력한다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T + 1):
    s = input() # 입력받은 문자열
    stack = []  # 여는 괄호를 담을 stack
    result = 0  # 괄호 검사
    for c in s:
        if c in '{(':   # 여는 괄호는 stack에 넣는다.
            stack.append(c)
        elif c in '})': # 닫는 괄호를 stack 값과 확인
            # 여는 괄호가 있는지 1차 확인, 입력받은 문자와 stack의 top이랑 비교해서 괄호가 맞다면 제거
            if stack and ((stack[-1] == '{' and c == '}') or (stack[-1] == '(' and c == ')')):
                stack.pop()
            else:   # 괄호의 짝이 맞지 않거나, 여는 괄호가 없다면 break
                break
    else:
        if not stack:   # 여는 괄호가 다 닫혔는지 확인
            result = 1
    print(f'#{tc} {result}')
```

## 🔍 결과 : Pass