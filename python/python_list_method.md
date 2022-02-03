# [Python] 리스트 메소드(list method)

리스트(list) 자료형은 mutable(가변형) 자료형으로 string 자료형과 다르게 원본을 바꿀 수 있다.

## 추가

`L.append(x)`: 리스트 마지막에 항목 x를 추가, 반환 값은 None

```python
lst = [1, 2, 'a', 'b']
lst.append(10)
print(lst)	#=> [1, 2, 'a', 'b', 10]	lst에 10을 추가한다.
```

---

`L.extend(iterable)`: iterable 객체를 list에 원소로 넣어준다.

string 넣을 때 주의! string을 넣으면 나눠서 들어간다. string을 통째로 넣고싶으면 list에 담아서 넣어야 한다.

```python
lst = [1, 2, 'a', 'b']
lst.extend('abcd')
print(lst)	#=> [1, 2, 'a', 'b', 'a', 'b', 'c', 'd']	abcd가 나눠서 lst에 들어간다.
lst.extend(['abcd'])
print(lst)	# => [1, 2, 'a', 'b', 'a', 'b', 'c', 'd', 'abcd'] 'abcd'가 lst에 들어간다.
```

---

`L.insert(i,x)`: 리스트 인덱스 i에 항목 x를 삽입

정해진 위치에 값을 추가한다. 리스크 길이보다 큰 경우 맨 뒤에 추가!!

```python
lst = [1, 2, 'a', 'b']


lst.insert(2,5)
print(lst)
lst.insert(100,'k')
print(lst)
lst.insert(-1,'a')
print(lst)
'''
[1, 2, 5, 'a', 'b']			# 2번째 인덱스에 있는 'a' 자리에 5를 삽입
[1, 2, 5, 'a', 'b', 'k']	# 리스트의 길이를 초과하는 인덱스이니 맨 끝에 'k' 삽입
[1, 2, 5, 'a', 'b', 'a', 'k']	# -1로 인덱스를 설정하면 -1, -2 인덱스 사이에 삽입
'''
```

---

---

## 삭제

`L.remove(x)`: 리스트 가장 왼쪽에 있는 항목 x를 제거, 항목이 존재하지 않을 경우, ValueError

```python
lst = [1, 2, 'a', 'b']

lst.remove(2)
print(lst)	# [1, 'a', 'b']  2 제거
lst.remove(100)	# ValueError: list.remove(x): x not in list
```

---

`L.pop(i)`: 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환, i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함.

```python
lst = [1, 2, 'a', 'b']

print(lst.pop(2))	# => a   : 제거한 항목을 반환
print(lst)	# [1, 2, 'b']  2번째 index인 'a' 제거
```



`L.clear()`: 모든 항목을 삭제!! 초기화할 때 사용한다.

```python
lst = [1, 2, 'a', 'b']

lst.clear()
print(lst)	# [] : 초기화
```

---

---

## 탐색

`L.index(x)` x값을 찾아 해당 index 값을 반환. 없는경우 value error

---

`L.count(x)` 리스트에 있는 x의 개수를 반환

---

`L.sort()`: sorted랑 다르다!!! 함수와 메서드의 차이~~!

**L.sort(reverse = True) : 내림차순 정렬**

원본 리스트를 정렬함. None 반환 => 원본을 변경

```python
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result) #=> [1, 2, 3, 5] None
```

```python
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result) #=> [3, 2, 5, 1] [1, 2, 3, 5]
```

---

`L.reverse()`: 순서를 반대로 뒤집음(정렬하는 것이 아님) : 원본 자체의 순서를 뒤집는다.

