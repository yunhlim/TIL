def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - \
        (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])


def cross():
    if x1 == x2:    # 첫번째 선분이 y축과 평행할 때(기울기가 무한)
        m2 = (y4 - y3) / (x4 - x3)      # 두번째 선분의 기울기
        k2 = y3 - m2 * x3               # 두번째 선분의 y절편
        cross_y = m2 * x1 + k2
        cross_x = x1
    elif x3 == x4:  # 두번째 선분이 y축과 평행할 때(기울기가 무한)
        m1 = (y2 - y1) / (x2 - x1)      # 첫번째 선분의 기울기
        k1 = y1 - m1 * x1               # 첫번째 선분의 y절편
        cross_y = m1 * x3 + k1
        cross_x = x3
    else:
        m1 = (y2 - y1) / (x2 - x1)      # 첫 선분의 기울기
        m2 = (y4 - y3) / (x4 - x3)      # 두번째 선분의 기울기

        k1 = y1 - m1 * x1               # 첫 선분의 y절편
        k2 = y3 - m2 * x3               # 두번째 선분의 y절편
        cross_x = (k2 - k1) / (m1 - m2)     # 두 직선의 교차점의 x 좌표
        cross_y = m1 * cross_x + k1
    return cross_x, cross_y



x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2 = [x1, y1], [x2, y2]
p3, p4 = [x3, y3], [x4, y4]

p12 = ccw(p1, p2, p3) * ccw(p1, p2, p4)  # p1, p2 선분으로 p3과 p4에 대한 ccw의 곱
p34 = ccw(p3, p4, p1) * ccw(p3, p4, p2)  # p3, p4 선분으로 p1과 p2에 대한 ccw의 곱
if p12 <= 0 and p34 <= 0:   # 두 선분이 교차하는 경우(한 직선 위에 있을 때 생각!)
    if p12 == 0 and p34 == 0:   # 두 선분이 한 점에서 만나거나 겹칠 때
        p1, p2 = min(p1, p2), max(p1, p2)
        p3, p4 = min(p3, p4), max(p3, p4)
        if p3 <= p2 and p1 <= p4:       # 두 선분이 만나는 경우
            if ccw(p1, p2, p3) == 0 and ccw(p1, p2, p4) == 0:   # 두 선분이 겹칠 때(한 점에서 안 만나야 한다.)
                if p3 == p2:    # p3와 p2 한 점에서 만날 때
                    print(1)
                    print(*p2)
                    exit()
                if p1 == p4:    # p1과 p4 한 점에서 만날 때
                    print(1)
                    print(*p1)
                    exit()
                print(1)        # 두 선분이 여러 점에서 겹칠 때
                exit()
            print(1)            # 두 선분이 한 점에서 만날 때(기울기가 다름)
            print(*cross())
            exit()
    else:
        print(1)
        print(*cross())
        exit()
print(0)        # 나머지는 교차하지 않는다.