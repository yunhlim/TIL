# [Django] Model [EP 05]

## π ORM (Object-Relation-Mapping)

- κ°μ²΄ μ§ν₯ νλ‘κ·Έλλ° μΈμ΄λ₯Ό μ¬μ©νμ¬ νΈνλμ§ μλ μ νμ μμ€ν κ°μ(Django - SQL)λ°μ΄ν°λ₯Ό λ³ννλ νλ‘κ·Έλλ° κΈ°μ 
- OOP νλ‘κ·Έλλ°μμ RDBMSλ₯Ό μ°λν  λ, λ°μ΄ν°λ² μ΄μ€μ κ°μ²΄ μ§ν₯ νλ‘κ·Έλλ° μΈμ΄ κ°μ νΈνλμ§ μλ λ°μ΄ν°λ₯Ό λ³ννλ νλ‘κ·Έλλ° κΈ°λ²
- Djangoλ λ΄μ₯ Django ORMμ μ¬μ©ν¨.
- μ₯μ 
  - SQLμ μ μμ§ λͺ»ν΄λ DB μ‘°μ κ°λ₯
  - SQLμ μ μ°¨μ  μ κ·Όμ΄ μλ κ°μ²΄ μ§ν₯μ  μ κ·ΌμΌλ‘ μΈν λμ μμ°μ± (νλ μΉ νλ μμν¬μ μμ μ μΉ κ°λ°μ μλλ₯Ό λμ΄λ κ²)
    - DBλ₯Ό κ°μ²΄λ‘ μ‘°μνκΈ° μν΄ ORMμ μ¬μ©
- λ¨μ 
  - ORM λ§μΌλ‘ μμ ν μλΉμ€λ₯Ό κ΅¬ννκΈ° μ΄λ €μ



## π  Django Model

### models.py

- ν΄λμ€ μμ±
  - λ°μ΄ν° λ² μ΄μ€μ νλμ μ€ν€λ§ λΉ νλμ ν΄λμ€λ‘ λ§λ€μ΄ μ€λ€.
  - models.Modelμ μμλ°λλ€. (λͺ¨λμ μ΄λ―Έ import λμ΄μλ€.)
  - PK(Primary Key)λ μμμ μμ±ν΄μ€λ€.
- λͺ¨λΈ νλλ [κ³΅μ ννμ΄μ§](https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types)λ₯Ό μ°Έκ³ νμ¬ μμ±νλ€.

- models.pyμ class λ§λ€κΈ°

  ```python
  class λͺ¨λΈλͺ(models.Model):
      # λͺ¨λΈμ νλ μμ± μλ μμ
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)	# μ΅μ΄ μμ± μΌμ
      updated_at = models.DateTimeField(auto_now=True)		# μ΅μ’ μμ  μΌμ
      
      audience = models.IntegerField()
      release_date = models.DateTimeField()
      score = models.FloatField()
      poster_url = models.URLField()
      
      def __str__(self):
          return self.title
  ```

- λͺ¨λΈμ μλ‘μ΄ μ€κ³λλ₯Ό λ§λ λ€.

  ```bash
  $ python manage.py makemigrations
  ```

- μ€κ³λλ₯Ό μ€μ  DBμ λ°μ.

  ```bash
  $ python manage.py migrate
  ```

- sql κ΅¬λ¬Έμ λ³΄κΈ° μν¨

  ```bash
  $ python manage.py sqlmigrate <app λͺ> 0001
  ```

- migrations μ€κ³λλ€μ΄ migrate λλμ§ νμΈ

  ```bash
  $ python manage.py showmigrations
  ```

> νμ΄λΈμ λμΌλ‘ λ³΄κ³  μΆμ κ²½μ°
>
> μ€νμ°½μ μΌμ SQLite: OPEN Databaseλ₯Ό ν΄λ¦­νλ€.
>
> νλ‘μ νΈ ν΄λμ μλ db.sqlite3λ₯Ό μ°κ²°μμΌμ€λ€.
>
> μμ  ν ν­μ μλ‘κ³ μΉ¨!!

- **νμ΄λΈμ μ κ±°νκ³  μΆμ λ models.pyμμ λ€ μ£Όμμ²λ¦¬νκ³  λ€μ μ κ³Όμ μ λ°λ³΅νλ€.**
  - μ΄ λ κ΄λ ¨λ views.pyμμλ μ£Όμμ²λ¦¬ν΄μΌ μλ¬κ° λμ§ μλλ€.




### seed μΆκ°

- νμ€νΈ λ°μ΄ν° μλ μμ±
- μ₯κ³  μλ μ€μΉ

```bash
$ pip install django-seed
```

- settings.py - INSTALLED_APPSμ λͺ¨λ μΆκ°

