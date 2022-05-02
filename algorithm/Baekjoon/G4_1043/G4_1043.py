def find(x):
    if x != par[x]:
        par[x] = find(par[x])       # 경로압축
    return par[x]


def union(a, b):
    a = par[a]
    b = par[b]
    if a in trues:      # 진실을 아는 사람이 부모가 되는 방향으로 합친다.
        par[b] = a
    else:
        par[a] = b


n, m = map(int, input().split())
trues = list(map(int, input().split()))     # 진실을 아는 사람들
arr = [list(map(int, input().split())) for _ in range(m)]
par = [i for i in range(n + 1)]
cnt = m         # 모든 파티에 참석하는 경우를 default로

if trues[0]:
    trues = trues[1:]
    for i in range(m):
        if arr[i][0] == 1:      # 파티에 혼자 참석하는 경우
            continue
        for j in range(2, len(arr[i])):     # 각각의 파티원들을 하나의 합집합으로 연결한다.
            if find(arr[i][1]) == find(arr[i][j]):      # 이미 같은 집합에 속해있는 경우
                continue
            union(arr[i][1], arr[i][j])     # 첫번째 사람과 나머지 사람들을 한 번씩 연결한다.
    
    for i in range(m):          # 파티를 다시 순회하며 진실을 아는 사람들의 집합에 속해있는 지 확인
        if find(arr[i][1]) in trues:    # 어차피 다 합집합으로 연결되어있으니 한 명만 파악하면 된다.
            cnt -= 1

print(cnt)      # 갈 수 있는 파티의 개수를 출력한다.