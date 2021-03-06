# [JavaScript] λ°°μ΄ (Arrays) [EP 07]



## π λ°°μ΄μ μ μμ νΉμ§

λ°°μ΄μ μ°Έμ‘° νμμ κ°μ²΄(Objects)

νμ΄μ¬κ³Ό κ°μ΄ λκ΄νΈλ₯Ό μ΄μ©νμ¬ μμ±νκ³ ,  μμλ₯Ό λ³΄μ₯νλ€.

νμ΄μ¬κ³Ό λ€λ₯Έ μ μ 0μ ν¬ν¨ν μμ μ μ μΈλ±μ€λ‘λ§ μ κ·Ό κ°λ₯νκ³ , -1 κ°μ μΈλ±μ€λ‘λ μ κ·Όμ΄ λΆκ°λ₯νλ€!

λ°°μ΄μ κΈΈμ΄λ `array.length`λ‘ μ κ·Όμ΄ κ°λ₯νλ€.



### Spread operator

spread operator(...)

λ°°μ΄ λ΄λΆμμ λ°°μ΄μ μ κ° κ°λ₯νλ€.

μμ λ³΅μ¬μ νμ©

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]
console.log(newArray)		// [0, 1, 2, 3, 4]
```

---

---

## π λ°°μ΄μ λ©μλ

### reverse

`array.reverse()`

μλ³Έ λ°°μ΄μ μμλ€μ μμλ₯Ό λ°λλ‘ μ λ ¬

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()	// [5, 4, 3, 2, 1]
```

---

### push

`array.push()`

λ°°μ΄μ κ°μ₯ λ€μ μμλ₯Ό μΆκ° (νμ΄μ¬μ append)

### pop

`array.pop()`

λ°°μ΄μ κ°μ₯ λ€μ μμλ₯Ό μ κ±°

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.push(100)		// [1, 2, 3, 4, 5, 100]
numbers.pop()			// [1, 2, 3, 4, 5]
```

---

### unshift

`array.unshift()`

λ°°μ΄μ κ°μ₯ μμ μμλ₯Ό μΆκ°

### shift

`array.shift()`

λ°°μ΄μ κ°μ₯ μμ μμλ₯Ό μ κ±°

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.unshift(100)		
console.log(numbers)	// [100, 1, 2, 3, 4, 5]
numbers.shift()

```

---

### includes

`array.includes(value)`

λ°°μ΄μ valueκ° μλμ§ νλ³ ν μ°Έ κ±°μ§ λ°ν

```javascript
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.includes(1))		// true
console.log(numbers.includes(100))		// false
```

---

### indexOf

`array.indexOf(value)`

λ°°μ΄μ νΉμ  κ°μ΄ μ‘΄μ¬νλμ§ νμΈ ν κ°μ₯ μ²« λ²μ§Έλ‘ μ°Ύμ μμμ μΈλ±μ€λ₯Ό λ°ν

μμΌλ©΄ -1μ λ°ν

```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3)		// 2
result = numbers.indexOf(100)	// -1
```

---

### join

`array.join([separator])`

λ°°μ΄μ λͺ¨λ  μμλ₯Ό μ°κ²°νμ¬ λ°ν

separator(κ΅¬λΆμ)λ₯Ό μ§μ , μλ΅ μ μΌνλ₯Ό κΈ°λ³Έ κ°μΌλ‘ μ¬μ©

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

## π― Array Helper Methods

- λ°°μ΄μ μννλ©° νΉμ  λ‘μ§μ μννλ λ©μλ

- λ©μλ νΈμΆ μ μΈμλ‘ callback ν¨μλ₯Ό λ°λ κ²μ΄ νΉμ§

  > callback ν¨μλ?
  >
  > μ΄λ€ ν¨μμ λ΄λΆμμ μ€νλ  λͺ©μ μΌλ‘ μΈμλ‘ λκ²¨λ°λ ν¨μ
  >
  > μ½λ°± ν¨μλ 3κ°μ§ λ§€κ°λ³μλ‘ κ΅¬μ±
  >
  > element : λ°°μ΄μ μμ
  >
  > index : λ°°μ΄ μμμ μΈλ±μ€
  >
  > array : λ°°μ΄ μμ²΄

