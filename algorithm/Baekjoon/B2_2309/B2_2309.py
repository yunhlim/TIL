arr = [int(input()) for _ in range(9)]

# 오름차순 버블 정렬, 9개 뿐이니 버블정렬을 사용한다.
for i in range(8):
    for j in range(8-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

ssum = 0
for i in range(9):
    ssum += arr[i]

ssum -= 100     # 합에서 100을 빼 스파이 2명 키의 합으로 바꿔준다.
s = 0
e = 8
while s != e:   # 스파이 2명을 찾아야하므로 투포인터를 사용한다.
    if arr[s] + arr[e] == ssum: # 스파이를 찾으면 종료
        del arr[e], arr[s]  # e와 s에 해당하는 스파이 제거
        break
    elif arr[s] + arr[e] > ssum:
        e -= 1
    else:
        s += 1

for i in range(7):  # 스파이를 뺀 일곱난쟁이 출력
    print(arr[i])