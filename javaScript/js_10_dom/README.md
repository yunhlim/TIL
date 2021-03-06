# [JavaScript] DOM ์กฐ์ [EP 10]



## ๐ DOM ์กฐ์์ด๋?

DOM์ผ๋ก ๊ตฌ์กฐํ๋์ด ๊ฐ์ฒดํ๋ HTML ๋ฌธ์๋ฅผ ์กฐ์ํ๋ ๊ฒ์ด๋ค.

์๋ฐ์คํฌ๋ฆฝํธ ์ธ์ด๋ฅผ ํ์ฉํ์ฌ ๋ฌธ์๋ฅผ ์กฐ์ํ๋ค.

์ต์์ ๊ฐ์ฒด๋ window์ด๋ค.(์์ฑ ์ ์๋ต ๊ฐ๋ฅํ๋ค.) => `[window. ์๋ต]console.log()`

### DOM ์์ ๊ตฌ์กฐ

> EventTarget => Node => Element/Document => HTMLElement

- EventTarget : Event Listener๋ฅผ ๊ฐ์ง ์ ์๋ ๊ฐ์ฒด๊ฐ ๊ตฌํํ๋ DOM ์ธํฐํ์ด์ค
- Node : ์ฌ๋ฌ๊ฐ์ง DOM ํ์๋ค์ด ์์ํ๋ ์ธํฐํ์ด์ค
- Element : Document ์์ ๋ชจ๋  ๊ฐ์ฒด๊ฐ ์์ํ๋ ๊ฐ์ฅ ๋ฒ์ฉ์ ์ธ ์ธํฐํ์ด์ค
- Document : DOM ํธ๋ฆฌ์ ์ง์์  ์ญํ ์ ์ํ
- HTMLElement : ๋ชจ๋  ์ข๋ฅ์ HTML ์์

> **Window.alert()**
>
> ์๋์ฐ ์๋ต ๊ฐ๋ฅํ๋ค.
>
> ํ์ธ ๋ฒํผ์ ๊ฐ์ง๋ฉฐ ๋ฉ์์ง๋ฅผ ์ง์ ํ  ์ ์๋ ๊ฒฝ๊ณ  ๋ํ์์๋ฅผ ๋์ด๋ค.
>
> `alert('๋ฉ๋กฑ!!!')`

---

## ๐ DOM ์ ํ

selector๋ ๋ฌธ์์ด ํ์์ผ๋ก ์ ๋๋ค.

- `document.querySelector(selector)`

  queryselector๋ ๋งจ ์์ ๋ง๋๋ ์ ํ์ ํ๋๋ฅผ ๊ฐ์ ธ์จ๋ค.

  CSS selector๊ฐ element ๊ฐ์ฒด๋ฅผ ๋ฐํํ๋ค. ์๋ค๋ฉด null์ ๋ฐํํ๋ค.

- `document.querySelectorAll(selector)`

  ์ ๊ณตํ ์ ํ์์ ์ผ์นํ๋ ์ฌ๋ฌ element๋ฅผ ์ ํํ๋ค.

  ์ง์ ๋ ์ ํ์์ ์ผ์นํ๋ NodeList๋ฅผ ๋ฐํํ๋ค. (NodeList๋ ๋ฐฐ์ด์ด ์๋๋ค. `forEach`๋ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค!!)

```javascript
const h1 = document.querySelector('h1')
const h2 = document.querySelector('h2')
const secondH2 = document.querySelector('#location-header')
const selectUlTag = document.querySelector('div > ul')

const liTags = document.querySelectorAll('li')
const secondLiTags = document.querySelectorAll('.ssafy-location')
```

