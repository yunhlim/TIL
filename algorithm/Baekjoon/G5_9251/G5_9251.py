arr1 = list(input())    # 첫 번째 문자열
arr2 = list(input())    # 두 번째 문자열

dic = {}                # 딕셔너리에 첫 번째 문자열의 문자는 key에 값에는 인덱스들을 리스트로 넣어준다.
for i in range(len(arr1)):
    if dic.get(arr1[i]):    # 있던 값일 때 추가
        dic[arr1[i]] += [i]
    else:                   # 처음 나왔을 때
        dic[arr1[i]] = [i]

dp = [0 for _ in range(1005)]   # dp 초기화
for s in arr2:      # 두 번째 문자열 순회
    v_arr = dic.get(s)  # 문자의 첫번째 문자열에서의 인덱스들의 집합
    if v_arr:   # 리스트가 있을 때
        dic2 = {}       # 값을 나중에 바꿔주기 위함
        for v in v_arr:
            if v:       # v가 0이 아닐 때
                dic2[v] = max(max(dp[0:v]) + 1, dp[v])  # 왼쪽에 있는 수 중 가장 큰 값 +1과 현 위치의 값 중 비교해 더 큰 값을 선택
            else:       # v가 0일 때
                dic2[0] = 1
        for v in v_arr: # 값을 한꺼번에 바꿔준다.
            dp[v] = dic2[v]

print(max(dp))  # 가장 큰 값 출력