number = int(input())

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)
        
print(factorial(number))

# for 문 사용!
# number = int(input())
#
# def factorial(num):
#     result = 1
#     for i in range(1,num+1):
#         result *= i
#     return result
#
# print(factorial(number))