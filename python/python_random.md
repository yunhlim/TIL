# [Python] λλ€(Random) λͺ¨λ π²

##  π² λλ€(Random)

- νμ΄μ¬μμ λμλ₯Ό λ°μμν€κΈ° μν΄ μ¬μ©.

- λλ€ λͺ¨λμ import νλ€.

  ```python
  import random
  ```



### λλ€ λ©μλ

- random.random()

  0.0 <= x < 1.0 μ¬μ΄μ λλ€ν μ€μ

  

- random.uniform(a, b)

  a<= x <= b μ¬μ΄μ λλ€ν μ€μ

  

- random.randint(a, b)

  a<= x< b μ¬μ΄μ λλ€ν μ μ

  

- random.randrange(a, b)

  a<= x< b μ¬μ΄μ λλ€ν μ μ

  

- random.randint(a, b)

  a<= x <= b μ¬μ΄μ λλ€ν μ μ

  

- random.choice(seq)

  seq μ€ λλ€μΌλ‘ κ³ λ₯Έ νλμ μμ

  

- random.sample(deq, n)

  seq μ€ nκ°μ λλ€ν μμλ€μ λ°°μ΄μ λ¦¬ν΄

  

- random.shuffle(seq)

  seqκ° λλ€μΌλ‘ μμ΄μ λ°κΏλ²λ¦°λ€! λ°ν κ°μ None

  

### random λͺ¨λ μ¬μ© μμ

```python
import random

print(random.random())              # 0.8999159382861155
print(random.uniform(1, 5))         # 1.4874879446752813
print(random.randint(1, 5))         # 5
print(random.randrange(1, 5))       # 4

arr = ['a', 'b', 'c', 'd', 'e']
print(random.choice(arr))           # d
print(random.sample(arr, 2))        # ['b', 'd']
print(random.shuffle(arr))          # None
print(arr)                          # ['c', 'b', 'e', 'd', 'a']
```

