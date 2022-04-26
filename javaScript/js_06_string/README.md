# [JavaScript] 문자열(String) 메서드 [EP 06]

## 📌 includes

특정 문자열의 존재 여부를 참/ 거짓으로 반환

```javascript
const str = 'a santa at nasa'
str.includes('santa')	// true
str.includes('aaa')		// false
```

---

## 📌 split

`string.split(value)`

문자열을 value 기준으로 나눈 배열 반환

파이썬과 다르게 `split()`을 하면 기존 문자열을 공백을 기준으로 나누지 않고 그냥 한꺼번에 담아 반환한다.

```javascript
const str = 'a cup'
str.split()		// ['a cup']
str.split('')	// ['a', ' ', 'c', 'u', 'p']
str.split(' ')	// ['a', 'cup']
```

---

## 📌 replace

`string.replace(from, to)`

해당 문자열에 from이 존재하는 경우, 1개만 to 값으로 교체 후 반환

### replaceAll

`string.replaceAll(from, to)`

문자열의 모든 from 값을 to 값으로 교체 후 반환

```javascript
const str = 'a santa at nasa'
str.replace(' ', '')	// 'asanta at nasa'	: 첫번째 공백만 제거
str.replaceAll(' ', '')	// 'asantaatnasa' : 모든 공백 제거

const str = 'a b c d'
str.replace(' ', '-') // 'a-b c d'
str.replaceAll(' ', '-') // 'a-b-c-d'
```

---

## 📌 trim

문자열의 좌우 공백 제거하여 반환

공백문자 : 스페이스, 탭, 엔터 등

### trimStart

문자열 시작의 공백문자를 제거한 후 반환

### trimEnd

문자열 끝의 공백문자를 제거한 후 반환

```javascript
const str = '    hello    '
str.trim()		// 'hello'
str.trimStart()	// 'hello    '
str.trimEnd()	// '    hello'
```

