star = '*'
cnt = 7
while True:
    if cnt > 0:
        print(f'{star*cnt:^7}')
    else:
        break
    cnt -= 2