while True:
    nums = sorted(map(int,input().split())) # 입력된 세가지 정수를 순서대로 정렬
    if nums[0] == 0:    # 0을 만나면 break
        break
    else:
        if (nums[2] ** 2) == (nums[0] ** 2) + (nums[1] ** 2):
            print('right')
        else: print('wrong')