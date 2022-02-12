a,b = input().split(', ')

def long_str(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        print("길이가 같습니다.")

print(long_str(a,b))