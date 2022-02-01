num1, num2 = map(int, input().split())

def max_gongyaksoo(num1, num2): # 최대공약수 구하기
    if num1 < num2: # 작은 수를 고른다
        small_num = num1
    else: small_num = num2

    for i in range(small_num,0,-1): # 작은 수에서 1씩 줄여가며 최대공약수를 찾는다.
        if (num1 % i == 0) and (num2 % i == 0):
            return i
    
def min_gongbaesoo(num1, num2): # 최소공배수 구하기
    num1_mul = num1
    num2_mul = num2
    while True:
        if num1_mul == num2_mul:
            return num1_mul
        elif num1_mul > num2_mul:
            num2_mul += num2
        else: num1_mul += num1

print(max_gongyaksoo(num1, num2))
print(min_gongbaesoo(num1, num2))