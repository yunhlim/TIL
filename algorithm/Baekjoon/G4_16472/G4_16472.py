n = int(input())    # 인식할 수 있는 문자 개수
string = input()    # 입력받은 문자열

s, e = 0, 0     # 투포인터
max_l = 0       # 출력할 최대 길이
dic = {}        # s와 e 이내의 문자를 담아준다.
dic[string[e]] = 1      # 시작 문자를 담는다.
while True:
    if n >= len(dic.keys()):  # 문자의 개수가 n 이하일 때만
        max_l = max(max_l, e - s + 1)   # 최대 길이와 비교해서 업데이트
        e += 1                      # e 전진
        if e == len(string):        # e가 인덱스를 초과하면 break
            break
        if dic.get(string[e]):      # 값을 넣어준다.
            dic[string[e]] += 1     # 이미 키가 존재하는 경우
        else:
            dic[string[e]] = 1      # 키가 없는 경우
    else:
        if dic[string[s]] == 1:     # 값을 빼준다.
            del dic[string[s]]      # 개수가 하나인 경우 키를 제거한다.
        else:
            dic[string[s]] -= 1     # 개수가 하나보다 많으면 개수를 하나 뺀다.
        s += 1                      # 문자의 개수가 더 많으면 s 전진

print(max_l)