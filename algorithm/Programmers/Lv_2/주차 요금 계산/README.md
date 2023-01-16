# [Programmers] Lv2. 주차 요금 계산 [2022 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [주차 요금 계산](https://school.programmers.co.kr/learn/courses/30/lessons/92341)

## 📖 풀이

문제가 조금 복잡하지만 풀이가 어렵지는 않다.

**딕셔너리**를 활용한다. 카카오는 딕셔너리 활용 문제가 많다.

딕셔너리의 key는 차량 번호이고 값은 2가지를 리스트로 저장한다.

> [들어온 시간 정보, 총 주차된 시간]

차가 들어와 있지 않으면 들어온 시간 정보에 -1이 있게끔 초기화 한다.

차량이 나가면 -1로 바꿔줄 것이다.

모든 차량 번호를 `[-1, 0]`로 초기화해준다.

그리고 입/출차 기록을 확인해 차량 시간을 구한다.

```python
    cars = {}       # key는 차량 번호, 값은 [<없으면 -1, 있으면 시간>, 총 주차된 시간]
    
    for record in records:
        time, car_num, in_out = record.split()
        car_num = car_num
        time = int(time[:2]) * 60 + int(time[3:])
        if not cars.get(car_num):       # 차량 정보가 없으면 넣어준다.
            cars[car_num] = [-1, 0]   # 들어온 시간(-1이면 들어오지 않은 것), 총 소요 시간
        if in_out == 'IN':          # 들어왔을 때
            cars[car_num][0] = time  # 분으로 변경해서 넣어준다.
        else:                       # 나갔을 때
            cars[car_num][1] += time - cars[car_num][0]   # 시간을 넣어준다.
            cars[car_num][0] = -1   # 없다는 걸 표시
```



모든 입/출차 기록을 확인한 후, 들어오고 나가지 않은 차들을 확인해 추가로 차량 시간을 구해 더해준다.

기본 시간으로 기본 요금을 구해주고 넘어가면 단위 시간에 따른 단위 요금을 환산해 더해준다.

**차량 번호가 key인 딕셔너리를 순회할 때 sorted()로 정렬하여 순회한다!**

```python
    answer = []     # 차량번호 순으로 요금을 넣어주는 리스트
    
    last_time = 23 * 60 + 59
    for car in sorted(cars):
        if cars[car][0] != -1:      # 23:59분까지 주차되어 있다면
            cars[car][1] += last_time - cars[car][0]    # 주차되어있는 차들 시간 계산
        time = cars[car][1]         # 주차한 시간
        fee = 0                     # 지불할 요금
        if time:                    # 주차한 경우
            fee += fees[1]          # 기본 시간 지불
            if time > fees[0]:          # 기본 시간 이상 주차한 경우
                time -= fees[0]         # 주차한 시간 - 기본 시간
                fee += fees[3] * (time // fees[2] + (1 if time % fees[2] else 0))   # 단위 요금 계산
        answer.append(fee)
```

## 📒 코드

```python
def solution(fees, records):
    # fees : [기본시간, 기본 요금, 단위 시간, 단위 요금]
    # records : ["시간 차량번호 내역", ...]
    cars = {}       # key는 차량 번호, 값은 [<없으면 -1, 있으면 시간>, 총 주차된 시간]
    
    for record in records:
        time, car_num, in_out = record.split()
        car_num = car_num
        time = int(time[:2]) * 60 + int(time[3:])
        if not cars.get(car_num):       # 차량 정보가 없으면 넣어준다.
            cars[car_num] = [-1, 0]   # 들어온 시간(-1이면 들어오지 않은 것), 총 소요 시간
        if in_out == 'IN':          # 들어왔을 때
            cars[car_num][0] = time  # 분으로 변경해서 넣어준다.
        else:                       # 나갔을 때
            cars[car_num][1] += time - cars[car_num][0]   # 시간을 넣어준다.
            cars[car_num][0] = -1   # 없다는 걸 표시
            
    answer = []     # 차량번호 순으로 요금을 넣어주는 리스트
    
    last_time = 23 * 60 + 59
    for car in sorted(cars):
        if cars[car][0] != -1:      # 23:59분까지 주차되어 있다면
            cars[car][1] += last_time - cars[car][0]    # 주차되어있는 차들 시간 계산
        time = cars[car][1]         # 주차한 시간
        fee = 0                     # 지불할 요금
        if time:                    # 주차한 경우
            fee += fees[1]          # 기본 시간 지불
            if time > fees[0]:          # 기본 시간 이상 주차한 경우
                time -= fees[0]         # 주차한 시간 - 기본 시간
                fee += fees[3] * (time // fees[2] + (1 if time % fees[2] else 0))   # 단위 요금 계산
        answer.append(fee)
        
    return answer
```

