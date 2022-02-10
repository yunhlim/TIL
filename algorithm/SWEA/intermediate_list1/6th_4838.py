T = int(input()) 

for tc in range(1, T+1):
    N = int(input())    # 양수의 개수
    num_lst = list(map(int, input().split()))
    max_num = num_lst[0]
    min_num = num_lst[0]

    for i in range(N):
        if max_num < num_lst[i]:
            max_num = num_lst[i]
        elif min_num > num_lst[i]:    # 이미 최댓값이면 최솟값인지 확인 안해도되니 elif로 
            min_num = num_lst[i]
    print(f'#{tc} {max_num - min_num}')