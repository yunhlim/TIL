# [JavaScript] ๊ฐ์ฒด(Object) [EP 08]

## ๐ ๊ฐ์ฒด(Object)

๊ฐ์ฒด๋ ์์ฑ์ ์งํฉ, ์ค๊ดํธ ๋ด๋ถ์ key์ value์ ์์ผ๋ก ํํํ๋ค.

๊ฐ์ฒด์ key๋ ๋ฌธ์์ด ํ์๋ง ๊ฐ๋ฅํ๋ค.

- key ์ด๋ฆ์ ๋์ด์ฐ๊ธฐ ๋ฑ์ ๊ตฌ๋ถ์๊ฐ ์์ผ๋ฉด ๋ฐ์ดํ๋ก ๋ฌถ์ด์ ํํ

๊ฐ์ฒด์ ์์ ์ ๊ทผ์๋ `[]`(๋๊ดํธ), `.`(์ )์ผ๋ก ์ ๊ทผ ๊ฐ๋ฅํ๋ค.

- key์ ๋์ด์ฐ๊ธฐ๊ฐ ์๋ ๊ฒฝ์ฐ๋ [] ๋ง ๊ฐ๋ฅ

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

// ๋งต ๊ฐ์ฒด ์ถ๊ฐํ๊ธฐ!!
const newUsers = users.map(user => {
    user['isAlive'] = true			// ๋๊ดํธ๋ก ์ ๊ทผ
	// user.isAlive = true			// ์ ์ผ๋ก ์ ๊ทผ
    return user 
})
console.log(newUsers)	// users ๊ฐ์ฒด์ ๊ฐ๊ฐ์ ์์ฑ์ isAlive = true๊ฐ ์ถ๊ฐ๋๋ค.
```

### ์ฃผ๋ก ์ฐ์ด๋ ๊ฐ์ฒด : String, Date ..

String์ EP 06์์ ๋ฐ๋ก ๋ค๋ฃจ์๋ค.

Date๋ ์๊ฐ ๊ฐ์ฒด๋ฅผ ๋ฐ์์ ์ฌ์ฉํ  ์ ์๋ค.

๐ [Date ๊ณต์ ๋ฌธ์](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date) ๋ฅผ ์ฐธ๊ณ !!

```javascript
const now = new Date()			// Date ๊ฐ์ฒด์ ์ธ์คํด์ค ๋ง๋ค๊ธฐ
// Date ๊ฐ์ฒด์ ๋ฉ์๋ ์ฌ์ฉ
const hour = now.getHours()		
const minute = now.getMinutes()
const second = now.getSeconds()
```

---

## ๐ ๋ฉ์๋

๋ฉ์๋๋ ๊ฐ์ฒด์ ์์ฑ์ด ์ฐธ์กฐํ๋ ํจ์์ด๋ค.

`๊ฐ์ฒด.๋ฉ์๋๋ช()`์ผ๋ก ํธ์ถ

๋ฉ์๋ ๋ด๋ถ์์๋ this ํค์๋๊ฐ ๊ฐ์ฒด๋ฅผ ์๋ฏธํ๋ค.

- `fullName`์ ๋ฉ์๋๊ฐ ์๋๊ธฐ ๋๋ฌธ์ ์ ์์ถ๋ ฅ ๋์ง ์์(NaN)
- `getFullName`์ ๋ฉ์๋์ด๊ธฐ ๋๋ฌธ์ ํด๋น ๊ฐ์ฒด์ `firstName` ๊ณผ `lastName`์ ์ ์์ ์ผ๋ก ์ด์ด์ ๋ฐํ

```javascript
const me = {
	firstName: 'John',
	lastName: 'Doe',
	fullName: this.firstName + this.lastName,	// error : ๋ฉ์๋๋ง this์ ์ ๊ทผํ๋ค. ์ฌ๊ธฐ์๋ window์ ์ ๊ทผ
	getFullName: function () {
		return this.firstName + this.lastName	// this๋ก ํด๋น ๊ฐ์ฒด์ ์ ๊ทผํ๋ค.
	}
}
```

---

## ๐ this

- JS์ `this`๋ ์คํ ๋ฌธ๋งฅ(execution context)์ ๋ฐ๋ผ ๋ค๋ฅธ ๋์์ ๊ฐ๋ฆฌํจ๋ค.

- class ๋ด๋ถ์ ์์ฑ์ ํจ์ (python์ `self` ์ ๊ฐ์)

- ๋ฉ์๋(๊ฐ์ฒด.๋ฉ์๋๋ช() ์ผ๋ก ํธ์ถ ๊ฐ๋ฅํ ํจ์)

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

  - `this`๋ ํด๋น ๋ฉ์๋๊ฐ ์์๋ ๊ฐ์ฒด๋ฅผ ๊ฐ๋ฆฌํด
  - ์ ๊ฒฝ์ฐ, `getFullName` ํจ์๋ ๋๋ฆฝ ์คํ ๋ฌธ๋งฅ์์๋ ๊ฐ์ฒด์ ์์๋์ด์์ง ์๊ธฐ ๋๋ฌธ์ ์ ๋๋ก ๋์ํ์ง ์์
  - `me` ๊ฐ์ฒด์ ๋ฉ์๋๋ก ํธ์ถ๋๋ ๋ฌธ๋งฅ์์๋ `this`๊ฐ `me`๋ฅผ ๊ฐ๋ฆฌํด

- ์์ ๋๊ฐ์ง ๊ฒฝ์ฐ๋ฅผ ์ ์ธํ๋ฉด ๋ชจ๋ ์ต์์ ๊ฐ์ฒด(`window`)๋ฅผ ๊ฐ๋ฆฌํด.



### `function` ํค์๋์ ํ์ดํ ํจ์ ์ฐจ์ด

ํ์ดํ ํจ์๊ฐ ๊ฐ์ฒด์์ ์ฐ์ด๋ฉด ์ข์ ์ด์ !!

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

- `this.radiuses`๋ ๋ฉ์๋(`๊ฐ์ฒด.๋ฉ์๋๋ช()`์ผ๋ก ํธ์ถ ๊ฐ๋ฅ) ์์์ด๊ธฐ ๋๋ฌธ์ ์ ์์ ์ผ๋ก ์ ๊ทผ ๊ฐ๋ฅ

  `forEach`์ ์ฝ๋ฐฑํจ์์ ๊ฒฝ์ฐ ๋ฉ์๋๊ฐ ์๋(`๊ฐ์ฒด.๋ฉ์๋๋ช()`์ผ๋ก ํธ์ถ ๋ถ๊ฐ๋ฅ)

  - ๋๋ฌธ์ ์ฝ๋ฐฑํจ์ ๋ด๋ถ์ this๋ window๊ฐ ๋์ด this.PI๋ ์ ์์ ์ผ๋ก ์ ๊ทผ ๋ถ๊ฐ๋ฅ

- ์ด ์ฝ๋ฐฑํจ์ ๋ด๋ถ์์ this.PI์ ์ ๊ทผํ๊ธฐ ์ํด์ ํจ์๊ฐ์ฒด.bind(this) ๋ฉ์๋๋ฅผ ์ฌ์ฉ.(์์ผ๋ฉด `this`๊ฐ `window` ๊ฐ์ฒด๋ฅผ ๊ฐ๋ฅดํค๊ฒ ๋์ `NaN` ์๋ฌ๊ฐ ๋๋ค.)

- ์ด ๋ฒ๊ฑฐ๋ก์ด `bind` ๊ณผ์ ์ ์์ค ๊ฒ์ด ํ์ดํ ํจ์

---

## ๐ฏ Object ์ถ์ฝ ๋ฌธ๋ฒ (ES6+)

### ์์ฑ๋ช ์ถ์ฝ

- ๊ฐ์ฒด๋ฅผ ์ ์ํ  ๋ key์ ํ ๋นํ๋ ๋ณ์์ ์ด๋ฆ์ด ๊ฐ์ผ๋ฉด ์๋์ ๊ฐ์ด ์ถ์ฝ ๊ฐ๋ฅ

```jsx
// ES5	: ์์ฑ๋ช ์ถ์ฝ X
var books = ['Learning JS', 'Learning Python']
var magazines = ['Vogue', 'Science']

