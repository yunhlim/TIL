N = int(input())
cnt = N
for _ in range(N):
    appear = set()  # 연속된 문자가 아닐 때 그 이전에 나왔던 문자들과 비교
    string = input()
    before = '' # 이전에 나온 문자 저장하는 변수
    for i in string:
        if i != before:         # 연속된 문자인지 확인
            before = i          # 새로운 단어로 연속된 문자인지 확인하는 변수를 바꿔준다.
            if {i} & appear:    # 이전에 나왔던 문자와 같은게 있을 때
                cnt -= 1        # 그룹 단어가 아니므로 감소
                break
            else: appear = appear | {i} # 이전에 나왔던 문자가 아니니 appear에 추가해준다.
print(cnt)