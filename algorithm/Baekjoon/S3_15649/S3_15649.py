n,m = map(int, input().split())

arr = [0 for i in range(m)]
visited = [False for i in range(n)] # 중복된 순열이 나오지 않게 사용된 숫자인지 확인!

def recur(cur): # 순열의 첫자리부터 채워준다.
    if cur == m:
        print(*arr) # 순열이 완성되면 프린트한다.
        return
    else:
        for i in range(n):  # 자리마다 모든 경우의 수를 넣어주기 위해 for문에 재귀함수를 넣는다.
            if visited[i] == True:
                continue
            else:
                arr[cur] = i+1
                visited[i] = True
                recur(cur+1)
                visited[i] = False

recur(0)