n, m = map(int, input().split())
memories = list(map(int, input().split()))
fees = list(map(int, input().split()))
dp = [[0] * n for _ in range(m + 1)]

