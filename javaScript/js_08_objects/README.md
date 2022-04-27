# [JavaScript] 객체(Object) [EP 08]

## 📌 객체(Object)

객체는 속성의 집합, 중괄호 내부에 key와 value의 쌍으로 표현한다.

객체의 key는 문자열 타입만 가능하다.

- key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

객체의 요소 접근에는 `[]`(대괄호), `.`(점)으로 접근 가능하다.

- key에 띄어쓰기가 있는 경우는 [] 만 가능

```javascript
const me = {
  name: 'jack',
  phoneNumber: '01012345678',
  'samsung products': {
    buds: 'Galaxy Buds pro',
    galaxy: 'Galaxy s20',
  },
};
console.log(me.name);
console.log(me.phoneNumber);
console.log(me['samsung products']);
console.log(me['samsung products'].buds);
/*
jack
01012345678
{buds: 'Galaxy Buds pro', galaxy: 'Galaxy s20'}
Galaxy Buds pro
*/

// 맵 객체 추가하기!!
const newUsers = users.map(user => {
    user['isAlive'] = true			// 대괄호로 접근
	// user.isAlive = true			// 점으로 접근
    return user 
})
console.log(newUsers)	// users 객체의 각각의 속성에 isAlive = true가 추가된다.
```

---

## 🔍 메서드

메서드는 객체의 속성이 참조하는 함수이다.

`객체.메서드명()`으로 호출

메서드 내부에서는 this 키워드가 객체를 의미한다.

- `fullName`은 메서드가 아니기 때문에 정상출력 되지 않음(NaN)
- `getFullName`은 메서드이기 때문에 해당 객체의 `firstName` 과 `lastName`을 정상적으로 이어서 반환

```javascript
const me = {
	firstName: 'John',
	lastName: 'Doe',
	fullName: this.firstName + this.lastName,	// error : 메서드만 this에 접근한다. 여기서는 window에 접근
	getFullName: function () {
		return this.firstName + this.lastName	// this로 해당 객체에 접근한다.
	}
}
```

---

## 📒 this

- JS의 `this`는 실행 문맥(execution context)에 따라 다른 대상을 가리킨다.

- class 내부의 생성자 함수 (python의 `self` 와 같음)

- 메서드(객체.메서드명() 으로 호출 가능한 함수)

  ```jsx
  function getFullName() {
  	return this.firstName + this.lastName
  }
  
  const me = {
  	firstName: 'John',
  	lastName: 'Doe',
  	getFullName: getFullName,
  }
  
  const you = {
  	firstName: 'Jack',
  	lastName: 'Lee',
  	getFullName: getFullName
  }
  
  me.getFullName() // JohnDoe (this === me)
  you.getFullName() // JackLee (this === you)
  getFullName()  // NaN (this === window
  ```

  - `this`는 해당 메서드가 소속된 객체를 가리킴
  - 위 경우, `getFullName` 함수는 독립 실행 문맥에서는 객체에 소속되어있지 않기 때문에 제대로 동작하지 않음
  - `me` 객체의 메서드로 호출되는 문맥에서는 `this`가 `me`를 가리킴

- 위의 두가지 경우를 제외하면 모두 최상위 객체(`window`)를 가리킴.



### `function` 키워드와 화살표 함수 차이

화살표 함수가 객체에서 쓰이면 좋은 이유!!

```jsx
const obj = {
	PI: 3.14,
	radiuses: [1, 2, 3, 4, 5],
	printArea: function () {
		this.radiuses.forEach(function (r) {
			console.log(this.PI * r * r)
		}.bind(this))
	},
}

obj.printArea()
const obj = {
	PI: 3.14,
	radiuses: [1, 2, 3, 4, 5],
	printArea: function () {
		this.radiuses.forEach((r) => {
			console.log(this.PI * r * r)
		})
	},
}

obj.printArea()
```

- `this.radiuses`는 메서드(`객체.메서드명()`으로 호출 가능) 소속이기 때문에 정상적으로 접근 가능

  `forEach`의 콜백함수의 경우 메서드가 아님(`객체.메서드명()`으로 호출 불가능)

  - 때문에 콜백함수 내부의 this는 window가 되어 this.PI는 정상적으로 접근 불가능

