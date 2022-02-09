import sys
sys.stdin = open('input.txt')   # input.txt 불러오는 방법

T = 10  # 테스트 케이스 10개
location = [-2,-1,1,2]  # 빌딩 양 옆으로 2칸 씩 보기위해 리스트 지정

for tc in range(1, T+1):
    length = int(input())   # 리스트의 길이 입력
    arr = list(map(int, input().split()))
    jomang = 0  # 조망권 세대 수 합

    for i in range(2,length-2):
        top = 0 # 빌딩 거리 2 사이에서 가장 큰 빌딩의 높이 찾기, 초기화
        for loc in location:
            if arr[i+loc] > top:
                top = arr[i+loc]    # 가장 큰 빌딩으로 선택
        if arr[i] - top > 0: jomang += arr[i] - top # 조망권 세대를 합

    print(f'#{tc} {jomang}')    # 원하는 모양으로 출력