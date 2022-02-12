# [SWEA] 파이썬 프로그래밍 기초(1) - 반복문

링크 : https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDAe6AATw5UW6&subjectId=AWT4H-1q2m8DFAVT

---

## SWEA 6230. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 1

### 📚 문제

다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고, 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

```python
Input
없음

Output
1번 학생은 88점으로 합격입니다.
2번 학생은 30점으로 불합격입니다.
3번 학생은 61점으로 합격입니다.
4번 학생은 55점으로 불합격입니다.
5번 학생은 95점으로 합격입니다.
```

---

### 📒 코드

```python
std = [88, 30, 61, 55, 95]
success = ""
cnt = 0
for score in std:
    cnt += 1
    if score>=60 :
        success = "합격"
    else :
        success = "불합격"
    print(f'{cnt}번 학생은 {score}점으로 {success}입니다.')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6231. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 2

### 📚 문제

1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.

```python
Input
없음

Output
1
2
3
4
5
...
99
100
```

---

### 📒 코드

```python
for i in range(1, 101, 1):
    print(i)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6234. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 3

### 📚 문제

1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.

```
Input
없음

Output
2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100
```

---

### 📒 코드

print문을 그냥 쓰면 줄바꿈이 되므로 print( , end='')로 줄바꿈 안되게 바꾸어 준다!

```
for i in range(2,101,2):
    print(f'{i} ',end='')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6238. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 4 

### 📚 문제

1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

```
Input
없음

Output
1, 3, 5, 7, 9, ... 95, 97, 99
```

---

`,`를 확인 안해서 1차 Fail..

값 중간에 `,`를 넣어서 출력해야 하므로 List를 활용한다.

, 다음에 띄어쓰기가 있으니 `print(*list명, sep = ', ')`로 작성한다.

list 앞에 `*`을 붙여 `[]`를 지우고 출력한다.

### 📒 코드

```python
odds = []

for i in range(1,100,2):
    odds.append(i)

print(*odds, sep = ', ')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6240. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 5

### 📚 문제

1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

```
Input
없음



Output
1부터 100사이의 숫자 중 3의 배수의 총합: 1683
```

---

앞 두 문제랑 비슷한데 print가 더 쉬워서 간단히 clear~

### 📒 코드

```python
total = 0
for i in range(3,101,3):
    total += i
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {total}')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6242. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 6

### 📚 문제

다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.

['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.**

```
Input

없음



Output

{'A': 3, 'O': 3, 'B': 2, 'AB': 2}

```

---

출력 값이 딕셔너리 값이니 딕셔너리를 만들어서 값을 추가시켜 완성~

### 📒 코드

```python
bloods = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
bloods_dic = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

for i in bloods:
    if i == 'A':
        bloods_dic['A'] += 1
    elif i == 'O':
        bloods_dic['O'] += 1
    elif i == 'B':
        bloods_dic['B'] += 1
    else:
        bloods_dic['AB'] += 1

print(bloods_dic)

```

### 🔍 결과 : **Pass**

---

---

## SWEA 6244. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 7

### 📚 문제 

다음은 학생의 점수를 나타내는 리스트입니다.

[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

```
Input

없음



Output

454

```

---

`pop()`은 리스트 요소 끄집어내는 함수이다.

`a.pop()`하면 맨 마지막 요소를 삭제하고 `a.pop(index)`를 하면 index요소를 삭제한다.

다른 삭제 함수인 `remove()`는 값을 비교해서 제거한다. 리스트 순서 중 앞에꺼부터 제거한다.

index가 list의 길이를 넘어갈 때 예외처리를 이용해 while 문을 탈출한다.

예외처리 시 아무런 코드를 실행하고 싶지 않을 땐 `pass`를 사용한다.

### 📒 코드


```python
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0
index = 0
try:
    while True:
        under80s = 0
        index = 0

        while True:
            if scores[index] < 80:
                scores.pop(index)
                break
            else:
                index += 1
except IndexError:
    pass
index = 0
try:
    while True:
        total += scores[index]
        index += 1
except IndexError:
    pass
print(total)


```

### 🔍 결과 : **Pass**

---

---

## SWEA 6246. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 8

### 📚 문제 

while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

```
Input

없음



Output

*****

****

***

**

*

```

---

파이썬에서 문자열끼리 합이나 곱은 지원하지만 차나 나눗셈은 지원하지 않는다.

### 📒코드

```python
cnt = 0



while cnt < 5:

    star = 5-cnt

    cnt += 1

    print("*"*star)

```

### 🔍 결과 : **Pass**

---

---

## SWEA 6247. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 9

### 📚 문제

while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

```python
Input
없음

output
*******
 *****
  ***
   *
```

---

print할 때 정렬!!

**f-strings**에서 가운데 정렬 하기 위해서 `{:^10}`을 사용. 10 자리 중 가운데 정렬!

복습해보면

>{:<} 왼쪽 정렬는  
>
>{:>} 오른쪽 정렬 
>
>{:.3} 정수 포함 총 3자리 
>
>{:.3f} 소수점 3번째 자리까지

### 📒 코드

```python
star = '*'
cnt = 7
while True:
    if cnt > 0:
        print(f'{star*cnt:^7}')
    else:
        break
    cnt -= 2
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6249. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 10

### 📚 문제

다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

```
Input
11

Output
0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0
```

---

중첩 반복문을 이용해 표현한다.

첫 번째 for문에서 입력의 숫자를 하나씩 고르고, 두 번째 for문에서 if문을 활용해 0~9 중 같은 숫자에 추가해준다.

그러기 위해서 0~9의 갯수를 파악하기 위한 units 리스트를 만들어준다.

0으로 초기화된 리스트를 만들 때 길이만큼 [0]를 곱해준다. =>`[0]*10`

출력할 때 **unpack 연산자**를 활용해 range()와 리스트의 괄호를 없애고 출력한다.

### 📒 코드

```python
num = input()
units = [0]*10

for idx in num:
    for i in range(10):
        if int(idx) == i:
            units[i] += 1

print(*range(10))
print(*units)
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6251. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 11

### 📚 문제

for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

```python
Input
없음

Output
    *
   **
  ***
 ****
*****
```

---

{:>5}를 사용해서 오른쪽 정렬!

### 📒 코드

```python
star = '*'
for i in range(1,6):
    print(f'{star*i:>5}')
```

### 🔍 결과 : **Pass**

---

---

## SWEA 6253. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 13

### 📚 문제

다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

```python
Input
9

Output
1001
```

----

10진수를 2진수로 바꾸기 위해 while 문을 활용한다.
`%`와 `//`, 몫과 나머지를 활용해 2진수로 변환한다.
중간에 string 타입으로 바꿔주기 위해 `str()`함수를 사용한다.

2로 나누다가 마지막에 1이 남으면 `break`를 걸어서 탈출한다.

### 📒 코드

```python
jinsu_10 = int(input())
jinsu_2 = ''
while True:
    jinsu_2 = str(jinsu_10 % 2) + jinsu_2
    jinsu_10 = jinsu_10//2
    if jinsu_10 < 2:
        jinsu_2 = str(jinsu_10) + jinsu_2
        break
print(jinsu_2)
```

### 🔍 결과 : **Pass**