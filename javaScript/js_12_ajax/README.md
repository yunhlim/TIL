# [JavaScript] AJAX [EP 12]



## 📚 AJAX 란?

AJAX(Asynchronous JavaScript And XML)은 비동기식 자바스크립트와 XML의 약자이다.

이름과 달리, JSON, XML, HTML 등 다양한 포맷을 주고 받을 수 있다.

특히 이 중 **JSON**을 많이 사용한다!

>JSON을 더 많이 쓰는 이유?
>
>- JSON이 XML보다 용량이 가볍다.
>- JSON은 JavaScript의 일부



### AJAX의 특징

- 페이지 새로 고침 없이 서버에 요청(**비동기성**)
- 서버로부터 데이터를 받고 작업을 수행



### ~~XMLHttpRequest 객체~~

데이터를 받아오기 위한 객체

서버와 상호작용하기 위해 사용한다. 주로 AJAX 프로그래밍에 사용한다.

생성자 : XMLHttpRequest()

XMLHttpRequest 대신에 **promise-style**(Axios)을 많이 사용한다.

XML 사용 예제는 아래 비동기에 있는 코드를 확인한다.

---

## 🕑 비동기

### 동기식(Synchoronus)

하나가 끝나야 다음 것을 한다.

자바스크립트는 싱글 쓰레드 : Call Stack이 하나!

> 스레드(thread)
>
> 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
>
> OS에서 배운다.
>
> 각 스레드는 한 번에 하나의 작업만 수행
>
> 다음 작업을 시작하려면 앞의 작업이 완료되어야 함.

### 비동기식(Asynchoronus)

병렬적으로 수행한다.

요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)

**사용자 경험** : 데이터를 불러오는 동안 지속적으로 응답하는 화면을 보여줌, 많은 웹 API 기능은 비동기 코드를 사용하여 실행

```javascript
const request = new XMLHttpRequest()		// 브라우저 창 열기
const URL = 'http://jsonplaceholder.typicode.com/todos/1'
request.open('GET', URL)	// URL을 주소창에 넣기

reqeust.send()		// enter

const todo = request.response

console.log(todo)
JSON.parse(todo)	// string을 Json으로 파싱!
```

한꺼번에 실행하면 응답이 없다.

request.send()만 비동기식이라 send()의 응답이 끝나길 기다려주지 않고 response를 가져오니 아무것도 존재하지 않는다.

---

## 🏓 동시성 모델

Event loop를 기반으로 하는 동시성 모델(Concurrency model)

1. ### Call Stack

   - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack 자료 구조

2. ### Web API (Browser API)

   - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API

   - Web API는 다중 쓰레드이다.

3. ### Task Queue (Event Queue, Message Queue)

   - 비동기 처리된 callback 함수가 대기하는 Queue 자료 구조

4. ### Event Loop

   - Call Stack이 비어있는지 확인
   - 비어 있는 경우 Task Queue에서 대기 중인 callback 함수를 꺼내 Call Stack에 Push
   - Queue에서 하나씩 꺼낸다.

- **참고**

> [이벤트 루프 유튜브 설명](https://www.youtube.com/watch?v=8aGhZQkoFbQ&t=3s)
>
> [코드 시각화 사이트](http://latentflip.com/loupe/?code=JC5vbignYnV0dG9uJywgJ2NsaWNrJywgZnVuY3Rpb24gb25DbGljaygpIHsKICAgIHNldFRpbWVvdXQoZnVuY3Rpb24gdGltZXIoKSB7CiAgICAgICAgY29uc29sZS5sb2coJ1lvdSBjbGlja2VkIHRoZSBidXR0b24hJyk7ICAgIAogICAgfSwgMjAwMCk7Cn0pOwoKY29uc29sZS5sb2coIkhpISIpOwoKc2V0VGltZW91dChmdW5jdGlvbiB0aW1lb3V0KCkgewogICAgY29uc29sZS5sb2coIkNsaWNrIHRoZSBidXR0b24hIik7Cn0sIDUwMDApOwoKY29uc29sZS5sb2coIldlbGNvbWUgdG8gbG91cGUuIik7!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D)

---

## 📗 Callback 함수

콜백함수는 다른 함수에 인자로 전달된 함수이다.

콜백함수는 자바스크립트 파이썬 장고 등등 여러 군데에서 사용된다!

비동기 작업이 완료된 후 코드 실행을 계속하는 데 사용되는 경우를 비동기 콜백(asynchronous callback)이라고 함.



### Async callbacks

- 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
- 요청이나 특정 루틴, action에 의해 호출되게 하여 event 조건으로 호출할 수 있다.
- 비동기 로직을 수행할 때는 콜백 함수가 필수이다.



### callback Hell

- 콜백함수가 연쇄적으로 호출되야하는 상황
- 코드 가독성이 떨어져 디버깅이 힘들다.
- 해결하기 위해 **Promise 콜백 방식 사용**

---

## 🎲 Promise

- 비동기 작업의 최종 완료 또는 실패를 나타내는 객체, 객체가 Promise 객체

- Chaining : 코드가 깔끔해진다. - 메서드 체인으로 나타내는 방법!!

- 비동기의 엄격한 순서를 보장해준다.

- 반환 값이 반드시 있어야 한다.

### Promise methods

- .then()
  - 이전 작업이 성공했을 때 수행할 작업을 나타내는 callback 함수
  - 이전 작업의 성공 결과를 인자로 전달받는다.
  - 성공했을 때의 코드를 함수 안에 작성

- .catch()
  - 실패에 대한 약속!
  - 하나라도 실패한 경우 동작한다. 여러개의 catch를 만들지 않아도 된다.

- .finally()
  - 결과와 상관없이 무조건 callback 함수 실행
  - 어떤 인자도 전달 받지 않는다.

### Axios

브라우저를 위한 Promise 기반의 클라이언트

[Axios 공식 문서](https://axios-http.com/kr/docs/intro) : 공식문서에서 javascript CDN을 불러와 사용한다.

XMLHttpRequest 대신 사용한다.

훨씬 편리한 AJAX 요청이 가능하도록 도움을 준다.

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    const API_URI = 'https://dog.ceo/api/breeds/image/random'
    const img_path = document.querySelector('img')
    function getDog() {
        // axios를 사용하여 API_URI로 GET 요청을 보낸다.
        axios.get(API_URI)
        // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
        // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.    
            .then(res => img_path.setAttribute('src', res.data.message))
            .catch(error => console.log(error))	// error를 처리한다.
    }
    const button = document.querySelector('button')
    button.addEventListener('click', getDog)
</script>
```

> **async await**
>
> 문법을 편하게 쓰게 해준다.
>
> async await는 promise에서 성능이 달라지는게 아니라 동기 표현처럼 좀 더 다듬는 느낌
>
> promise 구조의 then chaining 제거하고 좀 더 파이썬같은 코드를 나타낸다.
>
> 나타내는 방법
>
> - 함수로 묶어야 한다.
>
> - 해당 함수 앞에 async 키워드로 표시를 남긴다.
>
> - 블록 내부에 비동기로 동작하는 함수들을 찾아서 앞에 await을 남긴다.