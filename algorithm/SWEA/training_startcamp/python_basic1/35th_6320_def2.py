user1 = input()
user2 = input()
user1rps = input()
user2rps = input()

def rps(a,b) :
    if a == "가위":
        if b == "가위":
            print('비겼습니다!')
        elif b == "바위":
            print('바위가 이겼습니다!')
        else :
            print('가위가 이겼습니다!')
    if a == "바위":
        if b == "가위":
            print('바위가 이겼습니다!')
        elif b == "바위":
            print('비겼습니다!')
        else :
            print('보가 이겼습니다!')
    if a == "보":
        if b == "가위":
            print('가위가 이겼습니다!')
        elif b == "바위":
            print('보가 이겼습니다!')
        else :
            print('비겼습니다!')

rps(user1rps,user2rps)      