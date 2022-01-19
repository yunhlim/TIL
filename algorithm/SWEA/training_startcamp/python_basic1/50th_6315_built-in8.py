nums = list(range(1,11))

def evens(numbers):
    return list(map(lambda x: x**2, numbers))

print(evens(nums))