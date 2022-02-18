N, M = map(int, input().split())
# e가 1 더해지고 호출하니 배열을 넘칠 수 있다. 그래서 padding을 활용한다.
arr = list(map(int, input().split())) + [0] 
s = e = cnt = 0
sum = arr[0]
while e < N:    # e가 넘치면 종료
    if sum <= M:    # M보다 작거나 같을 때 e 증가, 같을 때는 s를 증가시키든 상관없다.(둘 다 증가시켜도 된다.)
        if sum == M:
            cnt += 1
        e += 1
        sum += arr[e]   # e가 배열을 넘어가면 한번 참조하긴 해야해서 위에 패딩을 넣어주었다.
    else:
        sum -= arr[s]
        s += 1
print(cnt)