- 이 콜백함수 내부에서 this.PI에 접근하기 위해서 함수객체.bind(this) 메서드를 사용.(없으면 `this`가 `window` 객체를 가르키게 되서 `NaN` 에러가 난다.)

- 이 번거로운 `bind` 과정을 없앤 것이 화살표 함수

---

## 🎯 Object 축약 문법 (ES6+)

### 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 아래와 같이 축약 가능

```jsx
// ES5	: 속성명 축약 X
var books = ['Learning JS', 'Learning Python']
var magazines = ['Vogue', 'Science']

var bookShop = {
	books: books,
	magazines: magazines,
}
console.log(bookShop)

// ES6+	: 속성명 축약 O
const books = ['Learning JS', 'Learning Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
	books,
	magazines,
}
console.log(bookShop)
```

### 메서드명 축약

- ES6+부터는 메소드(Object 내에 정의된 함수)를 선언할 때, `function` 키워드를 생략한 축약 가능
- 메서드를 정의할 때에만 적용한다.

```jsx
// ES5
var obj = {
  greeting: function () {
    console.log('Hi!')
  }
};

obj.greeting() // Hi!

// ES6+ (축약 문법 사용)
const obj = {
  greeting() {		// function 제거
    console.log('Hi!')
  }
};

newObj.greeting() // Hi!
```

### **Computed Property Name**

- 객체의 key 값을 표현식을 이용하여 동적으로 설정 가능
- 해당하는 값이 바뀌면 따라서 바뀌도록 설정해주는 것

```jsx
const key = 'regions'
const value = ['광주', '대전', '구미', '서울']

const ssafy = {
  [key]: value,
}

console.log(ssafy) 		   // { regions: Array(4) } 
console.log(ssafy.regions) // ["광주", "대전", "구미", "서울"]
```

### **Object Destructuring**

- Object에서 특정 key에 해당하는 값을 쉽게 변수에 할당하는 방법

```jsx
const userInformation = {
  name: 'ssafy kim', 
  userId: 'ssafyStudent1234',
  phoneNumber: '010-1234-1234',
  email: 'ssafy@ssafy.com'
}
```

**ES5** : 적용 X

```jsx
const name = userInformation.name
const userId = userInformation.userId
const phoneNumber = userInformation.phoneNumber
const email = userInformation.email 

console.log(name, userId, phoneNumber, email)
// ssafy kim ssafyStudent1234 010-1234-1234 ssafy@ssafy.com
```

**ES6+** : 적용 O

```javascript
const { name } = userInformation
const { userId } = userInformation
const { phoneNumber } = userInformation
const { email } = userInformation
console.log(name, userId, phoneNumber, email)
// ssafy kim ssafyStudent1234 010-1234-1234 ssafy@ssafy.com

const { name, userId, phoneNumber, email } = userInformation
console.log(name, userId, phoneNumber, email)
// ssafy kim ssafyStudent1234 010-1234-1234 ssafy@ssafy.com


// 함수의 인자로 사용하는 경우도 object destructuring 적용
const savedFile = {
    name: 'profile',
    extension: 'jpg',
    size: 29930
}

function fileSummary({name, extension, size}) {		// 여기서 적용한다!
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}

fileSummary(savedFile)
```



## 📗 JSON (JavaScript Object Notation)

- key - value 의 형태로 JS Object 와 유사한 모습으로 데이터를 표현하는 표기법
- 모습만 비슷할 뿐이고 실제로는 문자열 타입
- Object처럼 사용하기 위해서는 parsing(구문 분석) 작업이 필수
- JSON 형식의 파일을 다루기 위해 JS에서는 `JSON` 내장 객체를 제공

**Object → JSON(string)**

```jsx
const jsonData = JSON.stringify({
	coffee: 'Americano',
	iceCream: 'Cookie and cream',
})

console.log(jsonData)         //  "{"coffee":"Americano","iceCream":"Cookie and cream"}"
console.log(typeof jsonData)  // string
```

**JSON(string) → Object**

```jsx
const parsedData = JSON.parse(jsonData)

console.log(parsedData)         // {coffee: "Americano", iceCream: "Cookie and cream"}
console.log(typeof parsedData)  // object
```