> ๋ค์ 3๊ฐ์ง๋ ์ ํ์ฉํ์ง ์๋๋ค.
>
> getElementByID(id)
>
> getElementsByTagName(name)
>
> getElementsByClassName(names)
>
> ์๋๋ฉด ์ด์ฐจํผ querySelector()๋ก id, class, tag ๋ฑ ๋ชจ๋ ์ฌ์ฉ๊ฐ๋ฅํ๋ค.
>
> 
>
> HTMLCollection, NodeList๋ ๋ณ๊ฒฝ์ฌํญ์ด ์ค์๊ฐ์ผ๋ก ๋ฐ์๋๋ฏ๋ก ์ฐ์ง ์๊ณ , ๋์  ์ค์๊ฐ์ผ๋ก ๋ฐ์๋์ง ์๋ querySelectorAll()์ ์ด๋ค.

---

## ๐ DOM ์ถ๊ฐ ๋ฐ ๋ณ๊ฒฝ

- `document.createElement()`

  ์์ฑํ ํ๊ทธ ๋ช์ HTML ์์๋ฅผ ์์ฑํ์ฌ ๋ฐํ

- `child.append(parent)`

  ํ์ฌ ๋ธ๋(child)๋ฅผ ํน์  ๋ถ๋ชจ ๋ธ๋(parent)์ ๋ง์ง๋ง ์์ ๋ค์์ผ๋ก ์ฝ์ํ๋ค.

  String๋ ์ถ๊ฐ ๊ฐ๋ฅํ๋ค.

  ๋ฐํ ๊ฐ์ด ์๋ค.

  ์ฌ๋ฌ ๊ฐ๋ฅผ ํ ๋ฒ์ ์ถ๊ฐํ  ์ ์๋ค.

- `child.appendChild(parent)`

  ํ์ฌ ๋ธ๋(child)๋ฅผ ํน์  ๋ถ๋ชจ ๋ธ๋(parent)์ ๋ง์ง๋ง ์์ ๋ค์์ผ๋ก ์ฝ์ํ๋ค.

  String์ ์ถ๊ฐํ  ์ ์๊ณ  ํ๋์ Node๋ง ์ถ๊ฐํ๋ค.

  ์ฌ๋ฌ ๊ฐ๋ฅผ ์ถ๊ฐํ๋ฉด ๊ฐ์ฅ ๋จผ์  ๋ค์ด์ค๋ ์ธ์ ํ๋๋ง ์ถ๊ฐ๋๋ค.

- Node.innerText

  ํ๊ทธ ์ฌ์ด์ ๋ฌธ์์ด์ ๋ด์์ค๋ค.

  ์ ์๋ฐ์คํฌ๋ฆฝํธ์ innerText์ ์์ ๊ฐ ์๋ค.

  > Element.innerHTML์ ์ ์ฐ์ง ์๋๋ค.
  >
  > XSS ๊ณต๊ฒฉ์ ์ทจ์ฝํ๋ฏ๋ก ์ฌ์ฉ์ ์ฃผ์!
  >
  > XSS (Cross-site Scripting) : ์์ฑ ์๋ฐ์คํฌ๋ฆฝํธ ์ฝ๋๋ฅผ ์ฝ์ํด ๋ฏผ๊ฐํ ์ ๋ณด๋ฅผ ํ์ทจ

```javascript
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')  // li ํ๊ทธ๋ฅผ ๋ง๋ ๋ค.
newLiTag.innerText = '์๋ก์ด ๋ฆฌ์คํธ ํ๊ทธ'       // li ํ๊ทธ ์์ ํ์คํธ๋ฅผ ๋ฃ์ด์ค๋ค.
ulTag.append(newLiTag)						// ์์ ๋ธ๋๋ก ์ฝ์ํ๋ค.
ulTag.append('๋ฌธ์์ด๋ ์ถ๊ฐ ๊ฐ๋ฅ')

const new1 = document.createElement('li')
new1.innerText = '๋ฆฌ์คํธ 1'
const new2 = document.createElement('li')
new2.innerText = '๋ฆฌ์คํธ 2'
const new3 = document.createElement('li')
new3.innerText = '๋ฆฌ์คํธ 3'
ulTag.append(new1, new2, new3)			// 3๊ฐ์ง๊ฐ ํ ๋ฒ์ ์ถ๊ฐ๋๋ค.


const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = '์๋ก์ด ๋ฆฌ์คํธ ํ๊ทธ'
ulTag.appendChild(newLiTag)				// ์์ ๋ธ๋๋ก ์ฝ์
ulTag.appendChild('๋ฌธ์์ด์ ์ถ๊ฐ ๋ถ๊ฐ')		// error : ๋ฌธ์์ด์ ์ถ๊ฐํ  ์ ์๋ค.

const new1 = document.createElement('li')
new1.innerText = '๋ฆฌ์คํธ 1'
const new2 = document.createElement('li')
new2.innerText = '๋ฆฌ์คํธ 2'
ulTag.appendChild(new1, new2)			// ์ฌ๋ฌ๊ฐ๋ฅผ ๋ฃ์ผ๋ฉด ๋งจ ์์ ํ๋๋ง ์ถ๊ฐ๋๋ค.
```

