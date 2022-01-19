def countdown(num):
    if num > 0:
        for i in range(num,0,-1):
            print(i)
    else:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')

countdown(0)
countdown(10)