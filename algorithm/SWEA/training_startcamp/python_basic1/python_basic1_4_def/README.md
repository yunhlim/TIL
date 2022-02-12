# [SWEA] 파이썬 프로그래밍 기초(1) - 함수

링크 : https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDAe6AATw5UW6&subjectId=AWT4H-1q2m8DFAVT

---

## SWEA 6319. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 1

### 📚 문제

다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

```
Input
eye

Output
eye
입력하신 단어는 회문(Palindrome)입니다.
```

---

단어 순서를 거꾸로 바꾸기 위해 for문을 활용한다.

새로운 빈 문자열인 `word_rev`를 생성하고 for문이 입력받은 word를 순회한다.

그러면 word_rev의 왼쪽으로 하나씩 넣어주면 순서가 바뀌게 된다.

### 📒 코드

```python
word = input()


def reverse(word) :
    word_rev = ''
    for c in word:
        word_rev = c+word_rev
    print(word_rev)
    if word == word_rev :
        print('입력하신 단어는 회문(Palindrome)입니다.')
        
        
reverse(word)
```

### 🔍 결과: **Pass**

---

---

## SWEA 6320. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 2

### 📚 문제

다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

```python
Input
홍길동
이순신
가위
바위

Output
바위가 이겼습니다!
```

---

중첩반복문으로 하나하나 작성해서 해결..

바위가 이겼습니다!보단 이순신이 이겼습니다!가 맞을 것 같지만, 문제의 출력이 저러므로 저렇게 쓴다..

### 📒 코드

```python
user1 = input()
user2 = input()
user1rps = input()
user2rps = input()

def rps(a,b) :
    if a == "가위":
        if b == "가위":
            print('비겼습니다!')
        elif b == "바위":
            print('바위가 이겼습니다!')
        else :
            print('가위가 이겼습니다!')
    if a == "바위":
        if b == "가위":
            print('바위가 이겼습니다!')
        elif b == "바위":
            print('비겼습니다!')
        else :
            print('보가 이겼습니다!')
    if a == "보":
        if b == "가위":
            print('가위가 이겼습니다!')
        elif b == "바위":
            print('보가 이겼습니다!')
        else :
            print('비겼습니다!')

rps(user1rps,user2rps)      
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6321. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 3

### 📚 문제

소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가 소수인지를 판단하는 프로그램을 작성하십시오.

*소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력*

```
Input
13

Output
소수입니다.
```

---

소수를 출력하기 위한 함수를 만들어준다.

2부터 증가시키며 하나씩 입력한 숫자 값과 **%연산자**로 나누어떨어지는지 확인한다.

중간에 나누어떨어지면 자기자신 이외의 약수가 있는 것이므로 `소수가 아닙니다.`를 프린트한다.

입력한 숫자 값과 cnt가 같아지면 약수가 1과 자기 자신 이외에 없다는 것이므로 `소수입니다.`를 프린트한다.

### 📒 코드

```
a=int(input())

def sosu(a) :
    cnt = 1
    while True:
        cnt += 1
        if cnt == a :
            print("소수입니다.")
            break
        if a % cnt == 0 :
            print("소수가 아닙니다.")
            break
sosu(a)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6323. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 4

### 📚 문제

다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

```
Input
10

Output
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

---

앞의 두 수의 합이 다음 수인 피보나치 수열을 만들기 위해 함수 안에 정수형 변수 3개를 선언한다.

`[1,1]` list를 만들어 순차적으로 더해가며 다음 수를 채워간다.

for문으로 일정한 숫자만큼 반복한다.

### 📒 코드

```python
num = int(input())

def fibonaci(num):
    numbers = [1, 1]
    a = 1
    b = 1
    c = 0
    for i in range(num-2):
        c = a+b
        numbers.append(c)
        a = b
        b = c
    return numbers

print(fibonaci(10))
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6324. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 5

### 📚 문제

리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.

```
Input

없음

Output

[1, 2, 3, 4, 3, 2, 1]

[1, 2, 3, 4]

```

---

중복을 제거하기 위해 왼쪽 숫자부터 채우면서 왼쪽에 자신의 같은 숫자가 있는지 확인하며 채워나갔다.

### 📒 코드

