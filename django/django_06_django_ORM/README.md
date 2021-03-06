# [Django] Django ORM [EP 06]

## π κΈ°λ³Έ CRUD λ‘μ§

1. λͺ¨λ  user λ μ½λ μ‘°ν

   ```python
   User.objects.all()
   ```
   
2. user λ μ½λ μμ±

   ```python
   User.objects.create(first_name='κΈΈλ', last_name='ν', age=100, country='μ μ£Όλ')
   ```
   


3. ν΄λΉ user λ μ½λ μ‘°ν

   - `102` λ² idμ μ μ²΄ λ μ½λ μ‘°ν

   ```python
   User.objects.get(pk=101)
   ```
   
4. ν΄λΉ user λ μ½λ μμ 

   - `102` λ² κΈμ `last_name` μ 'κΉ' μΌλ‘ μμ 

   ```python
   user = User.objects.get(pk=101)
   user.last_name = 'κΉ'
   user.save()
   ```

5. ν΄λΉ user λ μ½λ μ­μ 

   - `101` λ² κΈ μ­μ 
   
   ```python
   User.objects.get(pk=101).delete()
   ```
   

---

## π μ‘°κ±΄μ λ°λ₯Έ μΏΌλ¦¬λ¬Έ

1. μ μ²΄ μΈμ μ

   - `User` μ μ μ²΄ μΈμμ

   ```python
   User.objects.count()
   
   len(User.objects.all())
   ```
   
2. λμ΄κ° 30μΈ μ¬λμ μ΄λ¦

   - `.values` νμ©
     - μμ: `User.objects.filter(μ‘°κ±΄).values(μ»¬λΌμ΄λ¦)`

   ```python
   User.objects.filter(age=30).values('first_name')
   # <QuerySet [{'first_name': 'μν'}, {'first_name': 'λ³΄λ'}, {'first_name': 'μμ'}]>
   
   # μ°Έκ³ 
   user = User.objects.filter(age=30).values('first_name')
   # <QuerySet [{'first_name': 'μν'}, {'first_name': 'λ³΄λ'}, {'first_name': 'μμ'}]>
   
   type(user)
   # <class 'django.db.models.query.QuerySet'>
   
   user.first().get('first_name')
   # 'μν'
   
   user[0].get('first_name')
   # 'μν'
   ```
   
   
   
3. λμ΄κ° 30μ΄ μ΄μμΈ μ¬λμ μΈμ μ

   - ORM: `__gte` , `__lte` , `__gt`, `__lt` -> λμκ΄κ³ νμ©

   ```python
   User.objects.filter(age__gte=30).count()
   ```
   
4. λμ΄κ° 20μ΄ μ΄νμΈ μ¬λμ μΈμ μ

   ```python
   User.objects.filter(age__lte=20).count()
   # 23
   ```
   
5. λμ΄κ° 30μ΄λ©΄μ μ±μ΄ κΉμ¨μΈ μ¬λμ μΈμ μ

   ```python
   User.objects.filter(age=30, last_name='κΉ').count()
   # 1
   
   # λμΌ - λ¨, λ¦¬ν΄λλκ² μΏΌλ¦¬μ κ°μ²΄
   User.objects.filter(age=30).filter(last_name='κΉ')
   ```
   
   > - **`OR` μ νμ©νκ³  μΆλ€λ©΄, `Q`object λ₯Ό νμ©νμ¬μΌ νλ€.**
   >
   >   [κ³΅μλ¬Έμ](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects)
   
6. λμ΄κ° 30μ΄κ±°λ μ±μ΄ κΉμ¨μΈ μ¬λ?

   ```python
   # κΈ°μ‘΄μ λ°©λ²λλ‘ filterλ§ μ¬μ©νλ©΄
   (User.objects.filter(age=30) | User.objects.filter(last_name='κΉ')).count()
   
   # μ΄λ, Qλ₯Ό μ΄μ©νλ©΄ μ‘°κΈ λ κ°λ¨νλ€.
   from django.db.models import Q
   User.objects.filter(Q(age=30) | Q(last_name='κΉ'))
   
   # μ΄ μΈμμ
   User.objects.filter(Q(age=30) | Q(last_name='κΉ')).count()
   # 26
   ```
   
7. μ§μ­λ²νΈκ° 02μΈ μ¬λμ μΈμ μ

   - `__startswith`
   - μ£Όμ! `%` μμΌλμΉ΄λμ΄λ€. `_` λ μ κ·ννμ νμ

   ```python
   User.objects.filter(phone__startswith='02-').count()
   # 24
   ```
   
8. κ±°μ£Ό μ§μ­μ΄ κ°μλμ΄λ©΄μ μ±μ΄ ν©μ¨μΈ μ¬λμ μ΄λ¦

   - `.values()` λ κ°μ λ½μ λ΄κ³  μΆμ λ°μ΄ν°μ νλμ κ°μ κ°μ Έμ¨λ€.
   - `filter` λ κ°μ κ°μλ₯Ό λ³΄μ₯ν  μ μκΈ° λλ¬Έμ λ¬΄μ‘°κ±΄ QuerySetμΌλ‘ return λλ€.

   ```python
   # .values νμΈ
   
   User.objects.filter(age__gte=30).values()
   
   User.objects.filter(age__gte=30).values('first_name')
   ```

   ```PYTHON
   User.objects.filter(country='κ°μλ', last_name='ν©').values('first_name')
   # <QuerySet [{'first_name': 'μμ '}]>
   
   # μ‘°κ±΄μ λΆν©νλ μ²«λ²μ§Έ μ¬λμ μ΄λ¦
   User.objects.filter(country='κ°μλ', last_name='ν©').values('first_name').first().get('first_name')
   # 'μμ '
   
   # μ‘°κ±΄μ λΆν©νλ μ²«λ²μ§Έ μ¬λμ ν°λ²νΈ
   user = User.objects.filter(country='κ°μλ', last_name='ν©').values('first_name').first()
   
   type(user)
   # user.models.User
   
   user.phone
   # '016-5956-2725'
   ```
   

