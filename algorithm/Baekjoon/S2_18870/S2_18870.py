n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))	# set로 중복을 제거하고 정렬한다.
dic = {}

for k, v in enumerate(arr2):	# enumerate의 인덱스와 값을 각각 딕셔너리의 값과 key에 매칭해준다.
    dic[v] = k
    
for i in range(n):			# 입력받았던 배열을 딕셔너리를 활용해 바꾸어준다.
    arr[i] = dic[arr[i]]

print(*arr)



# 1차 풀이
# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n):	# 값과 인덱스를 리스트로 묶어 2차원으로 넣어준다.
#     arr[i] = [arr[i], i]

# arr.sort()			# 배열을 값으로 정렬한다.

# prev = arr[0][0]	# 이전의 값 저장
# cnt = 0				# 바꿀 값
# arr[0][0] = cnt		# 0번째 값을 바꾸어준다.
# for i in range(1, n):
#     if arr[i][0] == prev:	# 이전의 값과 같을 땐 같은 값을 넣어준다.
#         arr[i][0] = cnt
#     else:				# 다를 땐 1을 더한 값을 넣어준다.
#         cnt += 1
#         prev = arr[i][0]	# 비교할 이전 값을 바꾸어준다.
#         arr[i][0] = cnt
        

# arr.sort(key=lambda x : x[1])	# 다시 인덱스 순으로 정렬한다.
# result = []
# for i in range(n):				# 값으로만 프린트하기 위해 result에 다시 담아준다.
#     result.append(arr[i][0])

# print(*result)
