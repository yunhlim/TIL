# [JavaScript] 자바스크립트의 조건문과 반복문 [EP 04]

> 조건문과 반복문 둘 다 중괄호 안에 작성하니 **블록 스코프**를 생성한다.



## 🏓 조건문

조건식을 작성할 때 `==`가 아닌 `===`로 작성해야 형변환을 하지 않고 비교할 수 있다.

### if 문

조건은 소괄호 안에 작성!

실행할 코드는 중괄호`{}` 안에 작성

>  if (expression) {
>      // 코드1
>  } else if (expression) {
>      // 코드2
>  } else {
>      // 코드3
>  }

```javascript
const username = 'admin'
if (username === 'admin') {
  console.log("관리자님 환영합니다.")
} else if (username === 'manager') {
  console.log("매니저님 환영합니다.")
} else {
  console.log(`${username}님 환영합니다.`)	// 매니저님 환영합니다.
}
```

### switch 문

python에는 없는 조건식이다.

여러가지 조건을 나누어서 비교할 때 사용할 수 있다.

조건이 조금이나마 복잡하면 switch 문을 쓸 수 없다.

break문을 안 걸어주면 이후 모든 케이스문의 내용을 확인한다.

> switch(expression) {
>     case 'first value': {
>         // 내용1
>         break
>     }
>     case 'second value': {
>         // 내용2
>         break
>     }
>     default:{
>      	// 내용3
>     }
> }

```javascript
const numOne = 10
const numTwo = 100
const operator = '+'

switch(operator) {
  case '+': {
    console.log(numOne + numTwo)	// 110
    break
  }
  case '-': {
    console.log(numOne - numTwo)
    break
  }
  case '*': {
    console.log(numOne * numTwo)
    break
  }
  case '/': {
    console.log(numOne / numTwo)
    break
  }
  default:{
    console.log("유효하지 않은 연산자입니다.")
  }
}
```

---

## 🎯 반복문

### while

조건문이 참인 동안 반복 시행

조건은 소괄호, 실행할 코드는 중괄호에 작성

> while (condition) {
>
> ​	// do something
>
> }

```javascript
let evenNumber = 0

while (evenNumber < 6) {
  evenNumber += 2
  console.log(evenNumber)
}
/*
2
4
6
*/
```



### for

전통적인 방법, c나 자바에서 쓰는 방법이다.

> for (초기값; 조건식; 변화식) {
>
> ​	// 내용
>
> }

```javascript
let oddNumber = 1

for (let i = 0; i < 5; i++) {
  oddNumber += 2
  console.log(oddNumber)
}
/*
3
5
7
9
11
*/
```



### for ... in

object 순회할 때 사용한다. 배열에 사용하면 index 값을 가져온다.

JS 객체의 value는 점(.) 또는 대괄호 표기법을 이용하여 key값을 통해 접근 가능. ex) obj.key, obj[key]

```javascript
const bestMovie = {
  title: '벤자민 버튼의 시간은 거꾸로 간다',
  releaseYear: 2008,
  actors: ['브래드 피트', '케이트 블란쳇'],
  genres: ['romance', 'fantasy'],
}

for (key in bestMovie) {
  console.log(`${key}: ''${bestMovie[key]}''`)
}
/*
title: '벤자민 버튼의 시간은 거꾸로 간다'
releaseYear: '2008'
actors: '브래드 피트,케이트 블란쳇'
genres: 'romance,fantasy'
*/
```



### for ... of

배열을 순회할 때 사용한다. object를 순회하려고 하면 에러 발생

```javascript
const movies = [
  {title: '어바웃 타임'},
  {title: '굿 윌 헌팅'},
  {title: '인턴'},
]

for (movie of movies) {
  console.log(movie)
}
/*
{title: '어바웃 타임'}
{title: '굿 윌 헌팅'}
{title: '인턴'}
*/
```

