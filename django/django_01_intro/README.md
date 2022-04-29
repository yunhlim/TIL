# [Django] Django Intro [EP 01]

## 📌 장고(Django) 란?

- 검증된 Python 언어 기반 Web framework

> 프레임워크 : 프로그래밍에서 특정 운영체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
>
> Web framework 란?
>
> 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적!
>
> 개발에 집중하기 위해 환경을 제공(tool), 개발을 zero부터 시작하지 않기 위해서
>
> 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함.
>
> 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종

### Framework Architecture

- MVC Design Pattern (model-view-controller) - 대부분의 프레임워크가 따르는 디자인 패턴(장고도 이 디자인 패턴을 따른다. 그런데 명칭을 바꿔 부른다)

  사용자 인터페이스로부터 프로그램 로직을 분리 서로 영향 없이 고칠 수 있다.

- 장고는 MTV Pattern이라고 부른다. 특별한 이유는 없다. view를 template, controller를 view로 부른다.

MTV 패턴

- model: 응용프로그램의 데이터 구조를 정의, 데이터베이스의 기록을 관리(추가, 수정, 삭제)

- Temlate(view): 파일의 구조나 레이아웃을 정의, 실제 내용을 보여주는 데 사용, 보여지는 부분 관장

- **View**(controller): 클라이언트 요청(HTTP 요청)을 서버가 수신하고 응답을 반환하는 것, 데이터베이스에 대한 조회(model과의 소통)도 view가 진행, template에게 응답의 서식 설정을 맡김, 하는 일이 가장 많다, 가장 중요!

  > 클라이언트 -> 서버 : 요청
  >
  > 클라이언트 <- 서버 : 응답
  >
  > ex). 클라이언트(웹브라우저 - 크롬), 서버(네이버)



## 💥 Django 시작하기

### 가상환경 세팅

- 독립적인 개발 환경을 만들기 위해 설치한다.

- git bash나 vs code IDE를 실행해 터미널에 명령어를 입력하여 생성(가상환경이름을 venv로 주로 짓는다.)

  ```bash
  $ python -m venv [가상환경이름]
  $ source [가상환경이름]/Scripts/activate
  ```



### Django 설치

- 가상환경을 실행한 후 설치한다.(4버전이 아닌 안정적인 3버전으로 설치한다.)

  ```bash
  $ pip install django==3.2.12
  ```



### Project  생성

- 프로젝트는 하나 생성한다. 이름에는 키워드나 `-`은 피해야한다.

  ```bash
  $ django-admin startproject [프로젝트명] .
  ```



### Project 구조

- asgi.py - 나중에 다른사람들도 사용하게 하기 위한 배포할 때 사용!

- **settings.py** - 중요!  애플리케이션의 모든 설정을 포함

- urls.py - 사이트의 **url**과 적절한 views의 연결을 지정

- wsgi.py - 다른 서버와 연결할 때 배포할 때 도움을 줄 수 있는 파일

- manage.py - 커맨드를 동작시키는 역할, 수정 X



### Application 생성

- 일반적으로 복수형으로 짓는다.
- 하나의 프로젝트에 여러가지 기능을 맡는 App 여러 개를 만들어서 사용한다.

```bash
$ python manage.py startapp [어플명s]
```



### Application 구조

admin.py - 관리자용 페이지를 설정하는 곳

apps.py - 앱의 정보가 작성된 곳, 수정 X

models.py - 앱에서 사용하는 Model을 정의하는 곳

tests.py - 프로젝트의 테스트 코드를 작성하는 곳, 수정 X

views.py - view 함수들이 정의 되는 곳

> template은 장고 명령어로 생성되는 것이 아니다. 
>
> template은 직접 생성해줘야 한다.



### App 등록

프로젝트의 settings.py의 INSTALLED_APPS에 `'어플명',` 을 추가해준다.