# [Python] Set 자료형 정리

Set 자료형은 순서가 없는 집합 자료형이다.(해시가능한, 불변 자료형만 담는다.)

순서가 없어 인덱스로의 접근이 불가능하다.

set는 {}처럼 괄호로만 초기화는 불가능하다.({}는 딕셔너리) 

set()로 초기화해야 한다.

## set자료형의 연산자

교집합 : `A & B`

합집합 : `A | B`

차집합 : `A - B`

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)
print(A | B)
print(A - B)
'''
{3}
{1, 2, 3, 4, 5}
{1, 2}
'''
```

## set 메서드

### `.add(elem)`

set은 순서가 없어 append가 아니라 add를 쓴다.

add를 해줘도 뒤에 붙는게 아니라 랜덤으로 섞인다.

### `.remove(elem)`

셋에서 삭제하고, 없으면 keyError 발생한다.

### `.discard(elem)`

셋에서 삭제하고 없어도keyError 발생 안한다.

### `.pop()`

set에서 임의의 원소를 제거한 후 반환한다.