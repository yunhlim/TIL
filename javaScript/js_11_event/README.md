# [JavaScript] ์ด๋ฒคํธ(Event) [EP 11]



## ๐ ์ด๋ฒคํธ (Event)

- ๋คํธ์ํฌ ํ๋์ด๋ ์ฌ์ฉ์์์ ์ํธ์์ฉ ๊ฐ์ ์ฌ๊ฑด์ ๋ฐ์์ ์๋ฆฌ๊ธฐ ์ํ ๊ฐ์ฒด
- ์ ํธ๋ณด๋ด๊ธฐ์ด๋ค. ๋ง์ฐ์ค ํด๋ฆญ์ด๋ ํค๋ณด๋ ์๋ ฅ๊ฐ์ ์ฌ์ฉ์์ ๋์์ผ๋ก ๋ฐ์ํ๋ค.



## ๐ EventListener

- ์ด๋ฒคํธ ๊ฐ์ฒด๋ค์ `EventTarget` ์ธํฐํ์ด์ค๋ฅผ ๊ตฌํํ๊ธฐ ๋๋ฌธ์ `addEventListener` ๋ฉ์๋๋ฅผ ํธ์ถํ์ฌ ์ด๋ฒคํธ๋ฅผ ๊ด์ฐฐ ๊ฐ๋ฅ

- `EventTarget.addEventListener(type, listener[, options])`

  - type์๋ ๋ฐ์ํ  ์ด๋ฒคํธ ์ ํ
  - listener๋ ์คํํ  ์ฝ๋ฐฑ ํจ์

- ์ฌ์ฉํ  ์ ์๋ ์ด๋ฒคํธ ํ์๋ค : [์ด๋ฒคํธ ์ฐธ์กฐ | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/Events)

  > change์ input์ ์ฐจ์ด!!
  >
  > ๊ณตํต์ ์ ๋ ๋ค ์ฌ์ฉ์์ ์๋ ฅ์ ๋ฐ๋๋ค.
  >
  > change: ์์ ๋ณ๊ฒฝ์ด ๋๋๋ฉด ๋ฐ์(ํฌ์ปค์ค๋ฅผ ์์ ๋)
  >
  > input: ์ฌ์ฉ์๊ฐ ๊ฐ์ ์์ ํ  ๋๋ง๋ค ๋ฐ์

- ์ด๋ฒคํธ์ ๋ฐ์์ ๋ฐ์ผ๋ฉด ์ฝ๋ฐฑ ํจ์๋ฅผ ์คํ!

  

### ์ฝ๋ฐฑ ํจ์

- ์ฝ๋ฐฑ ํจ์๋ `addEventListener` ๋ฉ์๋์ ํจ์๋ช๋ง ๊ธฐ์ํ๋ค!!
- ์ฝ๋ฐฑ ํจ์๋ event ๊ฐ์ฒด๋ฅผ ์ธ์๋ก ๋ฐ์์ ์ฌ์ฉํ๋ค. (event ๋ช์ e๋ก ์ฐ๊ธฐ๋ ํ๋ค.)
- EventListener ์์ ํจ์๋ฅผ ๋ง๋ค์ด ์ค ์๋ ์๋ค.

```javascript
const onColorInput = function (event) {					// ์ด๋ฒคํธ๋ฅผ ๋ฐ๊ณ  ์คํํ  ์ฝ๋ฐฑ ํจ์
    const userInput = event.target.value
    h2Tag.style.color = userInput
}

colorInput.addEventListener('input', onColorInput)		// eventlistner์ ์ธ์: ์ด๋ฒคํธ ํ์๊ณผ, ์ฝ๋ฐฑํจ์

// ๋ฉ์๋ ์ธ์์ ํจ์ ์์ฑ
checkBox.addEventListener('click', function (event) {
    console.log(event)	// event ๊ฐ์ฒด๋ฅผ ํ์ธํ๋ค.
})
```



### ๊ธฐ๋ณธ ๋์ ์ค๋จ

HTML ์์์ ๊ธฐ๋ณธ ๋์์ ์๋ํ์ง ์๊ฒ ๋ง๋๋ค.

- ex). a ํ๊ทธ์ ๋งํฌ ์ด๋ / form ํ๊ทธ์ ๋ฐ์ดํฐ ์ ์ก

์ฝ๋ฐฑ ํจ์ ๋ด์ `event.preventDefault()` ๋ฉ์๋๋ฅผ ์คํํ๋ค.

> scroll์ฒ๋ผ ๋ง์ ์ ์๋ ์ด๋ฒคํธ๋ค๋ ์กด์ฌํ๋ค.
>
> `event.cancelable`๋ก ํ์ธํ๋ค.

