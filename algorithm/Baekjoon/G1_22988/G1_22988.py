n, x = map(int, input().split())        # n: 용기의 수, x: 용기의 총 용량
arr = list(map(int, input().split()))   # 가지고있는 용기의 용량들의 집합
arr.sort()          # 오름차순으로 정렬한다.
result = 0          # 가득찬 용기의 개수

for i in range(len(arr)):       # 오름차순으로 정렬한 걸 앞에서부터 센다.
    if arr[i] == x:             # 가득차 있는 용기가 나오는지 확인
        result = len(arr) - i   # 가득차 있는 용기의 개수를 result에 더해준다.
        arr = arr[0:i]          # 가득차 있는 용기들을 제외한다.
        break

s = 0                           # 투포인터 앞에서와 뒤에서 시작한다.
e = len(arr) - 1
length = len(arr)               # 남은 개수를 센다.

while s < e:                    
    if 2 * (arr[s] + arr[e]) >= x:  # 두 용기를 더해서 절반보다 큰지 확인한다.
        e -= 1                      # 크면 e를 1 빼고 s를 1 더한다.
        result += 1                 # 두 용기를 하나로 합쳐 result에 더해준다.
        length -= 2                 # 남은 용기의 개수에 2개를 빼준다.
    s += 1                          # 크던 작던 s는 1씩 움직인다.

result += length // 3               # 남아있는 용기를 3으로 나눈 몫을 더한다.

print(result)