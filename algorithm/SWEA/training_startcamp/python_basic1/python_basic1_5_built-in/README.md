# [SWEA] 파이썬 프로그래밍 기초(1) - 내장함수

링크 : https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDAe6AATw5UW6&subjectId=AWT4H-1q2m8DFAVT

---

## SWEA 6308. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 1

### 📚 문제

다음의 결과와 같이 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

```
Input
홍길동
20

Output
홍길동(은)는 2099년에 100세가 될 것입니다.
```

---

`int()`도 내장함수

### 📒 코드

```python
name = input()
age = int(input())

print(f'{name}(은)는 {age+2079}년에 100세가 될 것입니다.')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6311. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 4

### 📚 문제

"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

```
Input
없음

Output
184
```

---

`map(x,y)` 함수를 사용한다. y라는 자료형의 각각에 x라는 함수를 적용해 바꾸어주는 함수이다.

x라는 함수는 람다식을 활용해 if else 구문을 반복해 만들어준다.

**람다식에 조건문을 넣을 땐 elif를 사용할 수 없고 break도 사용할 수 없다.** 따라서 조건문을 중첩으로 if else를 반복해 만들어야 한다.

### 📒 코드

```python
text = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
total = 0

scores = list(map(lambda x: 4 if x=='A' else 3 
if x=='B' else 2 if x=='C' else 1, text))

for score in scores:
    total += score
    
print(total)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6312. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 5

### 📚 문제

가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고, 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

```
Input
없음

Output
에러발생
```

---

함수에서 여러가지 값의 인자를 입력으로 받기 위해 `*nums`로 받는다. 이러면 nums는 **튜플**형태로 생성된다. 정수가 아닌 값을 구별하기 위해 `map함수`를 사용해 튜플 값인 `nums`를 `int`형태로 받는다. `tuple(map(int,nums))`가 nums와 다른 값을 가지게 되면, nums에 정수가 아닌 인수가 있는 것이므로 이 때 *"에러발생"* 키워드를 프린트한다.

### 📒 코드

```python
def mul(*nums):
  mul_result = 1
  if tuple(map(int,nums)) != nums:
      print("에러발생")
      return 0
  for num in nums:
      mul_result *= num
  print(mul_result)

mul(1,2,'4',3)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6313. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 6

### 📚 문제

ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

```
Input
65

Output
ASCII 65 => A
```

---

`chr() `함수를 사용해 숫자를 유니코드로 변환한다.

문제는 아스키코드라고 되어있지만.. python은 **유니코드**를 쓴다!

### 📒 코드

```python
num = int(input())

print(f'ASCII {num} => {chr(num)}')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6314. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 7

### 📚 문제

1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

```
Input
없음

Output
[2, 4, 6, 8, 10]
```

---

연속된 정수의 list를 만들기 위해 `range()`를 사용한다. `range()`를 `list()`로 씌워준다.

`filter(def,list)`는 *list*를 *def*라는 필터를 거쳐 남은 요소들만으로 변환시켜주는 함수이다.

짝수를 나타내는 함수를 한 줄로 정의해주기 위해서 람다식을 활용한다.

filter함수를 그냥 출력하면 **map**과 같이 **filter 객체**가 출력되므로 `list()`를 사용한다.

### 📒 코드

```
nums = list(range(1,11))

def evens(nums):
    return list(filter(lambda n: n % 2 == 0, nums))
    
print(evens(nums))
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6315. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 8

### 📚 문제

1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

```
Input
없음

Output
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

람다식으로 제곱 함수를 만들어주어 출력한다.

### 📒 코드

```python
nums = list(range(1,11))

def evens(numbers):
    return list(map(lambda x: x**2, numbers))

print(evens(nums))
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6316. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 9

### 📚 문제

1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

```
Input
없음

Output
[4, 16, 36, 64, 100]
```

---

`filter()`함수는 `map()`와 비슷한데 map은 전체 인수들을 바꾸어주는 것이라고 하면 filter는 특정 인덱스만 골라 새로운 배열로 만들어는 함수이다.

### 📒 코드

```python
nums = list(range(1,11))

def evens_double(numbers):
    result = numbers
    result = list(filter(lambda x: x%2==0, result))
    return list(map(lambda x: x**2, result))

print(evens_double(nums))
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6317. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 10

### 📚 문제

가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고, 다음과 같은 결과를 출력하는 프로그램을 작성하십시오.

```
Input
없음

Output
max(3, 5, 4, 1, 8, 10, 2) => 10
```

---

가변형 인자를 전달받기 위해 함수의 인자로 `*(unpack 연산자)`를 활용한다.

내장함수인 max함수로 연속된 인자 중 가장 큰 값을 반환한다.

### 📒 코드

```python
def max_num(*nums):
    return max(nums)
    
print(f'max(3, 5, 4, 1, 8, 10, 2) => {max_num(3, 5, 4, 1, 8, 10, 2)}')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6318. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 11

### 📚 문제

다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를 값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는 프로그램을 작성하십시오.

```
Input
없음

Output
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5
```

---

`zip()` 함수를 사용해서 string과 range()의 같은 **index**끼리 묶어주고 이를 `dict()`로 묶어 각각 key와 value로 만들어 준다. `dict()`는 딕셔너리로 만들어주는 함수이다.
딕셔너리는 for 문에서 key값을 순회시켜 사용 가능하다. 이때 값을 사용하고 싶으면 **딕셔너리[key]**를 사용한다.

### 📒 코드

```python
input_string = 'abcdef'
dic = dict(zip(input_string, range(6)))

for key in dic:   # 딕셔너리 for문 응용
    print(f'{key}: {dic[key]}')
```

### 🔍 결과: **Pass**