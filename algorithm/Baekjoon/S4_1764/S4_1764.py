import sys

n, m = map(int, input().split())    # 듣도 못한 사람의 수 n, 보도 못한 사람의 수 m
n_set = set()   # 듣도 못한 사람들을 담을 set
m_set = set()   # 보도 못한 사람들을 담을 set
result = []     # 듣보잡들을 담을 list

for i in range(n):  # 듣도 못한 사람들을 담는다.
    n_set.add(sys.stdin.readline().rstrip())

for i in range(m):  # 보도 못한 사람들을 담는다.
    m_set.add(sys.stdin.readline().rstrip())

result = list(n_set & m_set)    # set의 교집합 연산자를 사용한다.
result.sort()                   # 사전순으로 정렬
print(len(result))              # 듣보잡들의 수 출력
for name in result:             # 듣보잡들을 출력
    print(name)