# [Python] 조건 표현식

`list Comprehension` 특정 값을 가진 리스트를 간결하게 생성

2차원 리스트 초기화 할 때 매우 효과적으로 사용(for문 사용)

```python
m, n = 2, 3
lst = [[0] * m for _ in range(n)] # 3x2 리스트 초기화
print(lst)
'''
[[0, 0], [0, 0], [0, 0]]
'''
```

---

map를 list comprehension으로 사용(for문 사용)

```python
numbers = ['1','2','3','4','5']
lst = [int(x) for x in numbers]	# numbers의 인자들을 str에서 int로 변환
print(lst)
'''
[1, 2, 3, 4, 5]
'''
```

---

filter를 list comprehension으로 사용(for문 + if문 사용)

```python
numbers = [1,2,3,4,5]
lst = [x for x in numbers if x % 2]	# numbers의 인자들 중 홀수만 선택
print(lst)
'''
[1, 3, 5]
'''
```

---

map과 filter 모두 사용(for문 + if문 사용)

```python
numbers = [1,2,3,4,5]
lst = [x**2 for x in numbers if x % 2] # numbers의 인자들 중 홀수만 선택해서 제곱
print(lst)
'''
[1, 9, 25]
'''
```

---

if else 둘 다 사용!!

```python
numbers = [1,2,3,4,5]
lst = [True if x % 2 else False for x in numbers] # numbers의 인자가 홀수면 True, 짝수면 False 변환
print(lst)
'''
[True, False, True, False, True]
'''
```

