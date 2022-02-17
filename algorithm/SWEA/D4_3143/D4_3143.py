T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()  # 문자열 A, 포함된 문자열 B
    s = 0   # 이동하는 인덱스
    cnt = 0 # 중복된 문자열 개수 확인

    while s < len(A)-len(B)+1:  # 검색할 문자열을 넘어가면 종료
        if A[s:s+len(B)] == B:  # 패턴이 존재하는지 확인
            cnt += 1
            s += len(B)         # 존재하면 패턴의 길이만큼 이동
        else:
            s += 1
    print(f'#{tc} {len(A)-cnt*(len(B)-1)}')