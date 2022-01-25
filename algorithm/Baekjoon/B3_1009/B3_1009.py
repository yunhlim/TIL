T = int(input())    # 테스트 케이스 개수 T
a_b_lst = []    # a,b를 리스트에 담을 빈 배열
for i in range(T):  # [a,b]를 담은 2차원 리스트를 만든다.
    a_b_lst.append(list(map(int,input().split())))


def last_num(a, b): # 마지막 숫자를 수행해주는 프로그램
    result = 1  # 한번 곱할 때마다 바꿔줄 1의 자리 수
    small_a = a % 10    # a가 두 자리까지 들어오니 1의자리 남기고 버린다
    small_b = b % 100 # b의 수를 줄인다. 4의배수, 2의배수, 1의배수로 반복되니 100으로 우선 나눈다.
    if small_a in [0, 1, 5, 6]: # 0,1,5,6은 몇 번 곱해도 그대로니 그대로 출력
        if small_a == 0: print(10)  # 0이 나오면 10번째 컴퓨터가 이용하는거니까 10을 더한다.
        else: print(small_a)
        return
    elif small_a in [2, 3, 7, 8]: 
        small_b = b % 4   # 2,3,7,8은 4개 씩 반복되니 4로 나눈 나머지로 줄인다.
        if small_b == 0: small_b = 4
    else: 
        small_b = b % 2   # 4, 9는 2개 씩 반복되니 2로 나눈 나머지로 줄인다.
        if small_b == 0: small_b = 2
    result = (small_a**small_b) % 10
    if result == 0: print(10)
    else: print(result)

for i in range(T):  # [a,b] 가 T개 있으니 for문으로 순회
    last_num(*a_b_lst[i])    # 입력받은 [a,b]리스트를 언팩 연산자를 활용해 입력으로 넣어 실행한다.