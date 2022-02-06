# [Python] 연산자

## 멤버십 연산자

**멤버십 연산자** `in`, `not in` 컨테이너 포함 여부 확인

조건식에서 사용한다.

```python
lst = [1,2,3,4]
num = 5

if num in lst:	# in 연산자로 컨테이너 안에 있는지 확인한다.
    print(f"{num}는 {lst} 안에 있습니다.")
else: print(f"{num}는 {lst} 안에 없습니다.")
'''
5는 [1, 2, 3, 4] 안에 없습니다.
'''
```

for 문에서 하나 씩 순회 돌릴 때 사용한다. 시퀀스가 아닌 세트도 가능하다!

```python
for i in range(4):
    print('*'*(i+1))
'''
*
**
***
****
'''
```

set에선 순서를 상관하지 않고 사용해야 한다.

```python
set_arr = {1,4,3,2}

for i in set_arr:
    print('*'*i)
''' 순회할 때 set는 순서가 없으니 무작위로 순회한다고 생각하자!
*
**
***
****
'''
```

---

## 시퀀스형 연산자

시퀀스형 연산자(`+`,`*`)

문자열 뿐 아니라 리스트나 튜플 등의 시퀀스형 자료형을 곱해서 나타낼 수 있음!!

시퀀스 연산자 **+**는 `.append()`처럼 사용한다.

```python
lst = [1,2]

print(lst + [3,4]) # [1, 2, 3, 4]
print(lst*2)	# [1, 2, 1, 2]
```

tuple 연산자를 `+`더할 때 하나의 튜플을 더하려면 `(1,2) + ('a',)` 이런 식으로 합친다!

```python
tuple_arr = (1, 2, 3)

print(tuple_arr + (4))	# TypeError: can only concatenate tuple (not "int") to tuple
print(tuple_arr + (4,))	# (1, 2, 3, 4)
```

---

## set 연산자

set 연산자 (`|`: 합집합, `&`: 교집합, `-`: 차집합, `^`: 대칭차)

```python
set_a = {1,2,3}
set_b = {3,4,5}

print(set_a | set_b)	# 합집합
print(set_a & set_b)	# 교집합
print(set_a - set_b)	# 차집합
print(set_a ^ set_b)	# 대칭차
'''
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}
'''
```

---

## 논리 연산자

논리 연산자(`and`,  `or`,  `not`)

0이나 [],{}, False가 아니면 다 True

True를 반환할 때 그 값을 반환한다. **마지막으로 확인한 값을 반환!!**

```python
print(5 and 4)	# 4
print(0 and 5)	# 0
print([] and 3)	# []
print('' and False) # '' 공백을 출력
print(5 or 3)	# 5
print(5 or 0)	# 5
print(0 or 5)	# 5
print('' or 0)	# 0

if 5:	# 조건문은 boolean 값으로 변환해서 사용한다.
    print(True)
```

위처럼 논리 연산자를 사용하는 경우는 거의 드물고 조건문에서 거의 다 활용한다.