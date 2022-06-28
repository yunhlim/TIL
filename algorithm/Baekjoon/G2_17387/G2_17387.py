def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - \
        (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2 = [x1, y1], [x2, y2]
p3, p4 = [x3, y3], [x4, y4]

p12 = ccw(p1, p2, p3) * ccw(p1, p2, p4)  # p1, p2 선분으로 p3과 p4에 대한 ccw의 곱
p34 = ccw(p3, p4, p1) * ccw(p3, p4, p2)  # p3, p4 선분으로 p1과 p2에 대한 ccw의 곱
if p12 <= 0 and p34 <= 0:   # 두 선분이 교차하는 경우(한 직선 위에 있을 때 생각!)
    if p12 == 0 and p34 == 0:   # 두 선분이 같은 라인에 있을 때
        p1, p2 = min(p1, p2), max(p1, p2)
        p3, p4 = min(p3, p4), max(p3, p4)
        if p3 <= p2 and p1 <= p4:       # 두 선분이 만나는 경우
            print(1)
            exit()
    else:
        print(1)
        exit()
print(0)        # 나머지는 교차하지 않는다.