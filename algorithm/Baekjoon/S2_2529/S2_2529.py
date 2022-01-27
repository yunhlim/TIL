k = int(input())
lst_sign = input().split() # > < 를 나눠서 받는다.
lst = [-1 for _ in range(k+1)] # 출력 배열
success = False

def up_recur(cur):

    for i in range(0,k+1):  # index 0 부터 순서대로 넣어준다. 길이가 5면 0~4 숫자로 무조건 만들 수 있다.
        if cur == 0:    # 첫자리는 부등호 비교할 필요 없다. 중복된 수도 비교할 필요 X
            lst[cur] = i
            up_recur(cur+1)
        else:
            if i not in lst: # 앞에 나왔던 숫자에 중복되는지 확인한다.
                if (lst_sign[cur-1] == '<' and lst[cur-1] < i) or (lst_sign[cur-1] == '>' and lst[cur-1] > i):
                    lst[cur] = i
                    if cur == k:
                        success == True
                        return lst
                    up_recur(cur+1)
                    if success:
                        break
                    lst[cur] = -1
        

print(up_recur(0))