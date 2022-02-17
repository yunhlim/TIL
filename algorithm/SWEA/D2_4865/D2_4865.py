# 글자수
T = int(input())
for tc in range(1, T+1):

    str1 = set(input())     # 중복 제거해서 set에 담는다.
    str2 = input()
    dict = {}
    for c in str1:  # 딕셔너리의 key에 중복 제거한 문자로 초기화 시켜준다.
        dict[c] = 0

    for c in str2:  # str2의 문자를 하나씩 확인
        if c in str1:   # 딕셔너리 안에 str2의 문자가 있으면 그 value에 1을 더한다.
            dict[c] += 1

    max_num = 0
    for v in dict.values(): # 딕셔너리의 value들을 순회하며 가장 큰 값을 찾는다.
        if v > max_num:
            max_num = v
    print(f'#{tc} {max_num}')