# [AtCoder] B. Get Closer [Beginner Contest 246]

## π λ¬Έμ 

https://atcoder.jp/contests/abc246/tasks/abc246_b

---

## π νμ΄

math λ¬Έμ μ΄λ€. μ κ³±ν΄μ λν κ°μ΄ 1μ λ§λλ λ¬Έμ μ΄λ€. μ£Όμ΄μ§ A, Bκ° λ μμ λΉμ¨μ΄λ μ κ³±ν΄μ λν μμ μ κ³±κ·Όμ A, B κ°κ° λλ μ£Όλ©΄ λλ€.

## π μ½λ

```python
a, b = map(int, input().split())
total = a ** 2 + b ** 2
print(a/(total ** (1/2)), b/(total ** (1/2)))
```

## π κ²°κ³Ό

![image-20220403001248388](README.assets/image-20220403001248388.png)