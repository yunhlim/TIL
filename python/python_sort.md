# [Python] .sort 메서드, sorted 함수

## .sort() vs sorted()

`sorted()` 함수는 새로 정렬시킨 리스트를 만들어 반환하고 `.sort()` 메서드는 기존의 리스트를 바꾼다.

```python
arr = [2, 1, 6, 3]

a = sorted(arr)	
print(a)	# => [1, 2, 3, 6]
print(arr)	# => [2, 1, 6, 3]

b = arr.sort()
print(b)	# => None
print(arr)	# => [1, 2, 3, 6]
```

---

## 여러 가지 활용!

기본 default 값은 오름차순 정렬이지만 `reverse = True`

```python
arr = [2, 1, 6, 3]

a = sorted(arr, reverse=True)	# => 거꾸로 정렬
print(a)	# => [6, 3, 2, 1]

b = arr.sort(reverse=True)	# => 거꾸로 정렬
print(arr)	# => [6, 3, 2, 1]
```

iterable한 객체들을 원하는 인덱스 값으로 정렬시킬 수 있다. 

```python
arr = [('a', 1), ('c', 6), ('d', 2), ('f', 3)]

a = sorted(arr, key = lambda x : x[1])	# => 1번째 인덱스로 정렬
print(a)	# => [('a', 1), ('d', 2), ('f', 3), ('c', 6)]

b = arr.sort(key = lambda x : x[1])	# => 1번째 인덱스로 정렬
print(arr)	# => [('a', 1), ('d', 2), ('f', 3), ('c', 6)]
```

인덱스 여러 개 중 원하는 순서대로(사전처럼) 정렬 시킬 수 있다.

```python
arr = [(1, 10), (4, 60), (4, 20), (3, 20)]

a = sorted(arr, key = lambda x : (x[0], x[1]))	# 0번째 인덱스로 먼저 정렬하고 같으면 1번째 인덱스로 정렬
print(a)	# => [(1, 10), (3, 20), (4, 20), (4, 60)]

b = arr.sort(key = lambda x : (x[0], x[1]))	# 0번째 인덱스로 먼저 정렬하고 같으면 1번째 인덱스로 정렬
print(arr)	# => [(1, 10), (3, 20), (4, 20), (4, 60)]
```

lambda에 인덱스가 아닌 값도 사용 가능하다.

```python
arr = ['abc', 'coffee', 'banana', 'coke']

a = sorted(arr, key = lambda x : len(x))	# 값의 길이로 정렬
print(a)	# => ['abc', 'coke', 'coffee', 'banana']

b = arr.sort(key = lambda x : len(x))	# 값의 길이로 정렬
print(arr)	# => ['abc', 'coke', 'coffee', 'banana']
```

