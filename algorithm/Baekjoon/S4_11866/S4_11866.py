N, K = map(int, input().split())
circle = list(range(1,N+1)) # 1~N으로 이루어진 리스트
result = [] # 결과를 담을 요세푸스 순열

index = 0   # 첫번째 순서
for i in range(N,0,-1):
    index += K-1    # K번째를 제거해야 하니 K-1을 더한다.
    index %= i  # 현재 사람 수로 나머지 연산을 통해 제거할 인덱스를 정확히 찾는다.
    result.append(circle.pop(index))

print(f'<{", ".join(map(str,result))}>')    # join과 map함수로 문자열의 모양을 원하는 출력 형태로 바꾼다.