```javascript
const checkBox = document.querySelector('#my-checkbox')

checkBox.addEventListener('click', function (event) {
    event.preventDefault()		// checkBox์ ์ฒดํฌํ๋ ์ด๋ฒคํธ๋ฅผ ๋ง๋๋ค.
    console.log(event)
})
```



### ์ด๋ฒคํธ ๊ฐ์ฒด ์ฌ์ฉ

- ์ด๋ฒคํธ ๊ฐ์ฒด๋ฅผ ํตํด ์ด๋ฒคํธ๋ฅผ ๋ฐ์ํ ํ๊ฒ์ ๊ฐ์ ธ์ ์ํ๋ฅผ ํ์ธํ๊ณ  ์ฌ์ฉํ  ์ ์๋ค. (CRUD)

- `event.target.classList` : ํ๊ฒ ์์์ ํด๋์ค๋ฅผ CRUD

```javascript
event.target.classList.length	// ํด๋์ค ๋ฆฌ์คํธ์ ๊ธธ์ด๋ก ์๋์ง ํ์ธํ  ์ ์๋ค.

event.target.classList.add('done') // ํ๊ฒ ์์์ ํด๋์ค๋ฅผ ์ถ๊ฐํ๋ค.

event.target.classList.remove('done') // ํ๊ฒ ์์์ ํน์  ํด๋์ค๋ฅผ ์ง์ด๋ค.

event.target.classList.contains('done') // ํ๊ฒ ์์์ ํด๋์ค์ ํน์  ๊ฐ์ด ์๋์ง ํ์ธ

event.target.classList.toggle('done')	// ํ๊ฒ ์์์ ํด๋์ค๊ฐ ์์ผ๋ฉด ์์ฑ, ์์ผ๋ฉด ์ ๊ฑฐํ๋ค.
```

- `event.target.style` : ํ๊ฒ ์์์ ์คํ์ผ์ CRUD
- `event.target.tagName` : ํ๊ทธ ์ด๋ฆ(์ด๋ฆฐ ํ๊ทธ ๋ซํ ํ๊ทธ ์ฌ์ด์ ์ ์ Text) ๊ฐ์ ธ์ค๊ธฐ

```javascript
event.target.style.backgroundColor = 'yellow'	// ์คํ์ผ ๋ณ๊ฒฝ
alert("target =" + event.target.tagName + ", this=" + this.tagName)		// ํ๊ทธ๋ช ๊ฐ์ ธ์ค๊ธฐ
```

- `event.target.reset()` : Form ํ์์ reset ํจ๊ณผ

---

## ๋ฒ๋ธ๋ง(bubbling)

๋ถ๋ชจ ์์์ event๋ฅผ ๋ง๋ค๋ฉด ๊ฑฐํ์ด ์๊ธฐ๋ ๊ฒ์ฒ๋ผ ์ด๋ฒคํธ๊ฐ ์ ๋ฌ๋๋ค.

์์ ์์๋ฅผ ๋๋ฌ๋ event๊ฐ ๋ฐ์๋๋ค. ์์ ์์์๋ ๋ค๋ฅธ ํธ๋ค๋ฌ๊ฐ ์์ด๋, ์ฒด์ธ์ฒ๋ผ ๋ถ๋ชจ ์์ ํธ๋ค๋ฌ๊น์ง ๋ค ๋์ํ๋ค!!

[๋ฒ๋ธ๋ง์ ๋ํ ์ค๋ช!](https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/)

focus๋ ๋ฒ๋ธ๋งํ์ง ์๋๋ค.(๋ผ๋ฒจ ํด๋ฆญํ๋ฉด ์ปค์)

```html
<form onclick="alert('form')">Form
    <div onclick="alert('div')">Div
        <p onclick="alert('p')">P</p>
    </div>
</form>
```

์ ์ฝ๋๋ฅผ ๊ทธ๋ฆผ์ผ๋ก ํํํ๋ฉด ๋ค์๊ณผ ๊ฐ๋ค.

![image-20220428233728839](README.assets/image-20220428233728839.png)

๋นจ๊ฐ ๋ถ๋ถ์ ํด๋ฆญํ๋ฉด form์ ์ด๋ฒคํธ๋ง ๋์ํ๊ณ , p๋ฅผ ํด๋ฆญํ๋ฉด ์ธ ๊ฐ์ง๊ฐ ๊ฒน์ณ์์ผ๋ ์ ๋ค ๋์ํ๊ฒ ๋๋ค.

์ด๋ฌํ ์์์ ์ฃผ์ํ๋ฉฐ ์ด๋ฒคํธ๋ฅผ ๋ง๋ ๋ค.