```python
INSTALLED_APPS = (
    ... 
    'django_seed', 
)
```

- λͺλ Ήμ΄ μ€ν

```bash
$ python manage.py seed articles --number 20
```



### fixture

- λ°μ΄ν°λ² μ΄μ€μ serialized λ λ΄μ©μ ν¬ν¨νλ νμΌ λͺ¨μ
- djangoκ° fixtures νμΌμ μ°Ύλ κ²½λ‘
  - app/ficxtures/

- κ° λͺ¨λΈ λ³ dumpdata μ€ν

  - λ°μ΄ν°λ² μ΄μ€μ μλ λ°μ΄ν°λ₯Ό .json νμΌλ‘ μ μ₯

  ```bash
  $ python manage.py dumpdata --indent 4 aritcles.article > articles.json
  $ python manage.py dumpdata --indent 4 accounts.user > users.json
  ```

- fixtureμ λ΄μ©μ κ²μνμ¬ λ°μ΄ν°λ² μ΄μ€λ‘ λ‘λ

  - λ¨, loaddata μ μ λ°μ΄ν°λ² μ΄μ€ μ­μ 

  ```bash
  $ python manage.py loaddata user.json
  $ python manage.py loaddata movies.json
  
  $ python manage.py loaddata articles/articles.json articles/comments.json accounts/users.json
  ```




## π Model Relation

### μΌλλ€ κ΄κ³(1:N)

- A many-to-one relationship

- ForeignKey

- 2κ°μ νμ μμΉ μΈμκ° νμ

  - μ°Έμ‘°νλ model class

  - on_delete μ΅μ

    - μΈλ ν€κ° μ°Έμ‘°νλ κ°μ²΄κ° μ¬λΌμ‘μ λ μΈλ ν€λ₯Ό κ°μ§ κ°μ²΄λ₯Ό μ΄λ»κ² μ²λ¦¬ν  μ§λ₯Ό μ μ

    - Database Integrity(λ°μ΄ν° λ¬΄κ²°μ±)μ μν΄μ λ§€μ° μ€μν μ€μ 

    - on_delete μ΅μμ μ¬μ© κ°λ₯ν κ°λ€

      - `CASCADE` : **λΆλͺ¨ κ°μ²΄(μ°Έμ‘° λ κ°μ²΄)κ° μ­μ  λμ λ μ΄λ₯Ό μ°Έμ‘°νλ κ°μ²΄λ μ­μ **
      - `PROTECT` : μ°Έμ‘°κ° λμ΄ μλ κ²½μ° μ€λ₯ λ°μ
      - `SET_NULL` : λΆλͺ¨κ°μ²΄κ° μ­μ  λμ λ λͺ¨λ  κ°μ NULLλ‘ μΉν (NOT NULL μ‘°κ±΄μ λΆκ°λ₯)
      - `SET_DEFAULT` : λͺ¨λ  κ°μ΄ DEFAULT κ°μΌλ‘ μΉν
        - DEFAULT μ€μ  μμ΄μΌ νλ©° DBμμλ λ³΄ν΅ defaultκ° μμΌλ©΄ nullλ‘ μ‘κΈ°λ ν¨. μ₯κ³ λ μλ.

      - `SET()` : νΉμ  ν¨μ νΈμΆ
      - `DO_NOTHING` : μλ¬΄κ²λ νμ§ μμ.

      - λ€λ§, λ°μ΄ν°λ² μ΄μ€ νλμ λν SQL `ON DELETE` μ ν μ‘°κ±΄μ μ€μ ν΄μΌ ν¨
      - `RESTRICT`

       (new in 3.1)

      - RestrictedErrorλ₯Ό λ°μμμΌ μ°Έμ‘° λ κ°μ²΄μ μ­μ λ₯Ό λ°©μ§

- κ²μκΈ(1) - λκΈ(N) μμ μ½λ

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

- μ₯κ³ λ μΈλν€λ₯Ό λ§λ€λ©΄ _idλ₯Ό λΆμ¬μ λ§λ€μ΄μ€λ€.

#### μ°Έμ‘°

μ°Έμ‘°λ μ½λ€. μ­μ°Έμ‘°κ° μ€μ!

```python
comment = Comment.objects.get(pk=1)
comment.article.content
```

#### μ­μ°Έμ‘°

- μμ μ μ°Έμ‘°νλ λκ΅°κ°λ₯Ό μ°Έμ‘°ν  λ

- `article.comment_set`

