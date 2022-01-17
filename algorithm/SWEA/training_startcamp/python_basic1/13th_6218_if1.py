var = int(input())
div = 1
while True:
    if var % div == 0:
        print(f'{div}(은)는 {var}의 약수입니다.')
    if div == var:
        break
    else:
        div += 1