# [Programmers] Lv 1. 신규 아이디 추천 [2021 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [신규 아이디 추천](https://school.programmers.co.kr/learn/courses/30/lessons/72410)

## 📖 풀이

### 1단계

대문자로 바꿔주는 걸 ord()와 chr()를 활용해 해결했다. 파이썬의 string method인 `string.upper`를 사용해도 된다.

### 2단계

알파벳 소문자와 숫자, `-, _`가 오는 경우만 answer에 더해준다, `.`은 3단계에서 해결한다.

### 3단계

`.`이 나오는 경우 answer에 더해주고, answer의 마지막에 `.`이 있는 경우는 더하지 않는다.

### 4단계

처음이나 끝에 `.`을 제거하기 위해 strip('.') 메서드를 활용하여 `.`을 제거한다.

> strip()은 양쪽에 특정 문자가 나오지 않을 때까지 제거할 수 있다. strip()에 아무것도 넣지 않은 경우는 공백을 제거한다.

### 5단계

빈 문자열인 경우는 a를 넣어준다.

### 6단계

길이가 15보다 크면 나머지를 자른다. 그리고 오른쪽에 `.`을 제거하기 위해 `rstrip('.')`을 활용한다.

### 7단계

길이가 2자 이하이면, 남은 길이만큼 마지막 글자를 곱해서 더해준다.

## 📒 코드

```python
def solution(new_id):
    answer = ''
    for c in new_id:
        if 'A' <= c <= 'Z':     # 대문자를 소문자로 변경
            answer += chr(ord(c) + 32)
        elif 'a' <= c <= 'z' or '0' <= c <= '9' or c in '-_':
            answer += c

        if answer and c == '.' and answer[-1] != '.':        # .이 나온 경우
                answer += c

    answer = answer.strip('.')        # 처음이나 끝에 .이 있으면 제거
    
    if len(answer) > 15:                # 길이가 15보다 크면 잘라주고 양쪽으로 .을 지워준다.
        answer = answer[:15]
        answer = answer.rstrip('.')
    if not answer:                      # 아무 것도 없으면 a를 넣어준다.
        answer = 'a'
    if len(answer) <= 2:
        answer += (3 - len(answer)) * answer[-1]
    return answer
```