>```python
>article = model.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
>```
>
>μμ²λΌ μ¬μ©νμ¬ comment_setμμ commentsλ‘ λ³κ²½ κ°λ₯
>
>μ΄λ κ² νλ©΄ comment_setμ λͺ»μ΄λ€.
>
>`article.comments.all()`λ‘ μ¬μ©νλ€.
>
>`1:N`μμλ λ°κΎΈλ κ²μ κΆμ₯νμ§ μλλ€.
>
>`M:N`μμλ λ¬΄μ‘°κ±΄ μ¨μΌνλ μν©μ΄ μ¨λ€. κ·Έ λλ§ μ¬μ©νμ!!

- μμ

```python
article.comment_set.all()
comments = article.comment_set.all()
```

---

### λ€λλ€ κ΄κ³(M:N)

- 1:Nμ νκ³
  - μλ‘μ΄ μμ½μ μμ±νλ κ²μ΄ λΆκ°λ₯
  - μΈλ ν€μ 1, 2 νμμ μ¬λ¬ λ°μ΄ν°λ₯Ό μ¬μ©ν  μ μμ
- ManyToManyField
  - λ€λλ€ κ΄κ³ μ€μ  μ μ¬μ©νλ λͺ¨λΈ νλ
  - related_name : ForeignKeyμ related_nameκ³Ό λμΌ
  - symmetrical
    - 'self'λ₯Ό κ°λ¦¬ν€λ μ μμμλ§ μ¬μ©
    - symmetrical=True(κΈ°λ³Έκ°)μΌ κ²½μ° person_set λ§€λμ λ₯Ό μΆκ°νμ§ μμ
    - λμΉ­μ μνμ§ μλ κ²½μ° Falseλ‘ μ€μ 

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor, related_name='patients')

# symmetrical μμ 
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- μ€κ° λͺ¨λΈ νμ©
  - κ΄κ³ μ°κ²°νλ©΄μ κ΄κ³μ λ°λ₯Έ μμ±μ λ μΆκ°νκ³  μΆμ λ
  - through
    - μ€κ° νμ΄λΈμ μ§μ  μμ±νλ κ²½μ°, through μ΅μμ μ¬μ©νμ¬ μ€κ° νμ΄λΈμ λνλ΄λ Django λͺ¨λΈμ μ§μ ν  μ μμ


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

- μ€κ° λͺ¨λΈ μ€ λ°λμ μ­μ°Έμ‘°λ₯Ό μ¨μΌνλ μν©
  - 1:N κ΄κ³μμ μ΄λ―Έ ν΄λΉ λ©λμ  μ΄λ¦μ μ¬μ© μ€μΈ κ²½μ°
  - ManyToManyμμλ λ³΅μνμ ννμΌλ‘ λ°λμ related_nameμ μ μΈνμ!

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



## π Django User Model

- Custom User λͺ¨λΈ μ μνκΈ°

  - AbstractUserλ₯Ό μμλ°μ μλ‘μ΄ User λͺ¨λΈ μμ±
  - νλ‘μ νΈ μ€κ°μ λ³κ²½νλ©΄ ν¨μ¬ λ μ΄λ €μ΄ μμμ΄ νμνλ―λ‘ μ΄κΈ°μ μ€μ νλ κ²μ κΆμ₯

  ```python
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

  

- κΈ°μ‘΄ Djangoκ° μ¬μ©νλ User λͺ¨λΈμ΄μλ auth μ±μ User λͺ¨λΈμ accounts μ±μ User λͺ¨λΈμ μ¬μ©νλλ‘ λ³κ²½

  - settings.pyμ μλμ κ°μ΄ μΆκ°

    ```python
    AUTH_USER_MODEL = 'accounts.User'
    ```



## π Django Shell

- DBλ₯Ό ν°λ―Έλμμ μ‘°μνκΈ° μν¨

  ```bash
  $ pip install ipython
  $ pip install django-extensions
  ```

- INSTALLED_APPSμ `'django_extensions',` μΆκ°

  ```bash
  $ python manage.py shell_plus
  ```

- μ€ν μ·¨μνκ³  μΆμΌλ©΄ exit()

- μμμ μνλ μ΄λ¦μΌλ‘ νμΈνκΈ° μν λ°©λ²(modelμ μ μΈ)

  ```python
  # pk - μ λͺ©μΌλ‘
  def __str__(self):
      return f'{self.pk} - {self.title}'
  
  # μ λͺ©μΌλ‘
  def __str__(self):
          return self.title
  ```



## π Django Admin

- κ΄λ¦¬μ κ³μ  μμ±

```bash
$ python manage.py createsuperuser
```

- admin.pyμμ μ€μ νμ¬ admin νμ΄μ§μ Modelμ΄ λ³΄μ΄κ² ν΄μ€λ€.

```python
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)

# list_display #
# class ArticleAdmin(admin.ModelAdmin):
#	list_display = ('pk', 'title',)
# admin.site.register(Article, ArticleAdmin)
```

- Custom User λͺ¨λΈ λ±λ‘

```python
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



