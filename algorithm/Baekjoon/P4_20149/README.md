# [Baekjoon] 20149. ์ ๋ถ ๊ต์ฐจ 3 [P4]

## ๐ ๋ฌธ์  : [์ ๋ถ ๊ต์ฐจ 3](https://www.acmicpc.net/problem/20149)

## ๐ ํ์ด

**CCW**๋ฅผ ์ด์ฉํด ๊ต์ฐจํ๋์ง ๊ตฌํ๋ค.

์ ๋ถ ๊ต์ฐจ1, 2์ ๋ค๋ฅธ ์ ์ ๊ต์ฐจ์ ์ ๊ตฌํ๋ ๊ฒ์ด๋ค.

์ด ๋ ํ ์ ์์ ๋ง๋๋ ๊ฒฝ์ฐ๋ฅผ CCW๋ก ๊ตฌํ๊ณ  ๊ทธ ๋๋ง ์ฐ๋ฆฝ ๋ฐฉ์ ์์ผ๋ก ํ๋์ ๊ต์ฐจ์ ์ ๊ตฌํ๋ฉด ๋๋ค.

๋ฐ๋ผ์ CCW๋ก ์ํ๋ฅผ ๋ถ๊ธฐ์ฒ๋ฆฌํ  ๋ ์ฌ๋ฌ ๊ฐ์ง๋ก ์๊ฐํด ๋๋ ์ผ ํ๋ค.

1. ๋ ์ ๋ถ์ด ๊ต์ฐจํ๋ ๊ฒฝ์ฐ(2, 3, 4์ ํด๋น X)
2. ๋ ์ ๋ถ์ด ์ ๋ถ์ ๋ ์ ์์ ๋ง๋๋ ๊ฒฝ์ฐ
3. ๋ ์ ๋ถ์ด ์ฌ๋ฌ ์ ์์ ๊ฒน์น๋ ๊ฒฝ์ฐ
4. ๋ ์ ๋ถ์ด ํ ์ง์  ์์ ์๋๋ฐ ํ๋์ ์ ์์ ๋ง๋๋ ๊ฒฝ์ฐ
5. ๋ ์ ๋ถ์ด ๋ง๋์ง ์๋ ๊ฒฝ์ฐ

๋จผ์  ๋ ์ ๋ถ์ด ๊ต์ฐจํ๋ ๊ฒฝ์ฐ๋ ๋ ์ ๋ถ์ CCW์ ๊ณฑ์ด ๋ค 0๋ณด๋ค ์๊ฑฐ๋ ๊ฐ์ผ๋ฉด ๋๋ค.

CCW์ ๊ณฑ์ด ๋ค 0์ผ ๋๋ ์ ๋์ ์์ ๋ง๋๊ฑฐ๋ ํ ์ ๋ถ ์์ ๋์ด๋ ๊ฒฝ์ฐ์ด๋ ๋ถ๊ธฐ์ฒ๋ฆฌ๋ก ๊ตฌ๋ถํด์ผ ํ๋ค.

`CCW(p1, p2, p3) == 0 and CCW(p1, p2, p4) == 0`์ ๋ง์กฑํ  ๋๋ ํ ์ง์  ์์ ๋์ผ ๋์ด๋ค.

์ด ๋ ์ฃผ์ํ  ์ ์ ๋ ์ ๋ถ์ด ์ผ์ง์  ์์ ๋์ฌ์์ผ๋ฉด์ ๋ง๋์ง ์๋ ๊ฒฝ์ฐ์ด๋ค.

- p1 < p2, p3 < p4๋ก ์ ๋ ์ ์ ์์๋ฅผ ์ ํด์ฃผ๊ณ , p3 <= p2์ p1 <= p4๋ฅผ ๋ง์กฑํ  ๋๋ง ๋ ์ ๋ถ์ด ๋ง๋๋ ๊ฒฝ์ฐ๋ค.
- ๋ฐ๋ผ์ ์ด์ ํด๋น๋์ง ์์ผ๋ฉด 0์ ์ถ๋ ฅํ๋ค.

๊ทธ๋ฆฌ๊ณ  p3์ p2๊ฐ ๊ฐ๊ฑฐ๋ p1๊ณผ p4๊ฐ ๊ฐ์ผ๋ฉด ํ ์ ์์ ๋ง๋๋ ๊ฒฝ์ฐ์ด๋ ๊ต์ฐจ์ ๋ ์ถ๋ ฅํด์ผ ํ๋ค.



๊ต์ฐจ์ ์ ๊ตฌํ  ๋ ์ฐ๋ฆฝ๋ฐฉ์ ์์ ์ฌ์ฉํด ํด๊ฒฐํ๋ค.

๊ธฐ์ธ๊ธฐ๋ฅผ ๊ตฌํ๊ณ  y์ ํธ์ ๊ตฌํด ๊ต์ฐจ์ ์ ์ถ๋ ฅํ๋ค.

