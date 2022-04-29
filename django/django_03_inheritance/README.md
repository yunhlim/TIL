# [Django] 템플릿 상속(Inheritance) [EP 03]



## 📚 템플릿 상속

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점
  - Bootstrap CDN 같은 모든 템플릿에 공용으로 사용할 때 좋다.

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음

- 상속하기 위한 tag

>extends : {% extends '부모 템플릿의 이름' %}
>
>- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
>- 반드시 템플릿 최상단에 작성
>
>block : {% block content %} {% endblock %}
>
>- 하위 템플릿에서 overridden할 수 있는 블록을 정의
>- 즉, 하위 템플릿이 채울 수 있는 공간
>- 필요한 블록만 가져와서 재정의하면 된다.

---

## 🏠 base.html

- 뼈대 템플릿 경로 등록

  settings.py - TEMPLETES의 'DIRS'에 등록

  ```python
  'DIRS': [BASE_DIR / 'templates',],
  ```

  > BASE_DIR은 현재 장고 프로젝트를 가지고 있는 최상단 폴더
  >
  > 장고를 쓰는 플랫폼은 어떤 운영체제가 될지 모른다. 윈도우, 맥, 리눅스, 우분투 ...
  >
  > 맞춰서 다 경로시스템을 써야하는데 파이썬의 객체지향적인 언어로 사용하면 플랫폼마다 알아서 바꿔서 해준다.

- base.html 생성

  위에서 경로를 지정했으니 프로젝트 최상단에 templates 폴더를 만들고 base.html을 생성한다.

  ```django
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>
  <body>
    {% include '_nav.html' %}
    {% block content %}
    {% endblock content %}
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  위 같이 nav 바 같은 모든 템플릿에서 공용으로 사용하는 것을 상속받아 작성해주고, block을 활용해 하위 템플릿에서 새로 작성할 공간을 만든다.

- 다른 템플릿에서 base.html 상속받기

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <p>안녕하세요 저는 {{ info.name|lower }}입니다.</p>
    <p>제가 가장 좋아하는 음식은 {{ foods }}입니다.</p>
    <p>저는 사실 {{ foods.0 }}를 가장 좋아합니다.</p>
  {% endblock content %}
  ```

  

> 장고 설계 철학
>
> 표현과 로직(view)를 분리
>
> - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
> - 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원 X
>
> 중복을 배제
>
> - 상속을 통해 중복 코드를 없앤다.
> - 상속의 기초가 되는 철학