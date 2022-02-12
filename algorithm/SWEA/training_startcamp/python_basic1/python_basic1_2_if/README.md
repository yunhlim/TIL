# [SWEA] 파이썬 프로그래밍 기초(1) - If

링크 : https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDAe6AATw5UW6&subjectId=AWT4H-1q2m8DFAVT

---

## SWEA 6218. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 1

### 📚 문제 

다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

```
Input
9

Output
1(은)는 9의 약수입니다.
3(은)는 9의 약수입니다.
9(은)는 9의 약수입니다.
```

---

정수형 Input을 받아 var에 저장한다.

*var*을 1부터 1씩 증가시켜가며 순차적으로 나눠가며 약수를 찾는다. 그러기 위해 *div*라는 변수에 1을 담고 `%(나머지) 연산자`를 이용해 print한다.

while문을 break하기위해 div가 var과 같을 때 탈출하도록 한다.

### 📒 코드

```python
var = int(input())
div = 1
while True:
    if var % div == 0:
        print(f'{div}(은)는 {var}의 약수입니다.')
    if div == var:
        break
    else:
        div += 1
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6219. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 2

### 📚 문제

다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오 (단, 약수가 2개일 경우 소수임을 나타내십시오)

```
Input
5

Output
1(은)는 5의 약수입니다.
5(은)는 5의 약수입니다.
5(은)는 1과 5로만 나눌 수 있는 소수입니다.
```

---

소수를 확인하기 위해 *cnt*변수를 선언해 약수의 개수를 확인한다. 마지막에 약수의 개수가 2개일 때 소수라는 메시지를 출력한다.

### 📒 코드

```python
var = int(input())
div = 1
cnt = 0
while True:
    if var % div == 0:
        print(f'{div}(은)는 {var}의 약수입니다.')
        cnt += 1
    if div == var:
        if cnt == 2:
            print(f'{div}(은)는 1과 {var}로만 나눌 수 있는 소수입니다.')
        break
    else:
        div += 1
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6220. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 3

### 📚 문제

다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.

```
Input
b

Output
b 는 소문자 입니다.
```

---

파이썬에 대소문자 비교할 수 있는 함수인 `isupper(), islower()`가 있지만 if문을 활용하라고 했으니 a~z사이에 있으면 소문자, A~Z사이에 있으면 대문자, 그 이외엔 영어가 아닙니다.라는 메시지를 출력한다.

### 📒 코드

```python
alphabet = input()
if 'a' <= alphabet <= 'z':
    print(alphabet+' 는 소문자 입니다.')
elif 'A' <= alphabet <= 'Z':
    print(alphabet+' 는 대문자 입니다.')
else :
    print('영어가 아닙니다.')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6221. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 4

### 📚 문제

다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오. 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
**[입력]**

두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
**[출력]**

첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다. 예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다. 단, 비긴 경우는 Result : Draw 라고 출력한다.

```
Input
바위
가위

Output
Result : Man1 Win!
```

---

if elif 중첩문을 활용해 모든 경우의 수를 작성한다.

### 📒 코드

```python
man1 = input()
man2 = input()
if man1 == '바위':
    if man2 == '바위':
        print("Result : Draw")
    elif man2 == '가위':
        print("Result : Man1 Win!")
    elif man2 == '보':
        print("Result : Man2 Win!")
elif man1 == '가위':
    if man2 == '바위':
        print("Result : Man2 Win!")  
    elif man2 == '가위':
        print("Result : Draw")  
    elif man2 == '보':
        print("Result : Man1 Win!")
elif man1 == '보':
    if man2 == '바위':
        print("Result : Man1 Win!")
    elif man2 == '가위':
        print("Result : Man2 Win!")
    elif man2 == '보':
        print("Result : Draw")
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6222. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 5

### 📚 문제

다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고, 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오. 출력 시 아스키코드를 함께 출력합니다.

```
Input
c

Output
c(ASCII: 99) => C(ASCII: 67)
```

---

문자를 아스키코드로 변환시켜주기 위해 `ord()`함수를 사용한다. 

`islower()[isupper()]`를 사용해서 소[대]문자인지 판별하고 `upper()[lower()]`로 대[소]문자로 바꿔준다.

### 📒 코드

```python
ch = input()

if ch.islower():
    print(f'{ch}(ASCII: {ord(ch)}) => {ch.upper()}(ASCII: {ord(ch.upper())})')
else:
    print(f'{ch}(ASCII: {ord(ch)}) => {ch.lower()}(ASCII: {ord(ch.lower())})')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6226. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 7

### 📚 문제

1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

```
Input
없음

Output
7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196
```

---

for문과 `range()`로 1~200를 순서대로 센다. **%(나머지 연산자)**를 사용해서 배수인지 배수가 아닌지 판단한다.

,로 연결된 숫자들을 출력하기 위해 먼저 list를 만든다.

for문에 의해 알맞은 숫자들을 하나씩 `.append()`를 이용해 list에 입력한다.

list를 숫자 사이에 ,를 붙여 출력하기 위해 `print(*numbers, sep = ',')`로 출력한다.

unpack 연산자인 `*`로 []를 제거해주고 sep을 이용해 중간에 ,를 붙여준다.

### 📒 코드

```python
numbers = []
for i in range(1,201):
    if i % 7 == 0:
        if i % 5 != 0:
            numbers.append(i)

print(*numbers, sep = ',')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6227. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 8

###  📚 문제

100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

```
Input
없음

Output
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288
```

---

**1의 자리**를 나타내기 위해 **%연산자**를 활용해 `i%10` 10으로 나눈 나머지로 찾는다.

**10의 자리**를 나타내기 위해 100으로 나눈 나머지를 구해 10의자리 이하만 남기고 다시 **//연산자**를 사용해 10으로 나눈 몫으로 구한다.

**100의 자리**는 100으로 나눈 몫으로 찾는다.

숫자들 사이에 **','**를 넣어 출력해야 한다. list를 unpack 연산자로 대괄호를 제거한 후 그냥 print하면 숫자 사이에 공백이 들어가니 `, sep = ','`로 바꿔 공백을 ,로 바꿔준다.

### 📒 코드

```python
numbers = []
for i in range(100,301):
    ones = i % 10
    tens = i % 100 //10
    hundreds = i // 100
    if (hundreds % 2 == 0) and (tens % 2 == 0) and (ones % 2 == 0):
        numbers.append(i)

print(*numbers, sep = ',')
```

### 🔍 결과 : **Pass**

