# [Vue] Vue Intro [EP 01]

## 📚 Vue.js

대표적인 프론트엔드 프레임워크

사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크

> view와 발음이 같다.

현대적인 tool과 다양한 라이브러리를 통해 SPA(Single Page Application)를 완벽 지원

### SPA

- Single Page Apllication (단일 페이지 애플리케이션)
- 단일 페이지로 서버로부터 최초에만 페이지 다운로드, 이후은 동적으로 DOM 구성
- 장고의 templates는 html 여러 개, Vue는 html 한 개
- 화면의 끊김 없이 사용자 경험(UX)을 향상시켜준다.
- 동작 원리의 일부가 CSR의 구조를 따름

### CSR

- Client Side Rendering (클라이언트 사이드 렌더링)
- 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트 화면을 구성
- SPA가 사용하는 렌더링 방식

- 장점
  1. 서버와 클라이언트 간 트래픽 감소
     - 하나의 페이지, 자바스크립트 양을 늘린다.
  2. 사용자 경험(UX) 향상


- 단점
  1. SSR에 비해 초기 구동 속도가 느림 - 자바스크립트 양이 많아 느리다.
  2. SEO(검색 엔진 최적화)에 어렵다. - 최초 문서에 데이터 마크업이 없다.




> **SSR**
>
> Server Side Rendering (서버 사이드 렌더링)
>
> 서버에서 완성된 HTML을 브라우저에서는 보기만 하면 된다.
>
> 장점
>
> 1. 초기 구동 속도가 빠름
>    - 클라이언트가 빠르게 컨텐츠를 볼 수 있음
> 2. SEO(검색 엔진 최적화)에 적합
>    - DOM에 이미 모든 데이터가 작성되어있기 때문
>
> 단점
>
> - 모든 요청마다 새로운 페이지를 구성하여 전달
>   - 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐
>   - 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음
>

### SSR & CSR

- 서버가 만들면 SSR / 클라이언트가 만들면 CSR

- 비용적인 측면에서는 CSR이 좋다.

  - 우리 서버에서 일을 더해야 하면 개발자가 돈을 더 써야 한다.

  - 브라우저(클라이언트)가 일을 하도록하면 비용적으로 좋다.

- SSR와 CSR 중 서비스 프로젝트 구성에 맞는 선택!

> SEO를 대응
>
> Vue.js 또는 React 등 SPA 프레임워크는 SEO 대응기술이 존재
>
> 또한 별도의 프레임워크를 추가로 사용한다.
>
> - Nuxt.js - Vue
> - Next.js - React



### MVVM Pattern

- 구성요소

  1. Model

     - JavaScript Object

     - 모델은 오브젝트다 끝

  2. View
     - Vue에서 View는 DOM(HTML) 이다.

  3. **View Model**

- ViewModel

  Vue에서 ViewModel은 모든 Vue Instance

  View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리

