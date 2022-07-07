import sys
input = sys.stdin.readline


def recur(cur):
    if not tree.get(cur):
        return

    for food in tree[cur]:
        print((len(cur) - 1) * '--' + food)
        recur(cur + (food,))


n = int(input())
tree = {}

for _ in range(n):
    temp = list(input().split())
    prv = ('root',)   # key가 0인 경우
    for food in temp[1:]:
        cur = food
        tree[prv] = tree.get(prv, set())
        tree[prv].add(cur)
        prv = prv + (cur,)

for c in tree:
    tree[c] = sorted(list(tree[c]))

recur(('root',))