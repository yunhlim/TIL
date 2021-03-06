# [JavaScript] ν¨μ(Function) [EP 05]

## π ν¨μλ?

μ°Έμ‘° νμμ΄λ€. (μ£Όμλ₯Ό μ μ₯νλ κ²!)

μλ£νμ functionμ΄λ€.

> μΌκΈ κ°μ²΄(νμ΄μ¬, μλ°μ€ν¬λ¦½νΈμ μ‘΄μ¬)
>
> λ³μμ ν λΉ κ°λ₯
>
> ν¨μμ λ§€κ°λ³μλ‘ μ λ¬ κ°λ₯
>
> ν¨μμ λ°ν κ°μΌλ‘ μ¬μ© κ°λ₯

---

## π ν¨μ μ μΈμ

κ°μ₯ μΌλ°μ μΈ ννμ΄λ€.

3κ°μ§ λΆλΆμΌλ‘ κ΅¬μ±

- ν¨μλͺ
- λ§€κ°λ³μ
- λͺΈν΅ (λ΄μ©)

```javascript
function add(num1, num2) {
    return num1 + num2
}
add(1, 2)	// 3

// μλ ₯λ°μ λΉλ°λ²νΈκ° 8μ μ΄μμΈ κ²½μ°λ§ true
function isValid (password) {
	if (password.length < 8) {
		return false
	} else {
		return true
	}
}
console.log(isValid('abcd'))	// false
```



## π ν¨μ ννμ

ν¨μλ₯Ό ννμ λ΄μμ μ μ

ν¨μμ μ΄λ¦μ μλ΅νκ³  μ΅λͺ ν¨μλ‘ μ μν  μ μλ€.

λ°λΌμ λ§€κ°λ³μμ λͺΈν΅μ νμνκ³  ν¨μλͺμ λ£λμ§ μλ΅νλμ§ ν  μ μλ€.

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



## π₯ ν¨μ μ μΈμκ³Ό ννμ λΉκ΅

### κ³΅ν΅μ 

- function νμ

### μ°¨μ΄μ 

- ν¨μ μ μΈμμ μ΅λͺ ν¨μ λΆκ°λ₯, νΈμ΄μ€ν κ°λ₯
- ν¨μ ννμμ μ΅λͺ ν¨μ κ°λ₯, νΈμ΄μ€ν X (Airbnb μ€νμΌ κ°μ΄λ κΆμ₯ λ°©μ)

ν¨μ ννμμ var ν€μλλ‘ μμ±νλ©΄ μλ¬ λ°μ!



## π ν¨μμ μ¬λ¬ κΈ°λ₯

### κΈ°λ³ΈμΈμ

μΈμ μμ±ν  λ `=`λ€μ κΈ°λ³ΈμΈμλ₯Ό μ μΈνλ€. (νμ΄μ¬κ³Ό κ°λ€.)

```javascript
const greeting = function (name = 'yunh') {
    console.log(`hi ${name}`)
}
greeting()			// hi yunh

// μ£Όλ¬Έμ μμ±
makeOrder = function (menu, size = 'regular') {
	const order = {
		menu,
		size,
	}
	return order
}
console.log(makeOrder('mocha'))		// {menu: 'mocha', size: 'regular'}
```



### λ§€κ°λ³μμ μΈμμ κ°μ λΆμΌμΉ νμ©

λ§€κ°λ³μλ³΄λ€ μΈμμ κ°μκ° λ§μ κ²½μ°μλ μ΄κ³Όν μΈμλ₯Ό λ²λ¦°λ€.

λ§€κ°λ³μλ³΄λ€ μΈμμ κ°μκ° μ μ κ²½μ°μλ undefinedλ‘ λ£μ΄μ μ¬μ©νλ€.

```javascript
const noArgs = function () {
    return 0
}

noArgs(1, 2, 3) // 0

const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

console.log(threeArgs()) // [undefined, undefined, undefined]    λ§€κ°λ³μλ³΄λ€ μΈμμ κ°μκ° μ μ κ²½μ°
console.log(threeArgs(1)) // [1, undefined, undefined]
console.log(threeArgs(1, 2)) // [1, 2, undefined]
console.log(threeArgs(1, 2, 3, 4)) // [1, 2, 3]		λ§€κ°λ³μλ³΄λ€ μΈμμ κ°μκ° λ§μ κ²½μ°
```



### REST Parameter

νμ΄μ¬μ *argsμ μ μ¬νλ€.

ν¨μμ μ μΈλ¬Έμ νλΌλ―Έν°μμ μ°λ κ², κ°λ³μΈμλ₯Ό νλμ λ°°μ΄λ‘ λ°λλ€.

μΈμκ° μλ κ²½μ°λ λΉ λ°°μ΄

```javascript
const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs];
};
restOpr(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]] 
restOpr(1, 2) // [1, 2, []]
```



### Spread operator

...μ΄ νμ΄μ¬μμμ `*` μΈν©μ°μ°μ μ­ν μ νλ€.

ν¨μ νΈμΆλ¬Έμμ μ΄λ€. λ°°μ΄μ΄ ν΄λΉ λ§€κ°λ³μλ‘ κ°κ° λ§€νλλ€.

μ¦, μΈμλ‘ λ£μ λ κ΄νΈλ₯Ό μ κ±° ν κ°μ λ£μ΄μ€ μ μλ€.

```javascript
const spreadOpr = function (arg1, arg2, arg3, arg4) {
	return arg1 + arg2 + arg3 + arg4
}

const numbers = [1, 2, 3]

spreadOpr(...numbers, 4)			// 10
```



## Arrow Function(νμ΄ν ν¨μ)

ν¨μλ₯Ό λΉκ΅μ  κ°λ¨νκ² μ μν  μ μλ€.

1. function ν€μλλ₯Ό μ­μ νλ€.
2. `( λ§€κ°λ³μ ) => { λͺΈν΅ }` μΌλ‘ λνλΈλ€.
3. λ§€κ°λ³μκ° νλμ΄λ©΄ `()`λ₯Ό μ κ±°νκ³  μμ±ν΄λ λλ€.
4. λͺΈν΅μ΄ ν μ€μ΄λΌλ©΄ `{}`λ₯Ό μ κ±°ν ν returnμ μ­μ ν΄μ μ μΌλ©΄ λλ€.

```javascript
// function ν€μλ μ­μ , λ§€κ°λ³μ () μ­μ 
const celsiusToFaherenheit = celsius => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}
console.log(celsiusToFaherenheit(30))		// 86

// function ν€μλ μ­μ , λ§€κ°λ³μ () μ­μ , λͺΈν΅ {}κ³Ό return μ­μ 
const arrow = name => `hello, ${name}`
console.log(arrow('yunh'))					// hello, yunh
```

λμ€μ κ°μ²΄λ₯Ό λ€λ£¨λ©΄μ Arrow Functionμ μ°μμμ λν΄ λ λ°°μ΄λ€!