### forEach

λ°°μ΄μ κ° μμμ λν΄ μ½λ°± ν¨μλ₯Ό ν λ²μ© μ€ν

breakλ continueλ₯Ό μ¬μ©ν  μ μλ€.

> for ... of λ³΄λ€ forEachλ₯Ό μ°λ κ±Έ Airbnb Style Guideμμ κΆμ₯νλ€!!

**λ°ν κ° μμ**

```javascript
    const colors = ['red', 'green', 'blue']
    const noresult = colors.forEach((color, index, list) => {
      // ν μΌ(μμ) μ½λ°±ν¨μ
      console.log(`${index}λ² μμμ ${color}`)
      console.log(list)
    })
    /*
    0λ² μμμ red
	['red', 'green', 'blue']
	1λ² μμμ green
	['red', 'green', 'blue']
	2λ² μμμ blue
	['red', 'green', 'blue']
    */
```

---

### map

λ°°μ΄μ κ° μμμ λν΄ μ½λ°± ν¨μλ₯Ό ν λ²μ© μ€ν

μ½λ°± ν¨μμ λ°ν κ°μ μμλ‘ νλ μλ‘μ΄ λ°°μ΄μ λ°ν

```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNumbers = numbers.map((number) => {
    return number * 2
})
console.log(doubleNumbers)		// [2, 4, 6, 8, 10]
```

---

### filter

μ½λ°± ν¨μμ λ°ν κ°μ΄ μ°ΈμΈ μμλ€λ§ λͺ¨μμ μλ‘μ΄ λ°°μ΄ λ°ν

```javascript
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num) => {
    return num % 2
})
console.log(oddNums)	// [1, 3, 5]
```

---

### reduce

μ‘°κΈ μ΄λ ΅λ€.

μ½λ°± ν¨μμ λ°ν κ°λ€μ νλμ(acc)μ λμ  ν λ°ν

accλ return κ°μΌλ‘ κ°±μ νλ€. κ·Έλ¦¬κ³  reduceμ μΈμλ‘ accμ μ΄κΈ°κ°μ λ£μ΄μ€λ€.

```javascript
numbers = [1, 2, 3]
const result =  numbers.reduce((acc, element) => {
    console.log(`λ°ν€μ ${acc}, elementλ ${element}`)
    return acc + element
}, 0)
console.log(result)
/*
λ°ν€μ 0, elementλ 1
λ°ν€μ 1, elementλ 2
λ°ν€μ 3, elementλ 3
6
*/
```

---

### find

μ½λ°± ν¨μμ λ°ν κ°μ΄ μ°Έμ΄λ©΄ ν΄λΉ μμλ₯Ό λ°ν

μ°Ύλ κ°μ΄ λ°°μ΄μ μλ€λ©΄ undefinedλ₯Ό λ°ννλ€.

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

λ°°μ΄μ μμ μ€ νλλΌλ νλ³ ν¨μλ₯Ό ν΅κ³Όνλ©΄ μ°Έμ λ°ν

λΉ λ°°μ΄μ ν­μ κ±°μ§μ λ°ννλ€.

μ ν¨μ± κ²μ¬ν  λ μ μ©νλ€.

```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some(num => {
    return num % 2 === 0 // μ§μ
})
console.log(hasEvenNumber) // false
```

---

### every

λ°°μ΄μ λͺ¨λ  μμκ° νλ³ ν¨μλ₯Ό ν΅κ³Όνλ©΄ μ°Έμ λ°ν

λΉ λ°°μ΄μ ν­μ μ°Έμ λ°ννλ€.(ν΅κ³Όνμ§ λͺ»νλ λ°°μ΄μ μ°Ύλ κ²μ΄λ€.)

```javascript
const numbers = [2, 4, 6, 8, 10, 1]

const isEveryNumberEven = numbers.every(num => {
    return num % 2 === 0 // μ§μ
})
console.log(isEveryNumberEven)	// false
```

