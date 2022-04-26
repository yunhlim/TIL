# [JavaScript] 변수와 식별자 [EP 02]

## 📌 식별자 정의

식별자(identifier)는 변수를 구분할 수 있는 변수명을 말한다. 간단히 말하면 변수에 붙이는 이름이다.

---

## 🎲 식별자 규칙

1. 식별자는 반드시 문자나 사용가능한 특수문자로 시작해야 한다.
2. 식별자는 특수문자로 **달러($)**, 밑줄(_)을 사용할 수 있다.
3. 대소문자를 구분한다.
4. 공백 문자를 포함할 수 없다.
5. 예약어를 사용할 수 없다.

---

## 🎨 식별자 작성 스타일

- 카멜 케이스(camelCase, lower-camel-case)
  - 변수, 객체 함수에 사용
- 파스칼 케이스(PascalCase, upper-camel-case)
  - 클래스, 생성자에 사용
- 대문자 스네이크 케이스(SNAKE_CASE)
  - 상수(constants)에 사용 : 변경하지 않을 값에 사용한다.

---

---

## 📌 변수 선언 키워드

### let

재할당 할 예정인 변수 선언 시 사용

변수 재선언이 불가능하다.

블록 스코프

- 블록 스코프 내에서는 변수 재선언이 가능하다.(블록 안에서만 사용한다.)

```javascript
// 재할당
let a = 1
a = '제주도'
console.log(a)	// 제주도

// 재선언
let a = 1
let a = 2		// error

// let 블록 스코프
let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName)	// 블록 스코프: Guido Van Rossum
}

console.log('전역 스코프:', fullName)	// 전역 스코프: Brendan Eich : 같은 스코프 내에 있는 값
```



### const

재할당 예정이 없는 변수 선언 시 사용

변수 재선언 불가능하다.

블록 스코프

> 블록 스코프 vs 함수 스코프
>
> `{}`안에서 선언한 변수는 `{}`안에서만 사용
>
> 조건문이나 반복문 안에 선언한 변수도 블록 스코프에 의해 `{}` 밖에서 사용할 수 없다.
>
> > 자바도 블록 스코프! 파이썬만 함수 스코프이다.

```javascript
// const 재할당
const a = 1
a = '제주도'	// error

// const 재선언
const a = 1
const a = 2		// error

// const 블록 스코프
let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  const language = 'Python'
}

console.log(language)	// error : language가 같은 스코프 내에 없다.
```



~~**var**~~

ES6 이전에 변수를 선언할 때 사용하던 키워드

재선언 및 재할당 모두 가능!

함수 스코프

호이스팅되는 특성으로 인해 예기치 못한 문제가 발생 가능하다.

따라서 ES6 이후부터는 var 대신 const, let을 사용하는 걸 권장!

> 호이스팅이란?
>
> var 변수를 선언하면 최상단으로 이동하는 현상이다. 따라서 할당보다 선언을 뒤에 적어도 선언문이 앞으로 자동으로 이동하여 먼저 실행된다.

```javascript
// var 재선언
var a = 1
var a = 2
console.log(a)			// 2


// var 함수 스코프
function f1() {
  var message = 'You are doing great!'
}
console.log(message)		// error


// var 블록 스코프
const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)		// dark+


// 호이스팅
console.log(hoisted)
var hoisted = 'can you see me?'		// can you see me?

console.log(lunch)
const lunch = '초밥'			// error

console.log(dinner)
let dinner = '스테이크'			// error
```

> 자바스크립트 표준 문법 상 let이나 const 모두 재선언하면 에러를 내는 것이 맞다.
>
> 크롬 브라우저의 console 창에서 재선언해도 error가 발생하지 않는다. why??
>
> 일반 스크립트 실행과 크롬 개발자 도구의 콘솔 간에 차이가 있다.
>
> 개발자 도구도 한 줄에 같이 실행시키거나, 다른 키워드로 재선언하는 경우 에러를 내지만, 같은 키워드를 재선언하는 경우는 에러를 발생하지 않으니 알아 놓도록 한다!!