---

## π μ λ ¬ λ° LIMIT, OFFSET

1. λμ΄κ° λ§μ μ¬λμμΌλ‘ 10λͺ

   ```python
   User.objects.order_by('-age')[:10]
   ```

2. μμ‘μ΄ μ μ μ¬λμμΌλ‘ 10λͺ

   ```python
   User.objects.order_by('balance')[:10]
   
   # id=99 μ¬λμ μκ³  νμΈ - μ΅μ μ‘
   User.objects.get(id=99).balance
   # 150
   ```
   
3. μκ³ λ μ€λ¦μ°¨μ, λμ΄λ λ΄λ¦Όμ°¨μμΌλ‘ 10λͺ?

   ```python
   User.objects.order_by('balance', '-age')[:10]
   ```
   
4. μ±, μ΄λ¦ λ΄λ¦Όμ°¨μ μμΌλ‘ 5λ²μ§Έ μλ μ¬λ

   ```python
   User.objects.order_by('-last_name', '-first_name')[4]
   ```
   

---

## π ννμ

### Aggregate

> - [Djangoκ³΅μλ¬Έμμ°Έμ‘°](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation)
> - 'μ’ν©', 'μ§ν©', 'ν©κ³' λ±μ μ¬μ μ  μλ―Έ
> - μ§κ³ ν¨μ(Avg, Max, Min, Count, Sum λ±)μ μ¬μ©ν  λ μ¬μ©νλ λ©μλ.
> - νΉμ  νλ μ μ²΄μ ν©, νκ·  λ±μ κ³μ°ν  λ μ¬μ©
> - μ§κ³ ν¨μλ₯Ό νλΌλ―Έν°λ‘ λ°μμ λμλλ¦¬λ₯Ό λ°ν

1. μ μ²΄ νκ·  λμ΄

   ```python
   # age νλμ νκ·  κ°
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   # {'age__avg': 28.23}
   
   # μ΄λ¦μ νλμ ν¨μλ₯Ό μ‘°ν©ν΄ μλ μμ±λμ§λ§ λ€μκ³Ό κ°μ΄ μλμΌλ‘ μ΄λ¦μ μ§μ ν  μ μλ€.
   User.objects.aggregate(avg_value=Avg('age'))
   # {'avg_value': 28.23}
   ```
   
2. κΉμ¨μ νκ·  λμ΄

   ```python
   from django.db.models import Avg
   
   User.objects.filter(last_name='κΉ').aggregate(Avg('age'))
   # {'age__avg': 28.782608695652176}
   
   
   # λ μ΄μμ aggregate μμ±
   User.objects.filter(last_name='κΉ').aggregate(Avg('age'), Max('age'), Min('age'))
   # {'age__avg': 28.782608695652176, 'age__max': 39, 'age__min': 15}
   ```

3. κ°μλμ μ¬λ μ¬λμ νκ·  κ³μ’ μκ³ 

   ```python
   User.objects.filter(country='κ°μλ').aggregate(Avg('balance'))
   # {'balance__avg': 157895.0}
   ```
   
4. κ³μ’ μμ‘ μ€ κ°μ₯ λμ κ°

   ```python
   from django.db.models import Max
   
   User.objects.aggregate(Max('balance'))
   # {'balance__max': 1000000}
   ```
   
5. κ³μ’ μμ‘ μ΄μ‘

   ```python
   from django.db.models import Sum
   
   User.objects.aggregate(Sum('balance'))
   # {'balance__sum': 14425040}
   ```
   

### Annotate

- 'μ£Όμμ λ¬λ€' λΌλ μ¬μ μ  μλ―Έ

  - SQLμ `GROUP BY`

- νλλ₯Ό νλ λ§λ€κ³  κ±°κΈ°μ 'μ΄λ€ λ΄μ©'μ μ±μ λ£λλ€.
- λ°μ΄ν°λ² μ΄μ€μ μν₯μ μ£Όμ§ μκ³ , Querysetμ μ»¬λΌ νλλ₯Ό μΆκ°νλ κ²κ³Ό κ°λ€.

1. μ§μ­λ³ μΈμ μ

   ```python
   from django.db.models import Count
   
   User.objects.values('country').annotate(Count('country'))
   # κ° countryμ κ°μ
   
   User.objects.values('country').annotate(num_countries=Count('country'))
   # κ° country κ°μμ μ΄λ¦μ num_countriesλ‘ λ³κ²½
   
   User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
   # countryμ μ λΏλ§ μλλΌ balance νκ· λ ν¨κ» λ΄λλ€.
   ```

2. 1:N μμ

   - Article - Comment κ΄κ³κ° 1:N μΈ κ²½μ°

   ```PYTHON
   Article.objects.annotate(
       total_count=Count('comment'),
       pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
   )
   ```

   - `Article.objects.all()` μ λν΄μ annotateλ‘ μ°λ¦¬κ° νμλ‘ μΈν΄ λ§λ  2κ°μ μ»¬λΌ(`total_count`, `pub_date`)λ₯Ό λΆμ¬μ κ°μ Έμ€λ κ².
