n = int(input())
m = int(input())
arr = set(input().split()) if m else set()
move = 0
cnt = abs(n - 100)          # 숫자버튼을 이용하지 않는 경우 눌러야하는 횟수
while True:
    if cnt < move:          # 숫자버튼을 이용한 경우가 절대로 답이 될 수 없을 때
        break
    # 이동하고 싶은 채널에서 거리를 1씩 늘려가며 확인한다.
    if n - move >= 0 and not set(str(n - move)) & arr:  
        # - 방향 채널의 길이가 + 방향의 채널의 길이보다 작을 수 있다.
        # 0보다 작아지진 않는다.
        cnt = len(str(n - move)) + move             # 채널의 번호를 누르고 이동하는 경우
        break
    elif not set(str(n + move)) & arr:
        cnt = len(str(n + move)) + move
        break
    move += 1       # 거리를 +1

print(cnt)