n = int(input())
arr = [int(input()) for _ in range(n)]  # 다솜이와 나머지 사람의 득표수
cnt = 0     # 매수한 사람의 수

while True:
    max = 0
    for i in range(n):
        if arr[i] >= arr[max]:  # 가장 득표수가 많은 후보 선택
            max = i
    if max:                 # 다솜이보다 득표수가 많은 사람이 있을 때
        cnt += 1            # 매수
        arr[0] += 1         # 다솜이의 득표수 +1
        arr[max] -= 1       # 득표수가 많은 후보의 득표수 -1
    else:
        print(cnt)          # 매수한 사람의 수 출력
        break