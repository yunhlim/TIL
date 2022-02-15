def search_cnt(pages, page):  # 이진 탐색하는 횟수를 출력
    cnt = 1
    start = 1
    end = pages
    while page != (start + end) // 2:  # page를 찾으면 탐색 종료
        cnt += 1
        if page > (start + end) // 2:
            start = (start + end) // 2
        else:
            end = (start + end) // 2
    return cnt


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())  # P: 전체 쪽수 A, B: A, B가 찾을 쪽 번호
    cnt_A = search_cnt(P, A)  # A가 찾을 횟수
    cnt_B = search_cnt(P, B)  # B가 찾을 횟수
    win = 0
    if cnt_A == cnt_B:  # 비기면 0
        win = 0
    elif cnt_A > cnt_B:  # 횟수가 더 적은 쪽이 이긴다.
        win = 'B'
    else:
        win = 'A'
    print(f'#{tc} {win}')
