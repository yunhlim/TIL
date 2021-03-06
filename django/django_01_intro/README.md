# [Django] Django Intro [EP 01]

## ๐ ์ฅ๊ณ (Django) ๋?

- ๊ฒ์ฆ๋ Python ์ธ์ด ๊ธฐ๋ฐ Web framework

> ํ๋ ์์ํฌ : ํ๋ก๊ทธ๋๋ฐ์์ ํน์  ์ด์์ฒด์ ๋ฅผ ์ํ ์์ฉ ํ๋ก๊ทธ๋จ ํ์ค ๊ตฌ์กฐ๋ฅผ ๊ตฌํํ๋ ํด๋์ค์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๋ชจ์
>
> Web framework ๋?
>
> ์น ํ์ด์ง๋ฅผ ๊ฐ๋ฐํ๋ ๊ณผ์ ์์ ๊ฒช๋ ์ด๋ ค์์ ์ค์ด๋ ๊ฒ์ด ์ฃผ ๋ชฉ์ !
>
> ๊ฐ๋ฐ์ ์ง์คํ๊ธฐ ์ํด ํ๊ฒฝ์ ์ ๊ณต(tool), ๊ฐ๋ฐ์ zero๋ถํฐ ์์ํ์ง ์๊ธฐ ์ํด์
>
> ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฐ๋, ํํ๋ฆฟ ํํ์ ํ์ค, ์ธ์ ๊ด๋ฆฌ, ์ฝ๋ ์ฌ์ฌ์ฉ ๋ฑ์ ๊ธฐ๋ฅ์ ํฌํจ.
>
> ๋์ ์ธ ์น ํ์ด์ง๋, ์น ์ ํ๋ฆฌ์ผ์ด์, ์น ์๋น์ค ๊ฐ๋ฐ ๋ณด์กฐ์ฉ์ผ๋ก ๋ง๋ค์ด์ง๋ Application framework์ ์ผ์ข

### Framework Architecture

- MVC Design Pattern (model-view-controller) - ๋๋ถ๋ถ์ ํ๋ ์์ํฌ๊ฐ ๋ฐ๋ฅด๋ ๋์์ธ ํจํด(์ฅ๊ณ ๋ ์ด ๋์์ธ ํจํด์ ๋ฐ๋ฅธ๋ค. ๊ทธ๋ฐ๋ฐ ๋ช์นญ์ ๋ฐ๊ฟ ๋ถ๋ฅธ๋ค)

  ์ฌ์ฉ์ ์ธํฐํ์ด์ค๋ก๋ถํฐ ํ๋ก๊ทธ๋จ ๋ก์ง์ ๋ถ๋ฆฌ ์๋ก ์ํฅ ์์ด ๊ณ ์น  ์ ์๋ค.

- ์ฅ๊ณ ๋ MTV Pattern์ด๋ผ๊ณ  ๋ถ๋ฅธ๋ค. ํน๋ณํ ์ด์ ๋ ์๋ค. view๋ฅผ template, controller๋ฅผ view๋ก ๋ถ๋ฅธ๋ค.

MTV ํจํด

- model: ์์ฉํ๋ก๊ทธ๋จ์ ๋ฐ์ดํฐ ๊ตฌ์กฐ๋ฅผ ์ ์, ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ๊ธฐ๋ก์ ๊ด๋ฆฌ(์ถ๊ฐ, ์์ , ์ญ์ )

- Temlate(view): ํ์ผ์ ๊ตฌ์กฐ๋ ๋ ์ด์์์ ์ ์, ์ค์  ๋ด์ฉ์ ๋ณด์ฌ์ฃผ๋ ๋ฐ ์ฌ์ฉ, ๋ณด์ฌ์ง๋ ๋ถ๋ถ ๊ด์ฅ

- **View**(controller): ํด๋ผ์ด์ธํธ ์์ฒญ(HTTP ์์ฒญ)์ ์๋ฒ๊ฐ ์์ ํ๊ณ  ์๋ต์ ๋ฐํํ๋ ๊ฒ, ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ๋ํ ์กฐํ(model๊ณผ์ ์ํต)๋ view๊ฐ ์งํ, template์๊ฒ ์๋ต์ ์์ ์ค์ ์ ๋งก๊น, ํ๋ ์ผ์ด ๊ฐ์ฅ ๋ง๋ค, ๊ฐ์ฅ ์ค์!

  > ํด๋ผ์ด์ธํธ -> ์๋ฒ : ์์ฒญ
  >
  > ํด๋ผ์ด์ธํธ <- ์๋ฒ : ์๋ต
  >
  > ex). ํด๋ผ์ด์ธํธ(์น๋ธ๋ผ์ฐ์  - ํฌ๋กฌ), ์๋ฒ(๋ค์ด๋ฒ)



