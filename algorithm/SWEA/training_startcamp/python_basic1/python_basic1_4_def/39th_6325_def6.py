numlist = [2, 4, 6, 8, 10]

def num_search(num, nums):
    if num in nums:
        print(f'{num} => True')
    else:
        print(f'{num} => False')

print(numlist)
num_search(5,numlist)
num_search(10,numlist)