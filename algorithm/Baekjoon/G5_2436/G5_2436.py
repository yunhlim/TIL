# N, M = map(int, input().split())            # N 최대공약수, M 최소공배수

# if N == M:                                  # N, M이 같을 때 입력 그대로 출력한다.
#     print(N, N)
# else:
#     constant = M//N                         # 최대 공배수에서 최소 공배수를 나눈다.
#     div_num = constant                      # 약수 구하면서 값이 바뀌니 다른 변수에 저장
#     div_lst = []        # 약수의 짝을 튜플로 담을 리스트
#     for i in range(1, div_num):
#         if i * i > div_num:                 # 제곱근 이상의 약수는 구할 필요 없다.
#             break
        
#         if div_num % i == 0:                # 약수 구하기, 약수의 짝을 항상 생각한다.
#             if i * i == div_num:            # 제곱수일 때 처리해준다.
#                 div_lst.append((i,i))       
#             else: div_lst.append((i,constant//i))   # i에 더 작은 값이 들어간다.

#     each_other_lst = []      # 서로소 약수 짝을 튜플로 담을 리스트
#     for i in range(len(div_lst)):           # 유클리드 호제법으로 서로소인지 구하기
#         a, b = div_lst[i]                   # 약수를 담은 리스트에서 tuple 하나씩 가져온다.
#         while a % b != 0:                   # 두 수의 최대 공약수를 구해준다.
#             a, b = b, a % b                 # a가 b로 나누어 떨어지는 순간 출력되는 b가 최대 공약수이다.
#         if b == 1:                          # 최대 공약수가 1일 때가 서로소이다.
#             each_other_lst.append(div_lst[i])

#     a = each_other_lst[0][0]
#     b = each_other_lst[0][1]
#     min = a + b                             # a + b값을 서로소 리스트의index 0 값으로 초기화

#     for x, y in each_other_lst:
#         if min > x + y:                     # 합이 더 작을 때 a, b에 담아준다.
#             min = x + y
#             a = x
#             b = y

#     print(a*N, b*N)     # A, B는 a*N, b*N이니 다시 곱해서 출력한다.


# 제곱근을 구하고하면 조건문을 조금 도니까 속도 개선에 큰 영향을 미치나 테스트
# N, M = map(int, input().split())            # N 최대공약수, M 최소공배수

# constant = M//N                         # 최대 공배수에서 최소 공배수를 나눈다.
# div_num = constant                      # 약수 구하면서 값이 바뀌니 다른 변수에 저장
# sqrt_constant = constant ** (0.5)
# sqrt_constant = int(sqrt_constant)

# for i in range(1, sqrt_constant+1):
    
#     if div_num % i == 0:                # 약수 구하기, 약수의 짝을 항상 생각한다.
#         x = i
#         y = constant//i
#         while x % y != 0:                   # 두 수의 최대 공약수를 구해준다.
#             x, y = y, x % y                 # a가 b로 나누어 떨어지는 순간 출력되는 b가 최대 공약수이다.
#         if y == 1:                          # 최대 공약수가 1일 때가 서로소이다.
#             a = i
#             b = constant//i

# print(a*N, b*N)     # A, B는 a*N, b*N이니 다시 곱해서 출력한다.

N, M = map(int, input().split())
constant = M//N
div_num = constant
for i in range(1, div_num+1):
    if i * i > div_num:
        break
    if div_num % i == 0:
        x = i
        y = constant//i
        while x % y != 0:
            x, y = y, x % y
        if y == 1:
            a = i
            b = constant//i
print(a*N, b*N)