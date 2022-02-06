import sys
input = sys.stdin.readline  # 입력이 100000까지 들어온다.

N = int(input())
lst = []
for i in range(N):  # 나이와 이름을 tuple로 담는데 나이는 정수형으로 변환
    age, name = input().split()
    lst.append((int(age), name))

lst.sort(key=lambda x: x[0]) # tuple의 0번째 인덱스로 정렬

for i in range(N):
    print(*lst[i])  # 언팩연산자로 tuple의 ()제거 후 출력