# [Django] Model [EP 05]

## 📚 ORM (Object-Relation-Mapping)

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL)데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용함.
- 장점
  - SQL을 잘 알지 못해도 DB 조작 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성 (현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것)
    - DB를 객체로 조작하기 위해 ORM을 사용
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려움



## 🏠 Django Model

### models.py

- 클래스 생성
  - 데이터 베이스의 하나의 스키마 당 하나의 클래스로 만들어 준다.
  - models.Model을 상속받는다. (모듈은 이미 import 되어있다.)
  - PK(Primary Key)는 알아서 생성해준다.
- 모델 필드는 [공식 홈페이지](https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types)를 참고하여 작성한다.

- models.py에 class 만들기

  ```python
  class 모델명(models.Model):
      # 모델의 필드 작성 아래 예시
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)	# 최초 생성 일자
      updated_at = models.DateTimeField(auto_now=True)		# 최종 수정 일자
      
      audience = models.IntegerField()
      release_date = models.DateTimeField()
      score = models.FloatField()
      poster_url = models.URLField()
      
      def __str__(self):
          return self.title
  ```

- 모델의 새로운 설계도를 만든다.

  ```bash
  $ python manage.py makemigrations
  ```

- 설계도를 실제 DB에 반영.

  ```bash
  $ python manage.py migrate
  ```

- sql 구문을 보기 위함

  ```bash
  $ python manage.py sqlmigrate <app 명> 0001
  ```

- migrations 설계도들이 migrate 됐는지 확인

  ```bash
  $ python manage.py showmigrations
  ```

> 테이블을 눈으로 보고 싶은 경우
>
> 실행창을 켜서 SQLite: OPEN Database를 클릭한다.
>
> 프로젝트 폴더에 있는 db.sqlite3를 연결시켜준다.
>
> 수정 후 항상 새로고침!!

- **테이블을 제거하고 싶을 땐 models.py에서 다 주석처리하고 다시 위 과정을 반복한다.**
  - 이 때 관련된 views.py에서도 주석처리해야 에러가 나지 않는다.




### seed 추가

- 테스트 데이터 자동 생성
- 장고 시드 설치

```bash
$ pip install django-seed
```

- settings.py - INSTALLED_APPS에 모듈 추가

```python
INSTALLED_APPS = (
    ... 
    'django_seed', 
)
```

- 명령어 실행

```bash
$ python manage.py seed articles --number 20
```



### fixture

- 데이터베이스의 serialized 된 내용을 포함하는 파일 모음
- django가 fixtures 파일을 찾는 경로
  - app/ficxtures/

- 각 모델 별 dumpdata 실행

  - 데이터베이스에 있는 데이터를 .json 파일로 저장

  ```bash
  $ python manage.py dumpdata --indent 4 aritcles.article > articles.json
  $ python manage.py dumpdata --indent 4 accounts.user > users.json
  ```

- fixture의 내용을 검색하여 데이터베이스로 로드

  - 단, loaddata 전에 데이터베이스 삭제

  ```bash
  $ python manage.py loaddata user.json
  $ python manage.py loaddata movies.json
  
  $ python manage.py loaddata articles/articles.json articles/comments.json accounts/users.json
  ```




## 🏓 Model Relation

### 일대다 관계(1:N)

- A many-to-one relationship

- ForeignKey

- 2개의 필수 위치 인자가 필요

  - 참조하는 model class

  - on_delete 옵션

    - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 지를 정의

    - Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정

    - on_delete 옵션에 사용 가능한 값들

      - `CASCADE` : **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**
      - `PROTECT` : 참조가 되어 있는 경우 오류 발생
      - `SET_NULL` : 부모객체가 삭제 됐을 때 모든 값을 NULL로 치환 (NOT NULL 조건시 불가능)
      - `SET_DEFAULT` : 모든 값이 DEFAULT 값으로 치환
        - DEFAULT 설정 있어야 하며 DB에서는 보통 default가 없으면 null로 잡기도 함. 장고는 아님.

      - `SET()` : 특정 함수 호출
      - `DO_NOTHING` : 아무것도 하지 않음.

      - 다만, 데이터베이스 필드에 대한 SQL `ON DELETE` 제한 조건을 설정해야 함
      - `RESTRICT`

       (new in 3.1)

      - RestrictedError를 발생시켜 참조 된 객체의 삭제를 방지

