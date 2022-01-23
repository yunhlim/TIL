import sys

def un_zip(string):
    start_i = 0
    last_i = 0
    un_zip_str_len = 0
    cnt = 0
    open_i = 0
    close_i = 0
    for i, v in enumerate(string):
        if v == '(':
            start_i = i
        elif v == ')':
            last_i = i
            break
    if start_i == 0:
        if '<' in string:      
            for i,v in enumerate(string):
                if v == '<':
                    open_i = i
                    un_zip_str_len += cnt
                    cnt = 0
                elif v == '>':
                    close_i = i
                    un_zip_str_len += int(string[open_i+1:close_i])
                    cnt = 0
                else : cnt += 1
            un_zip_str_len += cnt
        else: 
            un_zip_str_len = len(string)
        return un_zip_str_len
    
    if '<' in string[start_i+1:last_i]:
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
    return un_zip(new_str)

print(un_zip(sys.stdin.readline().strip()))
#start_i랑 open_i 다르게
# 너무 머리 아프다...