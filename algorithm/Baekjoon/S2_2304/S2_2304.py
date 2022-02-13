N = int(input())    # 기둥의 개수

min_x = 1001 # 기둥이 있는 위치 최소값
max_x = 0 # 기둥이 있는 위치 최대값
max_height = 0 # 제일 높은 기둥의 높이
max_height_x = 0 # 제일 높은 기둥이 있는 위치
height_lst = [0 for _ in range(0, 1001)]    # index는 위치, 값은 height
result = 0

for i in range(N):   
    x, height = map(int, input().split())  # 기둥의 위치와 높이를 변수에 넣어준다.
    if x > max_x:   max_x = x   # 기둥 위치의 최대 최소값을 찾는다.
    if x < min_x:   min_x = x
    if height > max_height:
        max_height = height # 기둥의 최고 높이
        max_height_x = x    # 최고 높을 때의 위치
    height_lst[x] = height  # 높이 값을 리스트에 담아준다.

max_height = 0  # 변수 재활용하기 위해 초기화, 현재까지 제일 높은 기둥
for i in range(min_x, max_height_x + 1):    # 왼쪽부터 가장 높은 기둥까지 현재 최대높이 업데이트
    if max_height < height_lst[i]:
        max_height = height_lst[i]
    result += max_height    # 현재 가장 최고 높이를 더해준다.

max_height = 0 # 변수 재활용하기 위해 초기화, 현재까지 제일 높은 기둥
for i in range(max_x, max_height_x, -1):    # 오른쪽부터 가장 높은 기둥 전까지 현재 최대높이 업데이트
    if max_height < height_lst[i]:
        max_height = height_lst[i]
    result += max_height    # 현재 가장 최고 높이를 더해준다.

print(result)