## ๐ฅ Django ์์ํ๊ธฐ

### ๊ฐ์ํ๊ฒฝ ์ธํ

- ๋๋ฆฝ์ ์ธ ๊ฐ๋ฐ ํ๊ฒฝ์ ๋ง๋ค๊ธฐ ์ํด ์ค์นํ๋ค.

- git bash๋ vs code IDE๋ฅผ ์คํํด ํฐ๋ฏธ๋์ ๋ช๋ น์ด๋ฅผ ์๋ ฅํ์ฌ ์์ฑ(๊ฐ์ํ๊ฒฝ์ด๋ฆ์ venv๋ก ์ฃผ๋ก ์ง๋๋ค.)

  ```bash
  $ python -m venv [๊ฐ์ํ๊ฒฝ์ด๋ฆ]
  $ source [๊ฐ์ํ๊ฒฝ์ด๋ฆ]/Scripts/activate
  ```



### Django ์ค์น

- ๊ฐ์ํ๊ฒฝ์ ์คํํ ํ ์ค์นํ๋ค.(4๋ฒ์ ์ด ์๋ ์์ ์ ์ธ 3๋ฒ์ ์ผ๋ก ์ค์นํ๋ค.)

  ```bash
  $ pip install django==3.2.12
  ```



### Project  ์์ฑ

- ํ๋ก์ ํธ๋ ํ๋ ์์ฑํ๋ค. ์ด๋ฆ์๋ ํค์๋๋ `-`์ ํผํด์ผํ๋ค.

  ```bash
  $ django-admin startproject [ํ๋ก์ ํธ๋ช] .
  ```



### Project ๊ตฌ์กฐ

- asgi.py - ๋์ค์ ๋ค๋ฅธ์ฌ๋๋ค๋ ์ฌ์ฉํ๊ฒ ํ๊ธฐ ์ํ ๋ฐฐํฌํ  ๋ ์ฌ์ฉ!

- **settings.py** - ์ค์!  ์ ํ๋ฆฌ์ผ์ด์์ ๋ชจ๋  ์ค์ ์ ํฌํจ

- urls.py - ์ฌ์ดํธ์ **url**๊ณผ ์ ์ ํ views์ ์ฐ๊ฒฐ์ ์ง์ 

- wsgi.py - ๋ค๋ฅธ ์๋ฒ์ ์ฐ๊ฒฐํ  ๋ ๋ฐฐํฌํ  ๋ ๋์์ ์ค ์ ์๋ ํ์ผ

- manage.py - ์ปค๋งจ๋๋ฅผ ๋์์ํค๋ ์ญํ , ์์  X



### Application ์์ฑ

- ์ผ๋ฐ์ ์ผ๋ก ๋ณต์ํ์ผ๋ก ์ง๋๋ค.
- ํ๋์ ํ๋ก์ ํธ์ ์ฌ๋ฌ๊ฐ์ง ๊ธฐ๋ฅ์ ๋งก๋ App ์ฌ๋ฌ ๊ฐ๋ฅผ ๋ง๋ค์ด์ ์ฌ์ฉํ๋ค.

```bash
$ python manage.py startapp [์ดํ๋ชs]
```



### Application ๊ตฌ์กฐ

admin.py - ๊ด๋ฆฌ์์ฉ ํ์ด์ง๋ฅผ ์ค์ ํ๋ ๊ณณ

apps.py - ์ฑ์ ์ ๋ณด๊ฐ ์์ฑ๋ ๊ณณ, ์์  X

models.py - ์ฑ์์ ์ฌ์ฉํ๋ Model์ ์ ์ํ๋ ๊ณณ

tests.py - ํ๋ก์ ํธ์ ํ์คํธ ์ฝ๋๋ฅผ ์์ฑํ๋ ๊ณณ, ์์  X

views.py - view ํจ์๋ค์ด ์ ์ ๋๋ ๊ณณ

> template์ ์ฅ๊ณ  ๋ช๋ น์ด๋ก ์์ฑ๋๋ ๊ฒ์ด ์๋๋ค. 
>
> template์ ์ง์  ์์ฑํด์ค์ผ ํ๋ค.



### App ๋ฑ๋ก

ํ๋ก์ ํธ์ settings.py์ INSTALLED_APPS์ `'์ดํ๋ช',` ์ ์ถ๊ฐํด์ค๋ค.