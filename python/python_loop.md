# 반복문 else, iterable 객체 for문 순회

## 반복문 else

for문이나 while문 둘다 조건문처럼 **else**를 사용할 수 있다.

다 도는 동안 **break**를 거치지 않으면 **else문**이 실행된다.

break에 걸리는지 확인하는 용도로 사용할 수 있고, break를 안 거칠 때만 코드를 적용시킬 때 쓰면 편하다.

```python
for x in range(5):	# for문에서 else문 사용
    pass
else:
    pass
```

while문의 조건식을 True로 했으면, 절대로 else문을 거치지 않는다.

break가 걸려야만 while문을 **탈출**하기 때문이다.

## iterable 객체 for문 순회

for문은 시퀀스(string, tuple, list, range, set, dictionary) 를 포함한 순회가능한 객체 요소를 모두 순회한다.

**딕셔너리**는 **key**를 순회하여 사용하며 **순서 보장**은 안된다.

**세트**도 순회하지만 순서를 보장하진 않는다.