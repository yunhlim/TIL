nums = list(range(1,11))

def evens_double(numbers):
    result = numbers
    result = list(filter(lambda x: x%2==0, result))
    return list(map(lambda x: x**2, result))

print(evens_double(nums))