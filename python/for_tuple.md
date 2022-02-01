# [Python] for 문 응용, 여러 요소 순회

튜플이 들어간 자료형은 여러 요소를 한 번에 순회할 수 있다.

```python
data_list = [('민수', 27), ('철수', 27), ('영희', 29), ('지희', 32)]
for (name, age) in data_list:
    print(name, age)
    
'''
민수 27
철수 27
영희 29
지희 32
'''
```

---

리스트도 여러 요소를 한 번에 순회 가능하다.

```python
data_list = [['민수', 27], ['철수', 27], ['영희', 29], ['지희', 32]]
for (name, age) in data_list:
    print(name, age)
    
'''
민수 27
철수 27
영희 29
지희 32
'''    
```

---

갯수가 맞지 않으면 오류가 난다.

```python
data_list = [['민수', 27], ['철수', 27, 2], ['영희', 29], ['지희', 32]]
for (name, age) in data_list:
    print(name, age)
    
'''
ValueError: too many values to unpack (expected 2)
'''
```

