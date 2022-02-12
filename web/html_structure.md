# [HTML/CSS] HTML 기본구조

! 누르고 tab누르면 다음과 같이 자동완성된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

doctype은 관습적으로 쓰는것, 무슨 문서인지 알기 위해(여기서는 html)

---

## html

문서의 최상위(root) 요소

## head

문서 메타데이터 요소(정보를 담는다)

- 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
- 일반적으로 브라우저에 나타나지 않는 내용

> metadata(메타데이터) - ex). 카메라를 찍으면 사진이 데이터 => 사진을 설명하는 데이터(GPS, 노출정보, 촬영일자) : 메타데이터, 중요데이터는 body에 있지만 필요한 데이터가 head에 담겨있다.

- head 예시

  >`<title>` : 브라우저 상단 타이틀
  >
  >`<meta>` : 문서 레벨 메타데이터 요소
  >
  >`<link>` : 외부 리소스 연결 요소(CSS 파일, favicon 등)
  >
  >`<script>`: 스크립트 요소(JavaScript 파일/코드)
  >
  >`<style>` : CSS 직접 작성

## body

문서 본문 요소, 여기다가 내용을 작성한다.