# [Python] 문자열 메소드(string method)

**불변한(immutable) 자료형**이라서 원본을 바꾸거나 추가할 수 없다. 바꾸거나 추가하여 반환!

---

---

## 탐색

`s.find(x)`: x의 첫 번째 위치인덱스를 반환, 없으면 -1을 반환, 문자열로 넣으면 가장 앞 문자의 위치 반환

`s.index(x)`: x의 첫 번째 위치인덱스를 반환, 없으면 **오류 발생**, 문자열로 넣으면 가장 앞 문자의 위치 반환

```python
s = 'ssafy'

print(s.find('a'))	#=> 2 : ssafy에서 a의 인덱스 반환
print(s.find('s'))	#=> 0 : ssafy에서 s들 중 가장 빨리 등장하는 0번째 인덱스 반환
print(s.find('ssa')) #=> 0 : 문자열은 가장 앞에 나오는 문자의 인덱스를 반환

print(s.index('a'))	#=> 2 : ssafy에서 a의 인덱스 반환
print(s.index('s'))	#=> 0 : ssafy에서 s들 중 가장 빨리 등장하는 0번째 인덱스 반환
print(s.index('ssa')) #=> 0 : 문자열은 가장 앞에 나오는 문자의 인덱스를 반환

print(s.find('e'))	#=> -1 : 없으면 -1 반환
print(s.index('e')) #=> ValueError: substring not found
```

**find와 index는 에러가 뜨는지 안뜨는지의 차이이다!**

---

`s.count(x)` : 부분 문자열을 센다. s에 들어있는 x의 개수 반환

```python
s = 'ssafy'

print(s.count('s'))	#=> 2 : ssafy에서 s의 개수인 2 반환
```

`s.isalpha()`: 문자로만 이루어져있는지 여부 확인, *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)로만 이루어져있으면 True, 숫자나 공백이 들어가 있으면 False 반환

---

`s.isupper()`: 대문자 여부, 대문자이면 True 아니면 False 반환

`s.islower()`: 소문자 여부

is가 들어가면 반환값이 boolean이다.

---

`s.istitle()`: 타이틀 형식 여부 => 공백, `'`을 기준으로 다음에 대문자가 오는지 확인

`s.isspace() `: 공백으로만 이루어져있으면 True  **공백에 \n, \t도 포함!!**

---

`s.startswith(x)` : 문자열이 x로 시작하면 True, 아니면 False

`s.endswith(x)` : 문자열이 x로 끝나면 True, 아니면 False

둘 다 공백이 있으면 False가 나온다.

---

---

## 변환(제거)

`s.replace(old, new[,count]) `

바꿀 대상 글자를 새로운 글자로 바꿔서 반환

count를 넣어 바꾸는 횟수를 지정해 줄 수 있다.

```python
s = 'abcabc'

print(s.replace('c', 'a'))
print(s.replace('c', 'a', 1))

'''
abaaba	# 문자열의 모든 c를 a로 변환
abaabc	# 지정해준 count인 1만큼 c를 a로 변환
'''
```

---

`s.strip([chars])`: 공백이나 특정 문자를 제거하여 반환(문자열을 지정하지 않으면 공백을 제거)

로그인할 때 많이 쓰인다. 공백을 제거해서 데이터 클린징할 때 사용한다.

양쪽을 제거:  `s.strip()`, 왼쪽을 제거: `s.lstrip()`, 오른쪽을 제거: `s.rstrip()`

```python
s = '  ssafy  '

print(s.strip()+'7')
print(s.lstrip()+'7')
print(s.rstrip()+'7')

'''
ssafy7		# 양쪽의 공백 제거
ssafy  7	# 왼쪽의 공백만 제거
  ssafy7	# 오른쪽의 공백만 제거

'''
```

문자열 중 하나씩 확인해 chars에 있는 문자를 제거한다. chars에 없는 문자가 있으면 종료한다.

```python
s = '  abcda  '

print(s.strip(' abc'))
print(s.lstrip(' abc'))
print(s.rstrip(' abc'))

''' ' abc'의 문자열 안에 있는 문자이면 제거한다. 문자열 안에 없으면 멈추고 반환
d			# 왼쪽의 공백과 abc를 제거하고 오른쪽은 a와 공백을 제거한다.
da  		# 왼쪽에서 공백과 abc를 제거하고 d를 만나면 멈추고 반환한다.
  abcd		# 오른쪽에서 공백과 a를 지우고 d를 만나면 멈추고 반환한다.
'''
```

strip은 문자열 사이사이 공백을 지울 순 없다.

**`s.replace(' ', '')` => 모든 공백을 제거할 수 있다.**

```python
s = ' a b c '

print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace(' ',''))

'''	replace는 모든 공백을 없애버린다. strip은 문자열 사이사이는 없애지 못한다.
a b c
a b c 
 a b c
abc
'''
```

---

`s.upper()` 소문자를 대문자로 변경하여 반환

`s.lower()` 대문자를 소문자로 변경하여 반환

`s.swapcase() `: 대소문자를 서로 변경하여 반환

`s.capaitalize()` : 맨 앞 글자를 대문자로 만들어 반환

---

---

## **가장 자주 쓰이는 문자열 메소드 join(), split()📌📌**

전에 올렸던 포스팅 참조: https://velog.io/@yunhlim/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9D%91%EC%9A%A9

`s.split(sep=None, maxsplit=-1)`

문자열을 특정한 단위로 나눠 **리스트**로 반환, 알고리즘에서 참 많이 쓰인다.

maxsplit이 default인 -1이면 제한이 없음.

---

`'separator'.join([iterable])`

반복가능한 컨테이너 요소들을 separtor(구분자)로 합쳐 문자열로 반환

sep이 None이면 공백문자를 단일한 공백문자로 간주하고, 선행 후행 공백은 빈 문자열에 포함X

**iterable에 문자열이 아닌 값이 있으면 TypeError 발생** int만 되어도 type error