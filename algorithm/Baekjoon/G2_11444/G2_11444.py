def matrix_s(m):            # 행렬 곱, 입력에는 초기 행렬이나, 현재 결과 행렬만 들어온다.
    a, b = result_arr[0]    # 결과행렬이 들어오는 경우는 제곱, 아니면 곱이다.
    c, d = result_arr[1]
    e, f = m[0]
    g, h = m[1]
    result_arr[0][0] = (a * e + b * g) % 1_000_000_007
    result_arr[0][1] = (a * f + b * h) % 1_000_000_007
    result_arr[1][0] = (c * e + d * g) % 1_000_000_007
    result_arr[1][1] = (c * f + d * h) % 1_000_000_007


def recur(n):   # 거듭제곱 분할정복
    if n == 1:
        return

    if n // 2:
        recur(n // 2)
        matrix_s(result_arr)   # 제곱 연산

    if n % 2:
        matrix_s(first_arr) # 그냥 곱 연산


n = int(input())
first_arr = [[1, 1], [1, 0]]       # 초기 행렬
result_arr = [[1, 1], [1, 0]]      # 결과 행렬
recur(n - 1)
print(result_arr[0][0] % 1_000_000_007)