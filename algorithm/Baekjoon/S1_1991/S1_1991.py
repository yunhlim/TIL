def pre_order(v):	# 전위순회
    if v:
        return chr(v + ord('A') - 1) + pre_order(arr[v][0]) + pre_order(arr[v][1])
    else:
        return ''
        
        
def in_order(v):	# 중위순회
    if v:
        return in_order(arr[v][0]) + chr(v + ord('A') - 1) + in_order(arr[v][1])
    else:
        return ''
        
        
def post_order(v):	# 후위순회
    if v:
        return post_order(arr[v][0]) + post_order(arr[v][1]) + chr(v + ord('A') - 1)
    else:
        return ''



n = int(input())
arr = [[0, 0] for _ in range(n + 1)]

for i in range(n):
    par, left, right = map(lambda x: ord(x) - ord('A') + 1 if x != '.' else 0, input().split())
    arr[par][0] = left
    arr[par][1] = right

print(pre_order(1))
print(in_order(1))
print(post_order(1))