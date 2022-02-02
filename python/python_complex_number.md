# [Python] 복소수(complex) 표현

## 복소수 표현할 때 주의할 점~

복소수 표현할 때 `1+j` 이렇게 표현하면 에러가 난다.

이유는 숫자와 문자열을 더한다고 생각해서 에러가 나는데 j앞에 무조건 숫자를 같이 붙여줘야 한다.

따라서 `1+1j`처럼 써야 올바르게 복소수로 표현할 수 있다.

```python
print(type(1+j)) #=> error : 1 + j(변수)
print(type(1+1j)) #=> 복소수
print(type(j)) #=> error : j라는 변수로 읽는다.
print(type(1j)) #=> 복소수
```

## 복소수의 허수부와 실수부를 분리하고 싶을 때

복소수 표현으로 `.real` 와 `.imag` 가 있다. 
내장함수가 아니라 접근할 수 있는 속성으로 `.real'은 실수부를 나타내고 '.imag'는 허수부를 나타낸다.

```python
a = 1+1j
b = 1j
print(a.real, a.imag) #=> 1.0  1.0
print(b.real, b.imag) #=> 0.0  1.0
```

