# [Programmers] Lv 1. 실패율 [2019 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889)

## 📖 풀이

총 스테이지 개수는 1부터 500까지 , 사용자들이 도달한 stages의 개수는 200,000까지 주어진다.

1. 카운팅하는 **딕셔너리**를 만든다.

사용자들이 도달한 스테이지들의 개수를 카운팅 딕셔너리로 세준다.

카운팅 배열로 해도 되지만 나는 딕셔너리를 사용해 만들었다.

예제로 설명해보면,

stages가 [2, 1, 2, 6, 2, 4, 3, 3] 으로 주어졌다.

그러면 stage_cnt_dict 에 {1: 1, 2: 3, 3: 2, 4: 1, 6: 1}로 담아준다.

위와 같이 카운팅하는 딕셔너리를 만들어 넣어주었다.

```python
    stage_cnt_dict = {}
    for stage in stages:    # 스테이지의 개수를 카운팅해준다.
        stage_cnt_dict[stage] = stage_cnt_dict.get(stage, 0) + 1
    
```

2. 스테이지 별 참여 인원과 실패 인원을 리스트에 담아준다.

위에서 구한 stage_cnt_dict의 key가 도달했지만 아직 완료하지 못한 스테이지이므로, 1부터 key까지 모든 스테이지들의 참여 인원에 value 만큼 더해준다.

그리고 key와 일치하는 스테이지만 실패 인원을 value 만큼 더한다.

```python
    arr = [[0, 0] for _ in range(N + 2)]  # 도달한 플레이어 수, 클리어 못한 플레이어 수
    
    for stage in stage_cnt_dict:
        for j in range(1, stage + 1):
            arr[j][0] += stage_cnt_dict[stage]      # 도달한 플레이어 수
            if stage == j:                          # 클리어 못한 플레이어 수
                arr[j][1] += stage_cnt_dict[stage]
```

3. 실패율과 그 때 스테이지의 인덱스를 담고 실패율로는 내림차순 정렬, 2차적으로 인덱스로 오름차순 정렬한다.

참여인원과 실패인원으로 실패율을 담고 정렬을 해주기 위해 index 값도 담아준다.

그리고 나서 key=lambda를 활용해 1차적으로는 실패율로 내림차순 정렬, 2차적으로는 인덱스로 오름차순 정렬을 한다.

그리고 인덱스만 순서대로 뽑아 출력하면 된다.

```python
    arr_2 = []      # 실패율, 인덱스로 담는다.
    for i in range(1, N + 1):
        if arr[i][0] == 0:
            arr_2.append([0, i])
        else:
            arr_2.append([arr[i][1] / arr[i][0], i])        # 실패율, 인덱스
    arr_2.sort(key=lambda x: [-x[0], x[1]])

    answer = []
    for v in arr_2:
        answer.append(v[1])
    
    return answer
```

## 📒 코드

```python
def solution(N, stages):
    stage_cnt_dict = {}
    for stage in stages:
        stage_cnt_dict[stage] = stage_cnt_dict.get(stage, 0) + 1
    arr = [[0, 0] for _ in range(N + 2)]  # 도달한 플레이어 수, 클리어 못한 플레이어 수
    
    for stage in stage_cnt_dict:
        for j in range(1, stage + 1):
            arr[j][0] += stage_cnt_dict[stage]
            if stage == j:
                arr[j][1] += stage_cnt_dict[stage]

    arr_2 = []
    for i in range(1, N + 1):
        if arr[i][0] == 0:
            arr_2.append([0, i])
        else:
            arr_2.append([arr[i][1] / arr[i][0], i])
    arr_2.sort(key=lambda x: [-x[0], x[1]])

    answer = []
    for v in arr_2:
        answer.append(v[1])
    
    return answer
```

