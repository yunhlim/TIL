# [HTML/CSS] CSS

## HTML과 CSS의 차이

> HTML(Hyper Text Markup Language) : 웹페이지를 작성 구조화한 언어
>
> CSS(Cascading Style Sheets) : 스타일을 지정하기 위한 언어

박스모델은 CSS의 가장 핵심개념

## CSS 선택자

선택자(Selector)란, 스타일을 지정할 HTML 요소를 선택한다.

## CSS 작성 방법

> 1. 특정 태그에 직접 style 속성을 작성, 개별적으로 사용할 때
> 2. head 태그 안에 style 태그 작성, 공통적으로 사용할 때
> 3. 외부 참조로 사용, 외부 파일을 head 내 link로 불러오기(2번과 같다)

내부참조와 외부참조를 같이 쓸 수 있으니 필요에 맞게 선택적으로 사용하면 된다.

세가지 중 외부참조를 가장 많이 쓴다.

inline은 나중에 디버깅을 하기 어렵지만 외부참조는 효율적으로 관리할 수 있다.