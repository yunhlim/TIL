import sys

n, m = map(int, input().split())
arr = [0]   # 숫자를 입력 받아 문자를 출력하기 위한 리스트
dic = {}    # 문자를 입력받아 숫자를 출력하기 위한 리스트
for i in range(1, n+1):
    temp = sys.stdin.readline().rstrip()    # 도감을 입력 받는다.
    arr.append(temp)    # index값에 대한 입력 문자를 list에 넣어준다.
    dic[temp] = i       # key에는 입력 문자를 값에는 index를 입력해준다.
for _ in range(m):
    key = sys.stdin.readline().rstrip()     # 문제를 하나씩 꺼낸다.
    if key.isdigit():                       # 숫자가 나오면 list를 활용해 문자를 찾아준다.
        print(arr[int(key)])
    else:
        print(dic[key])                     # 문자가 나오면 dictionary를 활용해 index를 찾아준다.