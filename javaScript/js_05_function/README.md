# [JavaScript] 함수(Function) [EP 05]

## 📌 함수란?

참조 타입이다. (주소를 저장하는 것!)

자료형은 function이다.

> 일급 객체(파이썬, 자바스크립트에 존재)
>
> 변수에 할당 가능
>
> 함수의 매개변수로 전달 가능
>
> 함수의 반환 값으로 사용 가능

---

## 📒 함수 선언식

가장 일반적인 형태이다.

3가지 부분으로 구성

- 함수명
- 매개변수
- 몸통 (내용)

```javascript
function add(num1, num2) {
    return num1 + num2
}
add(1, 2)	// 3

// 입력받은 비밀번호가 8자 이상인 경우만 true
function isValid (password) {
	if (password.length < 8) {
		return false
	} else {
		return true
	}
}
console.log(isValid('abcd'))	// false
```



## 📗 함수 표현식

함수를 표현식 내에서 정의

함수의 이름을 생략하고 익명 함수로 정의할 수 있다.

따라서 매개변수와 몸통은 필요하고 함수명은 넣던지 생략하던지 할 수 있다.

```javascript
const join = function (array, separator) {
	let ret = ''
	let cnt = 0
	for (str of array) {
		cnt++
		ret += str
		if (cnt < array.length) {
			ret += separator
		}
	}
	return ret
}
console.log(join(['010', '1234', '5678'], '-'))		// 010-1234-5678
```



## 💥 함수 선언식과 표현식 비교

### 공통점

- function 타입

### 차이점

- 함수 선언식은 익명 함수 불가능, 호이스팅 가능
- 함수 표현식은 익명 함수 가능, 호이스팅 X (Airbnb 스타일 가이드 권장 방식)

함수 표현식을 var 키워드로 작성하면 에러 발생!



## 📖 함수의 여러 기능

### 기본인자

인자 작성할 때 `=`뒤에 기본인자를 선언한다. (파이썬과 같다.)

```javascript
const greeting = function (name = 'yunh') {
    console.log(`hi ${name}`)
}
greeting()			// hi yunh

// 주문서 작성
makeOrder = function (menu, size = 'regular') {
	const order = {
		menu,
		size,
	}
	return order
}
console.log(makeOrder('mocha'))		// {menu: 'mocha', size: 'regular'}
```



### 매개변수와 인자의 개수 불일치 허용

매개변수보다 인자의 개수가 많은 경우에는 초과한 인자를 버린다.

매개변수보다 인자의 개수가 적은 경우에는 undefined로 넣어서 사용한다.

```javascript
const noArgs = function () {
    return 0
}

noArgs(1, 2, 3) // 0

const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

console.log(threeArgs()) // [undefined, undefined, undefined]    매개변수보다 인자의 개수가 적은 경우
console.log(threeArgs(1)) // [1, undefined, undefined]
console.log(threeArgs(1, 2)) // [1, 2, undefined]
console.log(threeArgs(1, 2, 3, 4)) // [1, 2, 3]		매개변수보다 인자의 개수가 많은 경우
```



### REST Parameter

파이썬의 *args와 유사하다.

함수의 선언문의 파라미터에서 쓰는 것, 가변인자를 하나의 배열로 받는다.

인자가 없는 경우는 빈 배열

```javascript
const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs];
};
restOpr(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]] 
restOpr(1, 2) // [1, 2, []]
```



### Spread operator

...이 파이썬에서의 `*` 언팩연산자 역할을 한다.

함수 호출문에서 쓴다. 배열이 해당 매개변수로 각각 매핑된다.

즉, 인자로 넣을 때 괄호를 제거 후 값을 넣어줄 수 있다.

```javascript
const spreadOpr = function (arg1, arg2, arg3, arg4) {
	return arg1 + arg2 + arg3 + arg4
}

const numbers = [1, 2, 3]

spreadOpr(...numbers, 4)			// 10
```



## Arrow Function(화살표 함수)

함수를 비교적 간단하게 정의할 수 있다.

1. function 키워드를 삭제한다.
2. `( 매개변수 ) => { 몸통 }` 으로 나타낸다.
3. 매개변수가 하나이면 `()`를 제거하고 작성해도 된다.
4. 몸통이 한 줄이라면 `{}`를 제거한 후 return을 삭제해서 적으면 된다.

```javascript
// function 키워드 삭제, 매개변수 () 삭제
const celsiusToFaherenheit = celsius => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}
console.log(celsiusToFaherenheit(30))		// 86

// function 키워드 삭제, 매개변수 () 삭제, 몸통 {}과 return 삭제
const arrow = name => `hello, ${name}`
console.log(arrow('yunh'))					// hello, yunh
```

나중에 객체를 다루면서 Arrow Function의 쓰임새에 대해 더 배운다!