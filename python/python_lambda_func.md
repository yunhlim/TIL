# [Python] 람다(lambda) 표현식

람다 표현식은 def로 정의하지 않아 이름없는 함수를 만든다. 따라서 **익명 함수**라고도 부른다. 함수를 한 번만 사용할 경우 일회용으로 쓰고 사라지게 만들어 메모리도 효율적이고 시간도 절약시킬 수 있는 방법이다. 또한 코드도 간결해진다.

```python
def plus(x,y):	# 함수를 정의해서 사용
    return x+y

lambda x,y : x+y	# 람다표현식으로 표현
```

---

특히 일회용으로 `map()`과 함께 사용할 때가 많다.

```python
lst = [1,2,3,4,5]
print(list(map(lambda x : x**2, lst)))

''' 람다표현식을 활용해 제곱을 해주는 함수를 만든다.
[1, 4, 9, 16, 25]
'''
```

---

반복문을 쓸 수 없으며, 간편 조건문만 가능하다.

list comprehension과 달리 간편 조건문만 가능해서 elif를 쓸 수 없다.

따라서 중첩 if else문을 활용해서 사용해야 한다.

```python
def credit(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else: return 'F'

# 중첩 if else 반복으로 적어야해서 복잡하다. elif를 못 쓴다!
lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'

```

짧은 조건문이 아닌 복잡한 조건문은 함수를 따로 정의하는 것이 가독성에도 좋고 깔끔하다.