var bookShop = {
	books: books,
	magazines: magazines,
}
console.log(bookShop)

// ES6+	: ์์ฑ๋ช ์ถ์ฝ O
const books = ['Learning JS', 'Learning Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
	books,
	magazines,
}
console.log(bookShop)
```

### ๋ฉ์๋๋ช ์ถ์ฝ

- ES6+๋ถํฐ๋ ๋ฉ์๋(Object ๋ด์ ์ ์๋ ํจ์)๋ฅผ ์ ์ธํ  ๋, `function` ํค์๋๋ฅผ ์๋ตํ ์ถ์ฝ ๊ฐ๋ฅ
- ๋ฉ์๋๋ฅผ ์ ์ํ  ๋์๋ง ์ ์ฉํ๋ค.

```jsx
// ES5
var obj = {
  greeting: function () {
    console.log('Hi!')
  }
};

obj.greeting() // Hi!

// ES6+ (์ถ์ฝ ๋ฌธ๋ฒ ์ฌ์ฉ)
const obj = {
  greeting() {		// function ์ ๊ฑฐ
    console.log('Hi!')
  }
};

newObj.greeting() // Hi!
```

### **Computed Property Name**

- ๊ฐ์ฒด์ key ๊ฐ์ ํํ์์ ์ด์ฉํ์ฌ ๋์ ์ผ๋ก ์ค์  ๊ฐ๋ฅ
- ํด๋นํ๋ ๊ฐ์ด ๋ฐ๋๋ฉด ๋ฐ๋ผ์ ๋ฐ๋๋๋ก ์ค์ ํด์ฃผ๋ ๊ฒ

```jsx
const key = 'regions'
const value = ['๊ด์ฃผ', '๋์ ', '๊ตฌ๋ฏธ', '์์ธ']

