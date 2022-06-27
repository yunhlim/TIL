import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def tree_create(s, e, node):            # 세그먼트 트리에 최소값 담기
    if s == e:
        tree[node] = (arr[s], s)        # 최소값과 그 때의 인덱스를 담아준다.
        return tree[node]
    mid = (s + e) // 2
    left = tree_create(s, mid, node * 2)
    right = tree_create(mid + 1, e, node * 2 + 1)
    tree[node] = min(left, right)       # 최소값을 세그먼트 트리에 담아준다.
    return tree[node]


def tree_search(s, e, node, left, right):       # 세그먼트 트리로 최소값과 그 떄의 인덱스 찾기
    if left <= s and right >= e:        # 범위 안에 있는 경우
        return tree[node]
    if e < left or s > right:           # 범위 밖에 있는 경우
        return [INF, 0]
    # 범위가 걸쳐져 있는 경우
    mid = (s + e) // 2
    l = tree_search(s, mid, node * 2, left, right)
    r = tree_search(mid + 1, e, node * 2 + 1, left, right)
    if l[0] <= r[0]:            # 더 작은 값을 
        return l
    else:
        return r


def max_histogram(s, e):            # 히스토그램의 최대 직사각형 넓이 구하기
    global result
    min_val, min_idx = tree_search(1, n, 1, s, e)       # 최소값과 그 때의 인덱스 값
    result = max(result, min_val * (e - s + 1))
    if s != min_idx:
        max_histogram(s, min_idx - 1)
    if e != min_idx:
        max_histogram(min_idx + 1, e)


INF = 10000000000
while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break
    tree = [0] * n * 4      # 세그먼트 트리 초기화
    tree_create(1, n, 1)
    result = 0
    max_histogram(1, n)
    print(result)