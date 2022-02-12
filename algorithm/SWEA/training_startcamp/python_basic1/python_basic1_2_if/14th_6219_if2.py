var = int(input())
div = 1
cnt = 0
while True:
    if var % div == 0:
        print(f'{div}(은)는 {var}의 약수입니다.')
        cnt += 1
    if div == var:
        if cnt == 2:
            print(f'{div}(은)는 1과 {var}로만 나눌 수 있는 소수입니다.')
        break
    else:
        div += 1