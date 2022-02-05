x, y, w, h = map(int, input().split())
lst_distance = [x, y, w-x, h-y] # 직사각형의 각 변까지의 최소 거리 값
min_distance = lst_distance[0]   # 가장 작은 값 초기화
for distance in lst_distance:   # min함수 대신 직접 만든다.
    if min_distance > distance:
        min_distance = distance
print(min_distance)