```python
numbers = [1, 2, 3, 4, 3, 2, 1]

def only_numbers(numbers):
    only_nums = [numbers[0]]
    if numbers[0] != numbers[1]:
        only_nums.append(numbers[1])
    for i in range(2, len(numbers)-1):
        same = 0 
        for j in range(0, i):
            if numbers[i] == numbers[j]:
                same = 1
                break
        if same == 0:
            only_nums.append(numbers[i])
    return only_nums

print(numbers)
print(only_numbers(numbers))

```

---

**set**을 사용하면 중복된 걸 제거한다고 한다. 그 대신 **set**은 오름차순 정렬이므로 문제가 오름차순이라는 말이 없으면 조금 애매하다.

>set()에 리스트를 넣으면 대괄호에서 중괄호로 바뀌니 겉에 `list()함수`를 씌워준다. => `list(set(중복된 리스트))`
>
>```python
>numbers = [1, 2, 4, 3, 3, 2, 1]
>
>print(numbers)
>print(list(set(numbers)))
>```
>
>왼쪽 숫자부터 리스트에 넣으면서 다음 숫자들은 넣어진 리스트에 중복된 값이 있는지 비교하며 합쳐준다. 이렇게 푸는 방법이 가장 깔끔한 방법!

리스트의 값들과 비교하는 건 `a not in list` 으로 비교한다. 있는지 보려면 `a in list`를 사용한다.

### 📒 코드

```python
numbers = [1, 2, 3, 4, 3, 2, 1]

def only_numbers(nums):
    only_nums = []
    for i in nums:
        if i not in only_nums:
            only_nums.append(i)
    return only_nums

print(numbers)
print(only_numbers(numbers))

```

### 🔍 결과 : **Pass**

---

---

## SWEA 6325. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 6

### 📚 문제

정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고, 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

```
Input
없음

Output

[2, 4, 6, 8, 10]
5 => False
10 => True
```

---

특정 숫자를 찾기 위해 `if a in list`를 이용해 숫자가 list 안에 있는지 확인한다.

### 📒 코드

```python
numlist = [2, 4, 6, 8, 10]

def num_search(num, nums):
    if num in nums:
        print(f'{num} => True')
    else:
        print(f'{num} => False')

print(numlist)
num_search(5,numlist)
num_search(10,numlist)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6326. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 7

### 📚 문제

다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한 팩토리얼 값을 구하는 프로그램을 작성하십시오.

```
Input
5

Output
120
```

---

**재귀 함수**를 사용해서 해결해본다.

점화식을 써보면 `f(n) = n * f(n-1)` 이다.

초기 조건인 f(1) 값만 정의해주면 된다.

### 📒 코드

```python
number = int(input())

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)
        
print(factorial(number))
```

---

for 문으로도 해결해본다.

### 📒 코드

```python
number = int(input())

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

print(factorial(number))
```

### 🔍 결과 : **Pass**

점화식으로 나타내기 쉬우면 재귀함수를 사용하면 된다.

함수를 여러 번 통과하는게 for문보다 느리게 되니 알맞게 쓸 필요가 있다.

---

---

## SWEA 6327. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 8

### 📚 문제

숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

```
Input
2,3

Output
square(2) => 4
square(3) => 9
```

---

### 📒 코드

```python
a, b = map(int,input().split(','))
def square(num):
    print(f'square({num}) => {num**2}')

square(a)
square(b)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6328. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 9

### 📚 문제

인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고 결과를 출력하는 프로그램을 작성하십시오.

```
Input
one, three

Output
three
```

---

입력에 `,공백` 공백 한 칸이 있으므로

`.split(', ')` split 안에 `,공백`으로 적어서 해결

### 📒 코드

```python
a,b = input().split(', ')

def long_str(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        print("길이가 같습니다.")

print(long_str(a,b))
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6329. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 10

### 📚 문제

인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고, 이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오. 0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.

```
Input
없음

Output
카운트다운을 하려면 0보다 큰 입력이 필요합니다.
10
9
8
7
6
5
4
3
2
1
```

---

if 조건문을 이용해 1보다 작은 수가 들어오면 `"카운트다운을 하려면 0보다 큰 입력이 필요합니다."`를 출력한다. 1보다 큰 수가 들어오면 for 문을 활용해서 내림차순으로 출력한다.

### 📒 코드

```python
def countdown(num):
    if num > 0:
        for i in range(num,0,-1):
            print(i)
    else:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')

countdown(0)
countdown(10)
```

### 🔍 결과 : **Pass**