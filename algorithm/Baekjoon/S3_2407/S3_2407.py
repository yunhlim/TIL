n , m = map(int, input().split())   # nCm의 입력 n과 m
if n-m < m: # nCm에서 m이 n의 절반보다 클 경우 n-m으로 바꾼다.
    m = n-m

up_lst = [n-i for i in range(m)]    # 분자를 리스트에 하나씩 담는다.
down_lst = [i for i in range(1, m+1)] # 분모를 리스트에 담는다.
sosu_lst = []   # m이하의 소수를 찾아 담는다.
sosu_cnt_lst = [0 for _ in range(m+1)]    # 인덱스 맞춰 0~m까지의 소수 개수 초기화
result = 1

def sosu(num): # num이하의 소수를 찾는 함수
    if num > m: # 숫자가 m보다 큰 값이 나오면 안 찾는다.
        return
    for i in range(2, num):
        if num % i == 0:
            break
    else: sosu_lst.append(num)
    return sosu(num+1)

def sosu_cnt(num):  # 소수의 개수를 찾아주는 함수
    if num > m: # 숫자가 m보다 큰 값이 나오면 안 찾는다.
        return
    new_num = num
    for sosu in sosu_lst:
        if new_num == 1:
            break    
        while new_num % sosu == 0:  # 위에서 구한 소수로 나누어 개수를 찾는다.
            new_num = new_num//sosu
            sosu_cnt_lst[sosu] += 1
    return sosu_cnt(num+1)

sosu(2)
sosu_cnt(2)

for i in range(2, m+1): # 분모의 소수를 순서대로 가져와서 분자와 나누어 준다.
    if sosu_cnt_lst[i] != 0:   # 소수이고 나눌 수 있는 횟수가 있으면 반복문으로 들어온다.
        for j in range(len(up_lst)):
            while (sosu_cnt_lst[i] != 0) and (up_lst[j] % i == 0):  # 나누어지는지, 나눌 수 있는 수가 있는지 확인
                up_lst[j] = up_lst[j] // i
                sosu_cnt_lst[i] -= 1

for num in up_lst:
    result *= num

print(result)