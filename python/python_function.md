# [Python] 함수(function)

## 함수의 반환값은 무조건 하나

return이 없는 경우 **None**을 반환하고 종료한다.

`return x-y, x*y` 이렇게 적은 건 튜플 값을 1개 반환한 것이다.

2개 이상은 tuple값으로 반환한다. ex). `(x-y, x*y)`

---

---

## 매개변수(Parameter), 인자(Argument)

매개변수(parameter)는 내부에서 사용되는 식별자, 정의할 때 필요한 변수이다.

`def func():` 정의하면 ()안에 넣어주는 값 매개변수이다.

```python
def func(x, y):	# parameter x, y
    return
```

매개변수는 기본인자(default)를 가질 수 있다.

```python
def func(x, y = 1):	# parameter y의 기본인자(defualt)로 1 설정
    return
```

매개변수를 선언할 때 **기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.**

```python
def greeting(name='john', age):
    return f'{name}은 {age}살입니다.'
'''
SyntaxError: non-default argument follows default argument
'''
```

위처럼 사용하면 오류 발생!	

기본인자는 무조건 뒤부터 선언해줘야 한다.

---

인자(argument)는 호출할 때 넣어주는 실제 값이다.

```python
def func(x, y):	# 함수 선언
    return

func(1, 2)	# 함수 호출, argument : 1, 2
```

argument 중 **기본 인자** 값이 할당되어있는 파라미터는 안 넣어줘도 된다. 정의된 것보다 더 적은 개수의 argument로 호출 가능하다.

```python
def add(x, y, z = 0):	# 2, 3개를 넣어도 다 가능하다.
    return x + y + z

print(add(1, 3))	# x에 2를 담고, y에 3, z는 기본 인자 값인 0을 넣는다.
''' 1+3
4
'''
print(add(1, 2, 3)) # z에도 3을 담는다.
''' 1+2+3
6
'''
```

**argument에서는 위치인자, 키워드 인자**로 호출한다. 위치인자는 parameter 순서대로 넣어주면 되고 키워드 인자는 순서 상관없이 **parameter = 값**으로 넣어준다.

위치 인자와 키워드 인자를 함께 쓸 때 위치 인자를 먼저 적어야 한다. 키워드로 지정하는 순간 위치가 이미 박살나기 때문에 키워드 인자가 나오면 그 뒤는 다 키워드 인자만 넣어야 한다.

```python
def three_nums(hunds, tens, ones):	# 백의자리, 십의자리, 일의자리를 넣어 세자리 수로 반환한다.
    return hunds * 100 + tens * 10 + ones

print(three_nums(2, 3, 4))	# 위치인자로 2는 hunds, 3은 tens, 4는 ones에 들어간다.
'''
234
'''
print(three_nums(tens = 2, ones = 3, hunds = 1))	# 키워드 인자는 파라미터에 값을 넣어줘 순서 상관없이 적을 수 있다.
'''
123
'''
print(three_nums(1, ones = 3, tens = 2))	# 키워드 인자와 위치 인자를 중복해서 사용할 수 있다. 이 땐 무조건 위치 인자를 먼저 넣어야한다.
'''
123
'''
print(three_nums(tens = 1, ones = 3, 2))	# 키워드 인자가 나온 순간 위치는 박살나기 때문에 그 뒤에 위치 인자를 사용할 수 없다.
'''
SyntaxError: positional argument follows keyword argument
'''
```

---

---

## 함수는 가장 기본이 local scope! 

함수가 호출되고 종료될 때까지 유지한다. return을 만날 때까지 안에서 설정한 변수는 함수 밖에서 사용할 수 없다.

함수는 블랙박스로 입력과 return 값인 반환 값만 있다고 보면 된다. 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용하는 것이다.

