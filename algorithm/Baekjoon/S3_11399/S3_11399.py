n = int(input())
arr = list(map(int, input().split()))
arr.sort()      # 정렬
time = arr[0]
for i in range(1, n):  
    arr[i] += arr[i-1]  # 누적합
    time += arr[i]      # 누적합 시키면서 누적합의 결과를 time에 더한다.
print(time)