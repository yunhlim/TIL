import sys
input = sys.stdin.readline


def seg_init(s, e, node):                       # 세그먼트 트리 초기 설정
    if s == e:
        tree[node] = arr[s]
    else:
        mid = (s + e) // 2
        tree[node] = (seg_init(s, mid, node * 2) * seg_init(mid + 1 , e, node * 2 + 1)) % m
    return tree[node]


def seg_update(s, e, node):  # 세그먼트 트리 업데이트
    if not(s <= target <= e):
        return
    tree[node] = tree[node] // arr[target] * new_value
    if s != e:
        mid = (s + e) // 2
        seg_update(s, mid, node * 2)
        seg_update(mid + 1 , e, node * 2 + 1)


def seg_print(s, e, node):     # 구간 곱 출력
    if left <= s and right >= e:        # 포함하는 수일 때
        return tree[node]
    elif e < left or s > right:         # 포함하지 않는 경우
        return 1
    else:                               # 걸치는 경우
        mid = (s + e) // 2
        tree[node] = (seg_print(s, mid, node * 2) * seg_print(mid + 1 , e, node * 2 + 1)) % m
        return tree[node]


m = 1_000_000_007       # 나눈 값을 출력한다.
n, m, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]
for i in range(1, n + 1):   # 입력이 1부터 n 인덱스로 들어온다.
    arr[i] = int(input())

tree = [0 for _ in range(n * 4)]
seg_init(1, n, 1)
print(tree)
for i in range(m + k):
    a, b, c = map(int, input().split())
    print(tree)
    if a == 1:  # 변경
        target = b
        new_value = c
        seg_update(1, n, 1)
        arr[b] = c
    else:       # 출력
        left = b
        right = c
        print(seg_print(1, n, 1))