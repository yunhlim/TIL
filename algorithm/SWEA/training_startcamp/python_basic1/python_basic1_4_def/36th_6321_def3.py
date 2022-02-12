a=int(input())

def sosu(a) :
    cnt = 1
    while True:
        cnt += 1
        if cnt == a :
            print("소수입니다.")
            break
        if a % cnt == 0 :
            print("소수가 아닙니다.")
            break
sosu(a)