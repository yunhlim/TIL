# 시간 초과...
# X = int(input())
# cnt = 0
# def check_three(num):
#     global cnt
#     if num < 10:
#         print(cnt)
#         if num % 3: print('NO')
#         else: print('YES')
#     else: 
#         cnt += 1
#         num = sum(map(int,str(num)))
#         return check_three(num) 
# check_three(X)

def check_three(string,cnt):
    if len(string) == 1:
        if int(string) % 3: print(f'{cnt}\nNO')
        else: print(f'{cnt}\nYES')
    else: 
        cnt += 1
        num = str(sum(map(int,string)))
        return check_three(num,cnt) 
check_three(input(),0)