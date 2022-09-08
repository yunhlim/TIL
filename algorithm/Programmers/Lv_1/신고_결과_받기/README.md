# [Programmers] Lv 1. 신고 결과 받기 [2022 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

## 📖 풀이

**딕셔너리**를 활용한다.

결과를 출력할 리스트를 만든다. 신입사원 수 만큼 0으로 초기화 한다.

그리고 각 유저의 id에 해당하는 idx 값을 저장하는 딕셔너리를 하나 만들어 넣어준다.

어떤 유저를 신고한 유저들을 세트 자료형에 저장한다.

- set 자료형에 담는 이유는 중복으로 신고한 경우, 한 번으로 처리하기 위함이다.
- 이 때 딕셔너리로 신고당한 유저를 key, 신고한 유저들을 set 자료형에 담는다.

신고한 유저가 k 값보다 크거나 같은 경우, 신고한 유저 각각의 결과를 출력할 리스트 idx 값에 1을 더해준다. 그리고 그 값을 출력한다.

## 📒 코드

```python
def solution(id_list, report, k):
    arr = {}        # 신고한 아이디들의 집합
    id_idxs = {}     # 아이디들의 인덱스 찾기
    answer = [0 for _ in range(len(id_list))]
    
    for idx, id in enumerate(id_list):
        id_idxs[id] = idx
        arr[id] = set()     # 중복된 값은 제거하기 위해 set 자료형으로 초기화
        
    for v in report:
        to_id, from_id = v.split()
        arr[from_id].add(to_id)
        
    for key in arr:
        if len(arr[key]) >= k:
            for id in arr[key]:
                answer[id_idxs[id]] += 1
    
    return answer
```

