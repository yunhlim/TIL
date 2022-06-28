n = int(input())        # 숫자 카드 개수
arr = list(map(int, input().split()))
visited = {}            # 딕셔너리로 선언
for x in arr:
    visited[x] = visited.get(x, 0) + 1      # 숫자 카드 개수를 더해준다.

m = int(input())        # 확인해볼 수
arr = list(map(int, input().split()))
result = []
for x in arr:
    result.append(visited.get(x, 0))        # result 배열에 출력할 값을 담아준다.

print(*result)