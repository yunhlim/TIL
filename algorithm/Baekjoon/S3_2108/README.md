# [Baekjoon] 2108. 통계학 [S3]

## 📚 문제 : [통계학](https://www.acmicpc.net/problem/2108)

## 📖 풀이

평균값을 구하기 위해 반올림을 하는 함수로 round()를 사용한다.

최빈값을 구하기 위해 딕셔너리를 사용한다. 딕셔너리를 사용해 key는 수이고 value로 개수를 넣어준다.

그리고 최빈값이 여러가지 있는 경우 두 번째로 작은 수를 반환하기 위해, 딕셔너리에 담겨있는 정보를 리스트로 바꾼다.

- 개수로 1차적으로 내림차순 정렬한다.(최빈 값을 찾기 위함)
- 수로 2차적으로 오름차순 정렬한다.(최빈 값 중 2번째로 작은 값을 찾기 위함)

이 때, n이 1인 경우는 error가 날 수 있으니 n > 1일 때만 2번째 값을 확인한다.

위 변환된 리스트의 첫 번째와 두 번째로 많은 수의 개수가 같은 경우는 두 번째의 수를 출력하도록 한다.

최댓값과 최솟값은 같이 수들이 담겨있는 배열을 순회하며 찾아주면 된다.

## 📒 코드

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
cnt_dic = {}        # 최빈값을 찾기 위한 딕셔너리
total = 0           # 평균값을 찾기 위한 합계
max_num = arr[0]    # 최댓값
min_num = arr[0]    # 최솟값

for i in range(n):
    cnt_dic[arr[i]] = cnt_dic.get(arr[i], 0) + 1        # 딕셔너리에 key에 해당하는 수의 개수 저장
    total += arr[i]
    if max_num < arr[i]:        # 최댓값 저장
        max_num = arr[i]
    if min_num > arr[i]:        # 최솟값 저장
        min_num = arr[i]

print(round(total / n)) 

arr.sort()              # 중앙값을 찾기 위해 정렬
print(arr[n // 2])      # 중앙값 출력

cnt_arr = []
for k, v in cnt_dic.items():    # 딕셔너리를 리스트로 변환
    cnt_arr.append([v, k])

cnt_arr.sort(key=lambda x: (-x[0], x[1]))      # 최빈값을 찾기 위해 개수는 내림차순 정렬, 수는 오름차순 정렬

if n > 1 and cnt_arr[0][0] == cnt_arr[1][0]:        # 여러 개의 최빈 값이 존재하는 경우
    many_num = cnt_arr[1][1]                        # 두 번째로 작은 값 출력
else:
    many_num = cnt_arr[0][1]                        # 하나의 최빈 값이 존재하는 경우

print(many_num)

print(max_num - min_num)        # 최댓값 - 최솟값
```

## 🔍 결과

![image-20220802001550324](README.assets/image-20220802001550324.png)