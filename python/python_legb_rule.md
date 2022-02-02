# [Python] LEGB rule(이름 검색 규칙)

파이썬에서 사용되는 이름은 이름공간에 저장되어 있다.

**LEGB** rule (Local, Enclose, Global, Built-in) -> 왼쪽부터 오른쪽 순대로

---

**Built-in** 내장함수의 이름을 똑같이 (Global에)정의해서 사용하면 그 내장함수는 새로 정의한 걸 사용하게 된다.

del로 다시 Global 변수를 지워서 내장함수를 쓸 순 있다.

```python
list = []	# Bulit-in 내장함수를 글로벌에 똑같은 이름으로 정의, 이후로는 list() 사용 불가능하다.
del list	# global 영역에 정의된 list 변수를 지워 list()를 다시 사용할 수 있다.
```

---

**global** 키워드를 사용하면 global 영역의 변수를 입력이 아니어도 가져와서 사용한다.

함수 안에서 이런식으로 선언해서 사용한다.

```python 
a = 0
def func():
    global a	# 함수 안에서 global 영역에 있는 변수 a를 가져와서 사용
    a += 3  
```

---

**nonlocal** : E(enclose)

중첩 함수에서 사용한다. 함수 안에 함수가 있는 경우 global이 아닌 바깥 영역의 변수를 사용할 수 있다.

```python
def func1():
    a = 1
    def func2():	# nonlocal 키워드를 사용해 enclose 영역에 있는 변수를 사용한다.
        nonlocal a
        a += 2
```

---

global과 nonlocal을 가급적 실무에서는 사용하지 않기로 권장한다. 

알고리즘할 때 편하게 사용하자!