const ssafy = {
  [key]: value,
}

console.log(ssafy) 		   // { regions: Array(4) } 
console.log(ssafy.regions) // ["๊ด์ฃผ", "๋์ ", "๊ตฌ๋ฏธ", "์์ธ"]
```

### **Object Destructuring**

- Object์์ ํน์  key์ ํด๋นํ๋ ๊ฐ์ ์ฝ๊ฒ ๋ณ์์ ํ ๋นํ๋ ๋ฐฉ๋ฒ

```jsx
const userInformation = {
  name: 'ssafy kim', 
  userId: 'ssafyStudent1234',
  phoneNumber: '010-1234-1234',
  email: 'ssafy@ssafy.com'
}
```

**ES5** : ์ ์ฉ X

```jsx
const name = userInformation.name
const userId = userInformation.userId
const phoneNumber = userInformation.phoneNumber
const email = userInformation.email 

console.log(name, userId, phoneNumber, email)
// ssafy kim ssafyStudent1234 010-1234-1234 ssafy@ssafy.com
```

**ES6+** : ์ ์ฉ O

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


// ํจ์์ ์ธ์๋ก ์ฌ์ฉํ๋ ๊ฒฝ์ฐ๋ object destructuring ์ ์ฉ
const savedFile = {
    name: 'profile',
    extension: 'jpg',
    size: 29930
}

function fileSummary({name, extension, size}) {		// ์ฌ๊ธฐ์ ์ ์ฉํ๋ค!
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}

fileSummary(savedFile)
```



## ๐ JSON (JavaScript Object Notation)

- key - value ์ ํํ๋ก JS Object ์ ์ ์ฌํ ๋ชจ์ต์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ํํํ๋ ํ๊ธฐ๋ฒ
- ๋ชจ์ต๋ง ๋น์ทํ  ๋ฟ์ด๊ณ  ์ค์ ๋ก๋ ๋ฌธ์์ด ํ์
- Object์ฒ๋ผ ์ฌ์ฉํ๊ธฐ ์ํด์๋ parsing(๊ตฌ๋ฌธ ๋ถ์) ์์์ด ํ์
- JSON ํ์์ ํ์ผ์ ๋ค๋ฃจ๊ธฐ ์ํด JS์์๋ `JSON` ๋ด์ฅ ๊ฐ์ฒด๋ฅผ ์ ๊ณต

**Object โ JSON(string)**

```jsx
const jsonData = JSON.stringify({
	coffee: 'Americano',
	iceCream: 'Cookie and cream',
})

console.log(jsonData)         //  "{"coffee":"Americano","iceCream":"Cookie and cream"}"
console.log(typeof jsonData)  // string
```

**JSON(string) โ Object**

```jsx
const parsedData = JSON.parse(jsonData)

console.log(parsedData)         // {coffee: "Americano", iceCream: "Cookie and cream"}
console.log(typeof parsedData)  // object
```

