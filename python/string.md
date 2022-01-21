# [Python] 문자열 포맷팅, Escape sequence

## 문자열 표시 방법[Escape sequence]

문자열 표시 중첩 따옴표, 삼중 따옴표로 문자열 표시!

### escape sequence

\n 줄바꿈 (Line Feed(LF) 라는 의미를 가지며 일반적으로는 New Line, 즉 새로운 라인이라는 뜻입니다.) 

\t 탭(tab)

\r 캐리지 리턴(Carriage Return(CR) 라는 의미를 가지며 일반적으로는 맨앞으로 이동하라는 뜻입니다.) 

\나 ,를 나타내고 싶으면 \를 앞에 붙인다.

---

---

## 문자열 포맷팅 String Interpolation

중요하다!💥💥

가장 쉬운 방법은 **f-strings**! 파이썬 3.6버전 이상일 때~

print문 상관없이 사용할 수 있다.

작동 속도도 가장 빠르다고 한다!!

```python
name = '참새'
print(f'안녕 {name}야') # 안녕 참새야
str = f'안녕 {name}야' # print문 아니어도 적용 가능!!!
print(str) # 안녕 참새야
```

---

**%-formatting**, **str.format()**도 있다. 

3.6버전보다 아래 버전일 수도 있으니 알아두자~

```python
name = '참새'
print('안녕 %s야' %(name)) # % 포맷팅
print('안녕 {0}야'.format(name)) # format 함수
```

%-formatting은 문자열에는 %s를 쓰고, 정수에는 %d, 실수에는 %f를 사용

str.format()은 {0}, {1}, {2},... 순으로 들어간다.