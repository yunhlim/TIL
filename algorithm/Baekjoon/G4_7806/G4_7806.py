while True:
    try:
        n, k = map(int, input().split())    # 입력제한이 없는 경우 try except로 해결
    except:
        break
    temp = k                    # k를 소인수분해 계산하기 위해 temp에 담는다. 
    smalls = {}                 # 소인수와 소인수의 개수를 담기 위해 딕셔너리 사용
    for i in range(2, k+1):     # k의 소인수 분해
        if i * i > k:           # 제곱근보다 클 경우 종료
            break
        while temp % i == 0:    # 소인수일 경우 개수만큼 담아준다.
            temp //= i
            if smalls.get(i):
                smalls[i] += 1    # k의 소인수와 갯수를 담기 위해 list로 담는다.
            else:
                smalls[i] = 1
    if temp != 1:               # 제곱근보다 큰 소인수 추가
        smalls[temp] = 1         # k의 소인수가 아직 덜 나왔을 때 추가

    result = 1
    for num, cnt in smalls.items():
        temp = n
        cnt2 = 0                # 소인수가 n!에 곱해진 개수
        while temp // num:
            temp //= num
            cnt2 += temp
            if cnt2 >= cnt:     # n!에 존재하는 소인수의 개수가 k의 개수보다 크거나 같으면 종료한다.
                break           # 더 파악할 필요가 없다.

        result *= num ** min(cnt, cnt2) # n!에 존재하는 소인수의 개수와, k의 소인수 개수 중 최소값을 소인수에 거듭제곱해 곱해준다.
    print(result)