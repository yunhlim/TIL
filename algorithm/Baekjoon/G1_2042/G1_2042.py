import sys
input = sys.stdin.readline


def seg_init(s, e, index):      # 구간합을 구하는 함수
    if s == e:                  # s, e가 같은 경우는 그 때의 배열의 값을 return
        tree[index] = arr[s]
        return tree[index]
    mid = (s + e) // 2          # 중간 값 구하기
    left = seg_init(s, mid, index * 2)              # index * 2는 왼쪽
    right = seg_init(mid + 1, e, index * 2 + 1)     # index * 2 + 1은 오른쪽
    tree[index] = left + right
    return tree[index]


def seg_update(s, e, index):
    if s == e:
        tree[index] = arr[s]
        return tree[index]
    mid = (s + e) // 2
    left = seg_init(s, mid, index * 2)
    right = seg_init(mid + 1, e, index * 2 + 1)
    tree[index] = left + right
    return tree[index]

    
n, m, k = map(int, input().split())     # n: 수의 개수, m: 수의 변경 횟수, k: 구간의 합 구하는 횟수
arr = [0]   # 인덱스를 1부터 시작하게 하기 위함
for _ in range(n):
    arr.append(int(input()))
tree = [0 for _ in range(4 * n)]
seg_init(1, n, 1)
print(tree)