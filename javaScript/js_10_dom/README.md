# [JavaScript] DOM 조작 [EP 10]



## 📌 DOM 조작이란?

DOM으로 구조화되어 객체화된 HTML 문서를 조작하는 것이다.

자바스크립트 언어를 활용하여 문서를 조작한다.

최상위 객체는 window이다.(작성 시 생략 가능하다.) => `[window. 생략]console.log()`

### DOM 상속 구조

> EventTarget => Node => Element/Document => HTMLElement

- EventTarget : Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node : 여러가지 DOM 타입들이 상속하는 인터페이스
- Element : Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
- Document : DOM 트리의 진입점 역할을 수행
- HTMLElement : 모든 종류의 HTML 요소

> **Window.alert()**
>
> 윈도우 생략 가능하다.
>
> 확인 버튼을 가지며 메시지를 지정할 수 있는 경고 대화상자를 띄운다.
>
> `alert('메롱!!!')`

---

## 🔍 DOM 선택

selector는 문자열 타입으로 적는다.

- `document.querySelector(selector)`

  queryselector는 맨 위에 만나는 선택자 하나를 가져온다.

  CSS selector가 element 객체를 반환한다. 없다면 null을 반환한다.

- `document.querySelectorAll(selector)`

  제공한 선택자와 일치하는 여러 element를 선택한다.

  지정된 선택자에 일치하는 NodeList를 반환한다. (NodeList는 배열이 아니다. `forEach`는 사용 가능하다!!)

```javascript
const h1 = document.querySelector('h1')
const h2 = document.querySelector('h2')
const secondH2 = document.querySelector('#location-header')
const selectUlTag = document.querySelector('div > ul')

const liTags = document.querySelectorAll('li')
const secondLiTags = document.querySelectorAll('.ssafy-location')
```

> 다음 3가지는 잘 활용하지 않는다.
>
> getElementByID(id)
>
> getElementsByTagName(name)
>
> getElementsByClassName(names)
>
> 왜냐면 어차피 querySelector()로 id, class, tag 등 모두 사용가능하다.
>
> 
>
> HTMLCollection, NodeList도 변경사항이 실시간으로 반영되므로 쓰지 않고, 대신 실시간으로 반영되지 않는 querySelectorAll()을 쓴다.

---

## 🔍 DOM 추가 및 변경

- `document.createElement()`

  작성한 태그 명의 HTML 요소를 생성하여 반환

- `child.append(parent)`

  현재 노드(child)를 특정 부모 노드(parent)의 마지막 자식 다음으로 삽입한다.

  String도 추가 가능하다.

  반환 값이 없다.

  여러 개를 한 번에 추가할 수 있다.

- `child.appendChild(parent)`

  현재 노드(child)를 특정 부모 노드(parent)의 마지막 자식 다음으로 삽입한다.

  String은 추가할 수 없고 하나의 Node만 추가한다.

  여러 개를 추가하면 가장 먼저 들어오는 인자 하나만 추가된다.

- Node.innerText

  태그 사이에 문자열을 담아준다.

  위 자바스크립트에 innerText의 예제가 있다.

  > Element.innerHTML은 잘 쓰지 않는다.
  >
  > XSS 공격에 취약하므로 사용시 주의!
  >
  > XSS (Cross-site Scripting) : 악성 자바스크립트 코드를 삽입해 민감한 정보를 탈취

```javascript
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')  // li 태그를 만든다.
newLiTag.innerText = '새로운 리스트 태그'       // li 태그 안에 텍스트를 넣어준다.
ulTag.append(newLiTag)						// 자식 노드로 삽입한다.
ulTag.append('문자열도 추가 가능')

const new1 = document.createElement('li')
new1.innerText = '리스트 1'
const new2 = document.createElement('li')
new2.innerText = '리스트 2'
const new3 = document.createElement('li')
new3.innerText = '리스트 3'
ulTag.append(new1, new2, new3)			// 3가지가 한 번에 추가된다.


const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = '새로운 리스트 태그'
ulTag.appendChild(newLiTag)				// 자식 노드로 삽입
ulTag.appendChild('문자열은 추가 불가')		// error : 문자열은 추가할 수 없다.

const new1 = document.createElement('li')
new1.innerText = '리스트 1'
const new2 = document.createElement('li')
new2.innerText = '리스트 2'
ulTag.appendChild(new1, new2)			// 여러개를 넣으면 맨 앞의 하나만 추가된다.
```

---

## 🔍 DOM 삭제

- ChildNode.remove()

  해당 노드를 삭제

- Node.removeChild(child)

  해당 노드의 자식 노드(child) 삭제

  제거된 노드를 반환

```javascript
// remove
const header = document.querySelector('#location-header')
header.remove()			// header를 삭제

// removeChild
const parent = document.querySelector('ul')
const child = document.querySelector('ul > li')
const removedChild = parent.removeChild(child)		// ul > li 첫 번째 노드 삭제
console.log(removedChild)		// 삭제된 노드 출력 : <li class="ssafy-location">서울</li>

// 순서 바꾸기 : 삭제한 걸 뒤에 삽입
parent.append(child)
```



---

## 🔍 DOM 속성

- Element.setAttribute(name, value)

  요소 값 설정

  속성이 이미 존재하면 값을 갱신하고, 없으면 새로운 이름과 속성 추가

- Element.getAttribute(attributeName)

  요소 값 반환

  attributeName은 값을 얻고자 하는 속성의 이름

```javascript
// setAttribute
const header = document.querySelector('#location-header')
header.setAttribute('class', 'ssafy-location')	// class='ssafy-location' 추가

// getAttribute
const getAttr = document.querySelector('.ssafy-location')
console.log(getAttr.getAttribute('class'))	// ssafy-location : class 값 출력
console.log(getAttr.getAttribute('style'))	// null : style 값은 없다.
```



---

## 🔍 스타일 변경

- Element.style.attribute = 'value'

  style을 직접 적용시켜준다.

  style을 css로 작성하고, 원하는 태그에 연결해주는 방식(id나 태그 이름)이 더 많이 활용된다. => 여러가지 스타일을 한 번에 적용 가능하다.

```javascript
body.style.backgroundColor = 'gray'
body.style.color = 'white'

li1.style.cursor = 'pointer'
li2.style.color = 'blue'
li3.style.background = 'red'

// css로 작성해놓은 style을 적용
const body = document.querySelector('body')
body.setAttribute('id', 'main')
```



