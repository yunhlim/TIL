nums = list(range(1,11))

def evens(nums):
    return list(filter(lambda n: n % 2 == 0, nums))
    
print(evens(nums))