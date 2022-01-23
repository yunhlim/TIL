import sys

def un_zip(string):
    start_i = 0
    last_i = 0
    un_zip_str_len = 0
    cnt = 0
    open_i = 0
    close_i = 0
    for i, v in enumerate(string):  # ()를 찾아준다.
        if v == '(':    # index 순서대로 찾으며 (가 새로 들어올 때마다 저장
            start_i = i
        elif v == ')':  # )를 만나면 그 때를 last_i에 담고 break
            last_i = i
            break
    if start_i == 0:    # ()가 없을 때 조건문을 읽는다. 마지막 답 구할 때 사용
        if '<' in string:      # <, >를 찾아 안에 값은 숫자로 더해준다.
            for i,v in enumerate(string):
                if v == '<':
                    open_i = i
                    un_zip_str_len += cnt
                    cnt = 0
                elif v == '>':
                    close_i = i
                    un_zip_str_len += int(string[open_i+1:close_i])
                    cnt = 0
                else : cnt += 1 # < > 이외에 있는 값들은 갯수로 센다.
            un_zip_str_len += cnt
        else: 
            un_zip_str_len = len(string)
        return un_zip_str_len
    
    if '<' in string[start_i+1:last_i]: # ()가 있을 땐 여기로 들어온다.
        un_zip_str = string[start_i+1:last_i]
        for i, v in enumerate(un_zip_str):
            if v == '<':
                open_i = i
                un_zip_str_len += cnt
                cnt = 0
            elif v == '>':
                close_i = i
                un_zip_str_len += int(un_zip_str[open_i+1:close_i])
                cnt = 0
            else : cnt += 1
        un_zip_str_len += cnt
        un_zip_str_len *= int(string[start_i-1])
    else : un_zip_str_len = int(string[start_i-1])*(last_i - start_i-1)
    
    new_str = string[:start_i-1] + '<'+ str(un_zip_str_len) + '>' + string[last_i+1:]
    return un_zip(new_str) # 재귀

print(un_zip(sys.stdin.readline().strip()))

