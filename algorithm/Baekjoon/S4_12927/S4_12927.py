arr = list(input())
for i in range(len(arr)):   # Y는 1로 N은 0으로 바꾼다.
    if arr[i] == 'Y':
        arr[i] = 1
    else:
        arr[i] = 0
arr = [0] + arr     # 1 ~ N개이므로 0을 앞에 붙여준다.

cnt = 0             # 스위치 누른 횟수
s = 1               # 현재 확인하는 인덱스
while s < len(arr): # s를 1부터 옆으로 이동시키며 확인한다.
    if arr[s] == 1: # s가 1일 때만 스위치를 누른다.
        cnt += 1    # 스위치 누른 횟수 +1
        for i in range(s, len(arr)):
            if i % s == 0:  # 현재 인덱스가 s의 배수일 때
                arr[i] = 1 ^ arr[i]     # xor연산자로 스위칭
    s += 1          # 확인 했으면 옆으로 이동한다.

print(cnt)