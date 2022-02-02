# [Python] for문 순회 시 값 변환

```python
lst = [1,2,3,4]
for num in lst:
	num += 1
print(lst) #=> [1,2,3,4]
```

iterate 객체에서 값을 순회해서 바꿔줘도 바뀌지 않는다!

값만 복사해서 오니 각 주소를 가져오지 않는다.

리스트 값을 바꾸고 싶으면 index를 순회해야 함.

```python
lst = [1,2,3,4]
for i in range(len(lst)):
	lst[i] += 1
print(lst) #=> [2,3,4,5]
```

