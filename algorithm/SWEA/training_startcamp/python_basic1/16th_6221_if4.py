man1 = input()
man2 = input()
if man1 == '바위':
    if man2 == '바위':
        print("Result : Draw")
    elif man2 == '가위':
        print("Result : Man1 Win!")
    elif man2 == '보':
        print("Result : Man2 Win!")
elif man1 == '가위':
    if man2 == '바위':
        print("Result : Man2 Win!")  
    elif man2 == '가위':
        print("Result : Draw")  
    elif man2 == '보':
        print("Result : Man1 Win!")
elif man1 == '보':
    if man2 == '바위':
        print("Result : Man1 Win!")
    elif man2 == '가위':
        print("Result : Man2 Win!")
    elif man2 == '보':
        print("Result : Draw")