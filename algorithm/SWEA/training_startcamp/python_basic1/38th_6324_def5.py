# 처음 생각했던 방법

# numbers = [1, 2, 3, 4, 3, 2, 1]

# def only_numbers(numbers):
#     only_nums = [numbers[0]]
#     if numbers[0] != numbers[1]:
#         only_nums.append(numbers[1])
#     for i in range(2, len(numbers)-1):
#         same = 0 
#         for j in range(0, i):
#             if numbers[i] == numbers[j]:
#                 same = 1
#                 break
#         if same == 0:
#             only_nums.append(numbers[i])
#     return only_nums

# print(numbers)
# print(only_numbers(numbers))

#------------------------------------------------

# set 사용

# numbers = [1, 2, 4, 3, 3, 2, 1]

# print(numbers)
# print(list(set(numbers)))

#------------------------------------------------

# 리스트와 값을 비교하는 방법 사용

numbers = [1, 2, 3, 4, 3, 2, 1]

def only_numbers(nums):
    only_nums = []
    for i in nums:
        if i not in only_nums:
            only_nums.append(i)
    return only_nums

print(numbers)
print(only_numbers(numbers))