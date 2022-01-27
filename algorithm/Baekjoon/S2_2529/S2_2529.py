k = int(input())
lst_sign = input().split() # > < 를 나눠서 받는다.
lst = [-1 for _ in range(k+1)] # 출력 배열
success = False

def up_recur(cur):
    global success
    for i in range(0,k+1):  # index 0 부터 순서대로 넣어준다. 길이가 5면 0~4 숫자로 무조건 만들 수 있다.
        if cur == 0:    # 첫자리는 부등호 비교할 필요 없다. 중복된 수도 비교할 필요 X
            lst[cur] = i
            up_recur(cur+1)
        else:
            if i not in lst: # 앞에 나왔던 숫자에 중복되는지 확인한다.
                if (lst_sign[cur-1] == '<' and lst[cur-1] < i) or (lst_sign[cur-1] == '>' and lst[cur-1] > i):
                    lst[cur] = i
                    if cur == k:
                        success = True  # 가장 최근에 만들어진 하나만 출력하게 해주기 위해 사용
                        print(*lst) # lst를 언팩연산자를 활용해 제거 후 출력
                    up_recur(cur+1)
                    if success: # 완성된 것이 있으면 나머지 재귀함수들은 없앤다.
                        break
                    lst[cur] = -1   # 다음 자릿 수를 순차적으로 돌며 막히면 자릿 수를 다시 수정해준다.
        

up_recur(0) # index 0의자리부터 순차적으로 출력