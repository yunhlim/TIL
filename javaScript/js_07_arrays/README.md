# [JavaScript] 배열 (Arrays) [EP 07]

## 📌 배열의 정의와 특징

배열은 참조 타입의 객체(Objects)

파이썬과 같이 대괄호를 이용하여 생성하고,  순서를 보장한다.

파이썬과 다른 점은 0을 포함한 양의 정수 인덱스로만 접근 가능하고, -1 같은 인덱스로는 접근이 불가능하다!

배열의 길이는 `array.length`로 접근이 가능하다.



### Spread operator

spread operator(...)

배열 내부에서 배열을 전개 가능하다.

얕은 복사에 활용

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]
console.log(newArray)		// [0, 1, 2, 3, 4]
```

---

---

## 📚 배열의 메서드

### reverse

`array.reverse()`

원본 배열의 요소들의 순서를 반대로 정렬

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()	// [5, 4, 3, 2, 1]
```

---

### push

`array.push()`

배열의 가장 뒤에 요소를 추가 (파이썬의 append)

### pop

`array.pop()`

배열의 가장 뒤에 요소를 제거

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.push(100)		// [1, 2, 3, 4, 5, 100]
numbers.pop()			// [1, 2, 3, 4, 5]
```

---

### unshift

`array.unshift()`

배열의 가장 앞에 요소를 추가

### shift

`array.shift()`

배열의 가장 앞의 요소를 제거

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.unshift(100)		
console.log(numbers)	// [100, 1, 2, 3, 4, 5]
numbers.shift()

```

---

### includes

`array.includes(value)`

배열에 value가 있는지 판별 후 참 거짓 반환

```javascript
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.includes(1))		// true
console.log(numbers.includes(100))		// false
```

---

### indexOf

`array.indexOf(value)`

배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스를 반환

없으면 -1을 반환

```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3)		// 2
result = numbers.indexOf(100)	// -1
```

---

### join

`array.join([separator])`

배열의 모든 요소를 연결하여 반환

separator(구분자)를 지정, 생략 시 쉼표를 기본 값으로 사용

```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.join()		// 1,2,3,4,5
result = numbers.join('')	// '12345'
result = numbers.join(' ')	// '1 2 3 4 5'
result = numbers.join('-')	// '1-2-3-4-5'
```

---

---

## 🎯 Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드

- 메서드 호출 시 인자로 callback 함수를 받는 것이 특징

  > callback 함수란?
  >
  > 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수
  >
  > 콜백 함수는 3가지 매개변수로 구성
  >
  > element : 배열의 요소
  >
  > index : 배열 요소의 인덱스
  >
  > array : 배열 자체

### forEach

배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

break나 continue를 사용할 수 없다.

> for ... of 보다 forEach를 쓰는 걸 Airbnb Style Guide에서 권장한다!!

**반환 값 없음**

```javascript
    const colors = ['red', 'green', 'blue']
    const noresult = colors.forEach((color, index, list) => {
      // 할일(작업) 콜백함수
      console.log(`${index}번 색상은 ${color}`)
      console.log(list)
    })
    /*
    0번 색상은 red
	['red', 'green', 'blue']
	1번 색상은 green
	['red', 'green', 'blue']
	2번 색상은 blue
	['red', 'green', 'blue']
    */
```

---

### map

배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

콜백 함수의 반환 값을 요소로 하는 새로운 배열을 반환

```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNumbers = numbers.map((number) => {
    return number * 2
})
console.log(doubleNumbers)		// [2, 4, 6, 8, 10]
```

---

### filter

콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환

```javascript
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num) => {
    return num % 2
})
console.log(oddNums)	// [1, 3, 5]
```

---

### reduce

조금 어렵다.

콜백 함수의 반환 값들을 하나의(acc)에 누적 후 반환

acc는 return 값으로 갱신한다. 그리고 reduce의 인자로 acc의 초기값을 넣어준다.

```javascript
numbers = [1, 2, 3]
const result =  numbers.reduce((acc, element) => {
    console.log(`바톤은 ${acc}, element는 ${element}`)
    return acc + element
}, 0)
console.log(result)
/*
바톤은 0, element는 1
바톤은 1, element는 2
바톤은 3, element는 3
6
*/
```

---

### find

콜백 함수의 반환 값이 참이면 해당 요소를 반환

찾는 값이 배열에 없다면 undefined를 반환한다.

```javascript
const avengers = [
    { name: 'Tony Stark', age: 45},
    { name: 'Steve Rogers', age: 32},
    { name: 'Thor', age: 40000}
]

const findAvenger = avengers.find((avenger) => {
    return avenger.name == 'Thor'
})
console.log(findAvenger)		// {name: 'Thor', age: 40000}
```

---

### some

배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환

빈 배열은 항상 거짓을 반환한다.

유효성 검사할 때 유용하다.

```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some(num => {
    return num % 2 === 0 // 짝수
})
console.log(hasEvenNumber) // false
```

---

### every

배열의 모든 요소가 판별 함수를 통과하면 참을 반환

빈 배열은 항상 참을 반환한다.(통과하지 못하는 배열을 찾는 것이다.)

```javascript
const numbers = [2, 4, 6, 8, 10, 1]

const isEveryNumberEven = numbers.every(num => {
    return num % 2 === 0 // 짝수
})
console.log(isEveryNumberEven)	// false
```

