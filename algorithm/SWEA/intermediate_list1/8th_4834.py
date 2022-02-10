T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 카드 수
    card_lst = list(map(int, input()))
    count = [0 for _ in range(10)]

    many_card_num = 0   # 가장 많은 카드에 적힌 숫자
    many_card_cnt = 0   # 위 숫자가 적힌 카드의 개수
    for i in card_lst:
        count[i] += 1

    for i in range(10):
        # 같을 때에 index는 나중에 나온 걸로 선택하라고 했으니 <=로 써준다.
        if many_card_cnt <= count[i]:         
            many_card_num = i
            many_card_cnt = count[i]

    print(f'#{tc} {many_card_num} {many_card_cnt}')