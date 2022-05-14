# [Python] 랜덤(Random) 모듈 🎲

##  🎲 랜덤(Random)

- 파이썬에서 난수를 발생시키기 위해 사용.

- 랜덤 모듈을 import 한다.

  ```python
  import random
  ```



### 랜덤 메서드

- random.random()

  0.0 <= x < 1.0 사이의 랜덤한 실수

  

- random.uniform(a, b)

  a<= x <= b 사이의 랜덤한 실수

  

- random.randint(a, b)

  a<= x< b 사이의 랜덤한 정수

  

- random.randrange(a, b)

  a<= x< b 사이의 랜덤한 정수

  

- random.randint(a, b)

  a<= x <= b 사이의 랜덤한 정수

  

- random.choice(seq)

  seq 중 랜덤으로 고른 하나의 원소

  

- random.sample(deq, n)

  seq 중 n개의 랜덤한 원소들의 배열을 리턴

  

- random.shuffle(seq)

  seq가 랜덤으로 섞어서 바꿔버린다! 반환 값은 None

  

### random 모듈 사용 예시

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

