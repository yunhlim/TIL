# [Programmers] 성격 유형 검사하기 [Lv. 1]

## 📚 문제 : [성격 유형 검사하기](https://school.programmers.co.kr/learn/courses/30/lessons/118666)

## 📖 풀이

mbti를 오마주한 성격유형 검사하기 문제이다. RT, CF, JM, AN이 쌍으로 테스트가 된다.

점수 판단은 아래와 같다.

> 매우 비동의 비동의 약간 비동의 모르겠음 약간 동의 동의 매우 동의

RT를 survey의 원소로 받으면 각각 1 ~ 7점으로 올라간다.

- survey의 원소가 먼저 오는 것이 1점이 매우 비동의로 매칭된다. 1점이면 R이 매우 비동의인 것이다.

result를 [0, 0, 0, 0]로 초기화 하고, RT인 경우는 survey 원소 값에 - 4를 한 값을 더해준다. 그리고 TR이면 반대이므로 원소 값에 -4를 한 값을 빼주면 된다.

result 값이 0인 경우는 사전 순으로 앞서는 걸 가져와야 하므로, R을 가져오면 된다.

0보다 작거나 같을 때는 사전 순으로 앞서는 걸 가져오고, 0보다 크면 사전 순으로 나중에 오는 글자를 가져와 출력하면 된다.

## 📒 코드

```python
def solution(survey, choices):
    result = [0, 0, 0, 0]   # RT, CF, JM, AN
    for i in range(len(survey)):
        if survey[i] == 'RT':
            result[0] += choices[i] - 4
        elif survey[i] == 'TR':
            result[0] -= choices[i] - 4
        elif survey[i] == 'CF':
            result[1] += choices[i] - 4
        elif survey[i] == 'FC':
            result[1] -= choices[i] - 4
        elif survey[i] == 'JM':
            result[2] += choices[i] - 4
        elif survey[i] == 'MJ':
            result[2] -= choices[i] - 4
        elif survey[i] == 'AN':
            result[3] += choices[i] - 4
        else:
            result[3] -= choices[i] - 4
            
    answer = ''
    if result[0] <= 0:
        answer += 'R'
    else:
        answer += 'T'
    if result[1] <= 0:
        answer += 'C'
    else:
        answer += 'F'
    if result[2] <= 0:
        answer += 'J'
    else:
        answer += 'M'
    if result[3] <= 0:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer
```