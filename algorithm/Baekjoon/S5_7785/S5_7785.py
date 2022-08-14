import sys
input = sys.stdin.readline

n = int(input())

company = set()
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        company.add(name)
    else:
        company.remove(name)

for person in sorted(list(company), reverse=True):
    print(person)
