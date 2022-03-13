# [Baekjoon] Solved.ac Class 1 문제 풀이

## 1000. A+B [B5]

```python
A, B = map(int,input().split())
print(A+B)
```

## 1001. A-B [B5]

```python
A, B = map(int,input().split())
print(A-B)
```

## 1008. A/B [B4]

```python
A, B = map(int,input().split())
print(A/B)
```

## 1152. 단어의 개수 [B2]

```python
length = len(input().split())   # list에 나누어 넣어준다.
print(length)
```

## 1330. 단어 공부 [B2]

```python
length = len(input().split())   # list에 나누어 넣어준다.
print(length)
```

## 1330. 두 수 비교하기 [B4]

```python
A, B = map(int,input().split())

if A < B:
    print('<')
elif A > B:
    print('>')
else: print('==')
```

## 2438. 별 찍기 - 1 [B3]

```python
N = int(input())

for i in range(1, N+1):
    print('*'*i)
```

## 2439. 별 찍기 - 2 [B3]

```python
N = int(input())

for i in range(1, N+1):
    string = '*'*i
    print(f'{string:>{N}}')
```

## 2475. 검증수 [B5]

```python
nums = map(int,input().split())
sum = 0
for i in nums:
    sum += i**2
print(sum % 10)
```

## 2753. 윤년 [B4]

```python
year = int(input())

if (year % 4 == 0) and ((year % 100) or (year % 400 == 0)):
    print(1)
else: print(0)
```

## 9498. 시험 성적 [B4]

```python
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else: print('F')
```

## 10171. 고양이 [B5]

```python
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')
```

## 10172. 개 [B5]

```python
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|')
```

## 10869. 사칙연산 [B5]

```python
A, B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
```

## 10998. AxB [B5]

```python
A, B = map(int,input().split())
print(A*B)
```

## 11654. 아스키 코드 [B5]

```python
print(ord(input()))
```

## 10950. A+B - 3 [B3]

```python
for _ in range(int(input())):
    print(sum(map(int, input().split())))
```

## 10952. A+B - 5 [B3]

```python
while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    print(a + b)
```