# [React] 리액트 시작하기 [EP 02]

## 🛠 세팅

[리액트 공식문서 참조](https://create-react-app.dev/docs/getting-started)

```bash
npx create-react-app my-app
cd my-app
npm start
```

초기 파일들을 정리한다.

App.test.js, logo.svg, reportWebvitals.js, setupTests.js, App.css 삭제 App.js, index.css, index.js만 남겨둔다.

### index.js

- reportWebvitals 관련 내용을 지운다.

- React.StrictMode도 삭제

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

```

>### React DOM Client
>
>`react-dom/client`에 새로운 API가 추가되었다.
>
>#### `createRoot`
>
>렌더링 또는 언마운트할 루트를 만드는 새로운 메소드다. `ReactDOM.render`대신 사용하며, 리액트 18의 새로운 기능은 이것 없이 동작 하지 않는다.
>
>**before**
>
>```jsx
>import ReactDOM from 'react-dom'
>import App from 'App'
>
>const container = document.getElementById('root')
>
>ReactDOM.render(<App name="yceffort blog" />, container)
>
>ReactDOM.render(<App name="yceffort post" />, container)
>```
>
>**after**
>
>```jsx
>import ReactDOM from 'react-dom'
>import App from 'App'
>
>const container = document.getElementById('root')
>
>// 루트 생성
>const root = ReactDOM.createRoot(container)
>
>// 최초 렌더링
>root.render(<App name="yceffort blog" />) // During an update, there is no need to pass the container again
>// 업데이트 시에는, container를 다시 넘길 필요가 없다.
>root.render(<App name="yceffort post" />)
>```

### index.css

- 다 지운다.

### App.js

- 상단의 두 import 문구를 삭제한다.
- function app의 return 안의 모든 문구를 삭제한다.
- div태그에 hello!만 남긴다.

### package.json

- dependencies에서 설치한 것들을 import로 불러와서 사용할 것이다.



## 🍟 jsx

자바스크립트 안의 HTML의 jsx 코드라고 한다.

jsx의 구문은 브라우저가 바로 인식하지 못한다.

- 개발자 입장에서 코드 작성 편하다.

App.js의 function은 jsx를 반환한다. 이 점만 빼면 평범한 자바스크립트 함수이다.

jsx를 소위 리액트 컴포넌트라고 부른다.



## 🎨 className

리액트에서는 class를 선언하는 방식이 html과 조금 다르다. 자바스크립트에서 class는 키워드이다.

class가 아니라 className으로 적어줘야 한다.

아래 className에 대해 잘 정리된 블로그를 참고하자!

[블로그 참고(className)](https://hianna.tistory.com/469)

클래스를 추가하고 싶을 때 className으로 element에 추가하면 된다.