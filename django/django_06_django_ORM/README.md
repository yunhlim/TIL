# [Django] Django ORM [EP 06]

## 🍎 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   User.objects.all()
   ```
   
2. user 레코드 생성

   ```python
   User.objects.create(first_name='길동', last_name='홍', age=100, country='제주도')
   ```
   


3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   User.objects.get(pk=101)
   ```
   
4. 해당 user 레코드 수정

   - `102` 번 글의 `last_name` 을 '김' 으로 수정

   ```python
   user = User.objects.get(pk=101)
   user.last_name = '김'
   user.save()
   ```

5. 해당 user 레코드 삭제

   - `101` 번 글 삭제
   
   ```python
   User.objects.get(pk=101).delete()
   ```
   

---

## 🍒 조건에 따른 쿼리문

1. 전체 인원 수

   - `User` 의 전체 인원수

   ```python
   User.objects.count()
   
   len(User.objects.all())
   ```
   
2. 나이가 30인 사람의 이름

   - `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   User.objects.filter(age=30).values('first_name')
   # <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   
   # 참고
   user = User.objects.filter(age=30).values('first_name')
   # <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   
   type(user)
   # <class 'django.db.models.query.QuerySet'>
   
   user.first().get('first_name')
   # '영환'
   
   user[0].get('first_name')
   # '영환'
   ```
   
   
   
3. 나이가 30살 이상인 사람의 인원 수

   - ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   User.objects.filter(age__gte=30).count()
   ```
   
4. 나이가 20살 이하인 사람의 인원 수

   ```python
   User.objects.filter(age__lte=20).count()
   # 23
   ```
   
5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   User.objects.filter(age=30, last_name='김').count()
   # 1
   
   # 동일 - 단, 리턴되는게 쿼리셋 객체
   User.objects.filter(age=30).filter(last_name='김')
   ```
   
   > - **`OR` 을 활용하고 싶다면, `Q`object 를 활용하여야 한다.**
   >
   >   [공식문서](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects)
   
6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # 기존의 방법대로 filter만 사용하면
   (User.objects.filter(age=30) | User.objects.filter(last_name='김')).count()
   
   # 이때, Q를 이용하면 조금 더 간단하다.
   from django.db.models import Q
   User.objects.filter(Q(age=30) | Q(last_name='김'))
   
   # 총 인원수
   User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   # 26
   ```
   
7. 지역번호가 02인 사람의 인원 수

   - `__startswith`
   - 주의! `%` 와일드카드이다. `_` 는 정규표현식 필요

   ```python
   User.objects.filter(phone__startswith='02-').count()
   # 24
   ```
   
8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   - `.values()` 는 값을 뽑아 내고 싶은 데이터의 필드와 값을 가져온다.
   - `filter` 는 값의 개수를 보장할 수 없기 때문에 무조건 QuerySet으로 return 된다.

   ```python
   # .values 확인
   
   User.objects.filter(age__gte=30).values()
   
   User.objects.filter(age__gte=30).values('first_name')
   ```

   ```PYTHON
   User.objects.filter(country='강원도', last_name='황').values('first_name')
   # <QuerySet [{'first_name': '은정'}]>
   
   # 조건에 부합하는 첫번째 사람의 이름
   User.objects.filter(country='강원도', last_name='황').values('first_name').first().get('first_name')
   # '은정'
   
   # 조건에 부합하는 첫번째 사람의 폰번호
   user = User.objects.filter(country='강원도', last_name='황').values('first_name').first()
   
   type(user)
   # user.models.User
   
   user.phone
   # '016-5956-2725'
   ```
   

---

## 🍑 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   User.objects.order_by('-age')[:10]
   ```

2. 잔액이 적은 사람순으로 10명

   ```python
   User.objects.order_by('balance')[:10]
   
   # id=99 사람의 잔고 확인 - 최저액
   User.objects.get(id=99).balance
   # 150
   ```
   
3. 잔고는 오름차순, 나이는 내림차순으로 10명?

   ```python
   User.objects.order_by('balance', '-age')[:10]
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   User.objects.order_by('-last_name', '-first_name')[4]
   ```
   

---

## 🍏 표현식

### Aggregate

> - [Django공식문서참조](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation)
> - '종합', '집합', '합계' 등의 사전적 의미
> - 집계 함수(Avg, Max, Min, Count, Sum 등)을 사용할 때 사용하는 메서드.
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
> - 집계 함수를 파라미터로 받아서 딕셔너리를 반환

1. 전체 평균 나이

   ```python
   # age 필드의 평균 값
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   # {'age__avg': 28.23}
   
   # 이름은 필드와 함수를 조합해 자동 생성되지만 다음과 같이 수동으로 이름을 지정할 수 있다.
   User.objects.aggregate(avg_value=Avg('age'))
   # {'avg_value': 28.23}
   ```
   
2. 김씨의 평균 나이

   ```python
   from django.db.models import Avg
   
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   # {'age__avg': 28.782608695652176}
   
   
   # 둘 이상의 aggregate 생성
   User.objects.filter(last_name='김').aggregate(Avg('age'), Max('age'), Min('age'))
   # {'age__avg': 28.782608695652176, 'age__max': 39, 'age__min': 15}
   ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   # {'balance__avg': 157895.0}
   ```
   
4. 계좌 잔액 중 가장 높은 값

   ```python
   from django.db.models import Max
   
   User.objects.aggregate(Max('balance'))
   # {'balance__max': 1000000}
   ```
   
5. 계좌 잔액 총액

   ```python
   from django.db.models import Sum
   
   User.objects.aggregate(Sum('balance'))
   # {'balance__sum': 14425040}
   ```
   

### Annotate

- '주석을 달다' 라는 사전적 의미

  - SQL의 `GROUP BY`

- 필드를 하나 만들고 거기에 '어떤 내용'을 채워 넣는다.
- 데이터베이스에 영향을 주지 않고, Queryset에 컬럼 하나를 추가하는 것과 같다.

1. 지역별 인원 수

   ```python
   from django.db.models import Count
   
   User.objects.values('country').annotate(Count('country'))
   # 각 country의 개수
   
   User.objects.values('country').annotate(num_countries=Count('country'))
   # 각 country 개수의 이름을 num_countries로 변경
   
   User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
   # country의 수 뿐만 아니라 balance 평균도 함께 담는다.
   ```

2. 1:N 예시

   - Article - Comment 관계가 1:N 인 경우

   ```PYTHON
   Article.objects.annotate(
       total_count=Count('comment'),
       pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
   )
   ```

   - `Article.objects.all()` 에 더해서 annotate로 우리가 필요로 인해 만든 2개의 컬럼(`total_count`, `pub_date`)를 붙여서 가져오는 것.