์ด ๋ y์ถ๊ณผ ํํํ ์ง์ ์ด ๋์ค๋ฉด ๊ธฐ์ธ๊ธฐ๊ฐ ๋ฌดํ๋๊ฐ ๋๋, ๋ฐ๋ก ๋ถ๊ธฐ์ฒ๋ฆฌํด์ ํด๊ฒฐํด์ผ ํ๋ค.

## ๐ ์ฝ๋

```python
def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - \
        (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])


def cross():
    if x1 == x2:    # ์ฒซ๋ฒ์งธ ์ ๋ถ์ด y์ถ๊ณผ ํํํ  ๋(๊ธฐ์ธ๊ธฐ๊ฐ ๋ฌดํ)
        m2 = (y4 - y3) / (x4 - x3)      # ๋๋ฒ์งธ ์ ๋ถ์ ๊ธฐ์ธ๊ธฐ
        k2 = y3 - m2 * x3               # ๋๋ฒ์งธ ์ ๋ถ์ y์ ํธ
        cross_y = m2 * x1 + k2
        cross_x = x1
    elif x3 == x4:  # ๋๋ฒ์งธ ์ ๋ถ์ด y์ถ๊ณผ ํํํ  ๋(๊ธฐ์ธ๊ธฐ๊ฐ ๋ฌดํ)
        m1 = (y2 - y1) / (x2 - x1)      # ์ฒซ๋ฒ์งธ ์ ๋ถ์ ๊ธฐ์ธ๊ธฐ
        k1 = y1 - m1 * x1               # ์ฒซ๋ฒ์งธ ์ ๋ถ์ y์ ํธ
        cross_y = m1 * x3 + k1
        cross_x = x3
    else:
        m1 = (y2 - y1) / (x2 - x1)      # ์ฒซ ์ ๋ถ์ ๊ธฐ์ธ๊ธฐ
        m2 = (y4 - y3) / (x4 - x3)      # ๋๋ฒ์งธ ์ ๋ถ์ ๊ธฐ์ธ๊ธฐ

        k1 = y1 - m1 * x1               # ์ฒซ ์ ๋ถ์ y์ ํธ
        k2 = y3 - m2 * x3               # ๋๋ฒ์งธ ์ ๋ถ์ y์ ํธ
        cross_x = (k2 - k1) / (m1 - m2)     # ๋ ์ง์ ์ ๊ต์ฐจ์ ์ x ์ขํ
        cross_y = m1 * cross_x + k1
    return cross_x, cross_y



x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2 = [x1, y1], [x2, y2]
p3, p4 = [x3, y3], [x4, y4]

p12 = ccw(p1, p2, p3) * ccw(p1, p2, p4)  # p1, p2 ์ ๋ถ์ผ๋ก p3๊ณผ p4์ ๋ํ ccw์ ๊ณฑ
p34 = ccw(p3, p4, p1) * ccw(p3, p4, p2)  # p3, p4 ์ ๋ถ์ผ๋ก p1๊ณผ p2์ ๋ํ ccw์ ๊ณฑ
if p12 <= 0 and p34 <= 0:   # ๋ ์ ๋ถ์ด ๊ต์ฐจํ๋ ๊ฒฝ์ฐ(ํ ์ง์  ์์ ์์ ๋ ์๊ฐ!)
    if p12 == 0 and p34 == 0:   # ๋ ์ ๋ถ์ด ํ ์ ์์ ๋ง๋๊ฑฐ๋ ๊ฒน์น  ๋
        p1, p2 = min(p1, p2), max(p1, p2)
        p3, p4 = min(p3, p4), max(p3, p4)
        if p3 <= p2 and p1 <= p4:       # ๋ ์ ๋ถ์ด ๋ง๋๋ ๊ฒฝ์ฐ
            if ccw(p1, p2, p3) == 0 and ccw(p1, p2, p4) == 0:   # ๋ ์ ๋ถ์ด ๊ฒน์น  ๋(ํ ์ ์์ ์ ๋ง๋์ผ ํ๋ค.)
                if p3 == p2:    # p3์ p2 ํ ์ ์์ ๋ง๋  ๋
                    print(1)
                    print(*p2)
                    exit()
                if p1 == p4:    # p1๊ณผ p4 ํ ์ ์์ ๋ง๋  ๋
                    print(1)
                    print(*p1)
                    exit()
                print(1)        # ๋ ์ ๋ถ์ด ์ฌ๋ฌ ์ ์์ ๊ฒน์น  ๋
                exit()
            print(1)            # ๋ ์ ๋ถ์ด ํ ์ ์์ ๋ง๋  ๋(๊ธฐ์ธ๊ธฐ๊ฐ ๋ค๋ฆ)
            print(*cross())
            exit()
    else:
        print(1)
        print(*cross())
        exit()
print(0)        # ๋๋จธ์ง๋ ๊ต์ฐจํ์ง ์๋๋ค.
```

## ๐ ๊ฒฐ๊ณผ

![image-20220629123005623](README.assets/image-20220629123005623.png)