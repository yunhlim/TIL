N = int(input())    # 스위치 개수
arr = [0] + list(map(int, input().split()))     # 스위치 상태 받아오기, padding으로 1번부터

def man(num):   # 남자는 배수 바꾸기
    for i in range(num, N + 1):
        if i % num == 0:            # 배수인지 확인
            arr[i] = 1 ^ arr[i]     # 바꿔준다.

def woman(num): # 여자는 대칭인 만큼 바꾸기
    arr[num] = 1 ^ arr[num]         # 입력받은 수는 무조건 바꾼다.
    di = 1
    while (num-di > 0) and (num+di < N + 1) and (arr[num-di] == arr[num+di]):   # 인덱스 안넘는지 확인, 대칭인지도 확인
        arr[num-di] = 1 ^ arr[num-di]
        arr[num+di] = 1 ^ arr[num+di]
        di += 1     # 더 옆으로 가능한지 확인하기 위해 바꿔준다.

M = int(input())    # 사람 수
for _ in range(M):
    gen, idx = map(int, input().split())
    if gen == 1:
        man(idx)    # 남자일 때
    else:           
        woman(idx)  # 여자일 때

del arr[0]          # padding 제거
cnt = 0
result = []         # 나눠서 출력해야하니 배열하나 새로 초기화
for v in arr:
    cnt += 1
    result.append(v)
    if cnt == 20:   # 20개씩 잘라서 출력
        print(*result)
        result = []
        cnt = 0
if result:          # 나머지 출력
    print(*result)