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