---

## ๐ DOM ์ญ์ 

- ChildNode.remove()

  ํด๋น ๋ธ๋๋ฅผ ์ญ์ 

- Node.removeChild(child)

  ํด๋น ๋ธ๋์ ์์ ๋ธ๋(child) ์ญ์ 

  ์ ๊ฑฐ๋ ๋ธ๋๋ฅผ ๋ฐํ

```javascript
// remove
const header = document.querySelector('#location-header')
header.remove()			// header๋ฅผ ์ญ์ 

// removeChild
const parent = document.querySelector('ul')
const child = document.querySelector('ul > li')
const removedChild = parent.removeChild(child)		// ul > li ์ฒซ ๋ฒ์งธ ๋ธ๋ ์ญ์ 
console.log(removedChild)		// ์ญ์ ๋ ๋ธ๋ ์ถ๋ ฅ : <li class="ssafy-location">์์ธ</li>

// ์์ ๋ฐ๊พธ๊ธฐ : ์ญ์ ํ ๊ฑธ ๋ค์ ์ฝ์
parent.append(child)
```



---

## ๐ DOM ์์ฑ

- Element.setAttribute(name, value)

  ์์ ๊ฐ ์ค์ 

  ์์ฑ์ด ์ด๋ฏธ ์กด์ฌํ๋ฉด ๊ฐ์ ๊ฐฑ์ ํ๊ณ , ์์ผ๋ฉด ์๋ก์ด ์ด๋ฆ๊ณผ ์์ฑ ์ถ๊ฐ

- Element.getAttribute(attributeName)

  ์์ ๊ฐ ๋ฐํ

  attributeName์ ๊ฐ์ ์ป๊ณ ์ ํ๋ ์์ฑ์ ์ด๋ฆ

```javascript
// setAttribute
const header = document.querySelector('#location-header')
header.setAttribute('class', 'ssafy-location')	// class='ssafy-location' ์ถ๊ฐ

// getAttribute
const getAttr = document.querySelector('.ssafy-location')
console.log(getAttr.getAttribute('class'))	// ssafy-location : class ๊ฐ ์ถ๋ ฅ
console.log(getAttr.getAttribute('style'))	// null : style ๊ฐ์ ์๋ค.
```



---

## ๐ ์คํ์ผ ๋ณ๊ฒฝ

- Element.style.attribute = 'value'

  style์ ์ง์  ์ ์ฉ์์ผ์ค๋ค.

  style์ css๋ก ์์ฑํ๊ณ , ์ํ๋ ํ๊ทธ์ ์ฐ๊ฒฐํด์ฃผ๋ ๋ฐฉ์(id๋ ํ๊ทธ ์ด๋ฆ)์ด ๋ ๋ง์ด ํ์ฉ๋๋ค. => ์ฌ๋ฌ๊ฐ์ง ์คํ์ผ์ ํ ๋ฒ์ ์ ์ฉ ๊ฐ๋ฅํ๋ค.

```javascript
body.style.backgroundColor = 'gray'
body.style.color = 'white'

li1.style.cursor = 'pointer'
li2.style.color = 'blue'
li3.style.background = 'red'

// css๋ก ์์ฑํด๋์ style์ ์ ์ฉ
const body = document.querySelector('body')
body.setAttribute('id', 'main')
```



