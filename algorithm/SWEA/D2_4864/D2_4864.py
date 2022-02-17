# 보이어 무어 알고리즘
T = int(input())
for tc in range(1, 1+T):
    pattern = input()   # 패턴
    string = input()    # 패턴이 있는지 확인할 문자열
    p_l = len(pattern)  # 패턴의 길이
    s_l = len(string)   # 문자열의 길이
    i = p_l - 1         # 패턴의 뒤부터 비교
    is_str = 0          # 패턴이 문자열에 존재하는지 확인

    while i < s_l:
        if string[i] == pattern[-1]:  # 패턴의 끝과 문자가 같을 때
            for j in range(p_l):    # 패턴의 끝이 같을 때 패턴과 역순으로 비교해서 다 같은지 확인
                if string[i-j] != pattern[-1-j]:    # 다르면 1만큼 이동
                    i += 1
                    break
            else:
                is_str = 1  # 패턴이 문자열에 존재
                i = s_l     # 있으니 반복문을 종료

        else:    # 문자와 패턴의 끝이 다를 때
            for j in range(1, p_l):
                if string[i] == pattern[-1-j]:  # 패턴 내의 같은 문자를 찾아 거기까지 이동
                    i += j
                    break
            else:   # 패턴 내에 없으면 패턴의 길이만큼 이동
                i += p_l

    print(f'#{tc} {is_str}')