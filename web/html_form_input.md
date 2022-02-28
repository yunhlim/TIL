# [HTML/CSS] HTML form, input

## 📌 form

`<form>` 정보(데이터)를 서버에 제출하기 위한 영역

action, method input이 어떻게 동작하는지만 알자

기본 속성

>action: form을 처리할 서버의 URL
>
>method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
>
>enctype: method가 post인 경우 데이터의 유형
>
>- application/x-www-form-urlencoded: 기본값
>- multipart/form-data: 파일 전송시(input type이 file인 경우)
>- text/plain: HTML5 디버깅 용(잘 사용되지 않음)

## 📌 input

다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

### 대표적인 속성

>name: form control에 적용되는 이름(이름/값 페어로 전송됨)
>
>value: form control에 적용되는 값(이름/값 페어로 전송됨)
>
>required, readonly, autofocus, autocomplete, disabled 등

### input label

label을 클릭하여 input자체에 초점을 맞추거나 활성화 시킬 수 있음, 사용자가 선택할 수 있는 영역이 늘어난다.

input의 id 속성을 label에서 for 속성으로 상호 연관을 시킨다.

### input 유형

>text: 일반 텍스트 입력
>
>password: 입력 시 값이 보이지 않고 문자를 *로 표시
>
>email: 이메일 형식이 아닌 경우 제출 불가
>
>number: min,max,step 속성을 활용해 숫자 범위 설정 가능
>
>file: accept 속성을 활용하여 파일 타입 지정 가능
>
>checkbox: 다중 선택
>
>radio: 단일 선택
>
>color: color picker
>
>date: date picker
>
>hidden: 사용자에게 보이지 않는 input
>
>submit: submit으로 하면 action경로로 요청이 한꺼번에 넘어간다.

---

라디오버튼이나 체크박스는 **name**이 동일하게 부여가 되어 있어야 한다. 그리고 서버로 보낼 땐 **value**를 지정해주어야 한다.

**autofocus**를 설정하면 자동으로 커서가 올라가는 구역을 설정한다.

**placeholder**로 아이디같은 텍스트를 입력할 때 안내문 형식으로 작게 표시되게 설정할 수 있다.