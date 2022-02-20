# [Python] 딕셔너리(dictionary) 메서드(method)

**key**는 **해시 가능한 객체(immutable)**만 담을 수 있다. list나 딕셔너리는 못 담는다.

**value**는 중복 가능, **key**는 중복 불가능

`{}`로 초기화하거나 `dict()`로 초기화한다.

```python
dic = {}
dic = dict()
```

## 딕셔너리 메서드

### 📌 .keys()

`딕셔너리.keys()`를 사용해 key를 dict_keys 객체로 뽑아온다.

### 📌 .values()

`딕셔너리.values()`를 사용해 value를 dict_values 객체로 뽑아온다.

### 📌 .items()

`딕셔너리.items()`를 사용해 딕셔너리의 key와 value를 **tuple**로 묶어 dict_items 객체로 뽑아온다.

```python
dic = {'철수' : 20, '영희' : 25, '짱구' : 10}
print(dic.keys())
print(dic.values())
print(dic.items())
'''
dict_keys(['철수', '영희', '짱구'])
dict_values([20, 25, 10])
dict_items([('철수', 20), ('영희', 25), ('짱구', 10)])
'''
```

item 같은 경우는 딕셔너리의 키와 value를 둘다 순회하여 for문으로 사용할 때 유용하게 사용한다.

### 📌 .get(key[,default = None])

key를 통해 value를 가져오면 default는 None이다! 에러가 없으며 default를 변경해 없는 값을 불러올 때 다른 값이 반환되도록 설정할 수 있다.

딕셔너리[key]로 사용하는 것과 에러 유무가 다르다.

### 📌 .pop(key[,default])

key가 있으면 제거하고 **해당 값을 반환**한다. 없으면 default를 반환한다. 기본으로 설정된 default 값이 없다.

default가 없으면 제거할 항목이 없을 때 KeyError 에러가 난다.

>del 키워드로 제거 가능!
>
>del dic[key]

### 📌 .update()

값을 제공하는 key, value로 덮어쓴다.

문자열 key는 따옴표 없이 넣는다. parameter는 따옴표 없이 사용한다.

key가 문자열 일 때는 `.update(문자 = value, ~)` 형식으로 넣고 key에 따옴표를 제거한 후 정수같은 게 들어오면 `.update({key : value, ~})` 이렇게 다 넣는다. 딕셔너리 형태로 넣으면 에러 발생할 일이 없다.

데이터를 한꺼번에 바꿀 때 유용하다.