- 게시글(1) - 댓글(N) 예시 코드

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- 장고는 외래키를 만들면 _id를 붙여서 만들어준다.

#### 참조

참조는 쉽다. 역참조가 중요!

```python
comment = Comment.objects.get(pk=1)
comment.article.content
```

#### 역참조

- 자신을 참조하는 누군가를 참조할 때

- `article.comment_set`

>```python
>article = model.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
>```
>
>위처럼 사용하여 comment_set에서 comments로 변경 가능
>
>이렇게 하면 comment_set을 못쓴다.
>
>`article.comments.all()`로 사용한다.
>
>`1:N`에서는 바꾸는 것을 권장하지 않는다.
>
>`M:N`에서는 무조건 써야하는 상황이 온다. 그 때만 사용하자!!

- 예시

```python
article.comment_set.all()
comments = article.comment_set.all()
```

---

### 다대다 관계(M:N)

- 1:N의 한계
  - 새로운 예약을 생성하는 것이 불가능
  - 외래 키에 1, 2 형식의 여러 데이터를 사용할 수 없음
- ManyToManyField
  - 다대다 관계 설정 시 사용하는 모델 필드
  - related_name : ForeignKey의 related_name과 동일
  - symmetrical
    - 'self'를 가리키는 정의에서만 사용
    - symmetrical=True(기본값)일 경우 person_set 매니저를 추가하지 않음
    - 대칭을 원하지 않는 경우 False로 설정

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor, related_name='patients')

# symmetrical 예제
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- 중개 모델 활용
  - 관계 연결하면서 관계에 따른 속성을 더 추가하고 싶을 때
  - through
    - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있음


```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor, through='Reservation')

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

- 중개 모델 중 반드시 역참조를 써야하는 상황
  - 1:N 관계에서 이미 해당 메니저 이름을 사용 중인 경우
  - ManyToMany에서는 복수형의 표현으로 반드시 related_name을 선언하자!

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



## 📌 Django User Model

- Custom User 모델 정의하기

  - AbstractUser를 상속받아 새로운 User 모델 작성
  - 프로젝트 중간에 변경하면 훨씬 더 어려운 작업이 필요하므로 초기에 설정하는 것을 권장

  ```python
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

  

- 기존 Django가 사용하는 User 모델이었던 auth 앱의 User 모델을 accounts 앱의 User 모델을 사용하도록 변경

  - settings.py에 아래와 같이 추가

    ```python
    AUTH_USER_MODEL = 'accounts.User'
    ```



## 📗 Django Shell

- DB를 터미널에서 조작하기 위함

  ```bash
  $ pip install ipython
  $ pip install django-extensions
  ```

- INSTALLED_APPS에 `'django_extensions',` 추가

  ```bash
  $ python manage.py shell_plus
  ```

- 실행 취소하고 싶으면 exit()

- 쉘에서 원하는 이름으로 확인하기 위한 방법(model에 선언)

  ```python
  # pk - 제목으로
  def __str__(self):
      return f'{self.pk} - {self.title}'
  
  # 제목으로
  def __str__(self):
          return self.title
  ```



## 📒 Django Admin

- 관리자 계정 생성

```bash
$ python manage.py createsuperuser
```

- admin.py에서 설정하여 admin 페이지에 Model이 보이게 해준다.

```python
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)

# list_display #
# class ArticleAdmin(admin.ModelAdmin):
#	list_display = ('pk', 'title',)
# admin.site.register(Article, ArticleAdmin)
```

- Custom User 모델 등록

```python
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



