# [Algorithm] 객체 정렬(python)

python에서는 **Class**를 사용한다.

객체로 나타낼 때 튜플보다 클래스 방식으로 하는 것이 더 깔끔하고 추천!!



> private을 쓰는 이유
>
> 캡슐화 : 너희는 코드를 건들이지 말고 사용만 해라!



## 🍘 파이썬 클래스 변수 및 메서드

- 클래스 변수
  - 모든 인스턴스에 공용으로 사용되는 변수

- 클래스 메서드
  - 인스턴스를 정의하지 않아도 사용할 수 있는 메서드

```python
class Agent():
    # 클래스 변수
    babo_name = ""
    babo_score = 101

    def __init__(self, name, score):
       	score = int(score)
        self.name = name
        self.score = score
        if Agent.babo_score > score:	# 클래스 변수 값 변경
            Agent.babo_score = score
            Agent.babo_name = name
	# 클래스 메서드
    @classmethod
    def babo(cls):
        return cls.babo_name, cls.babo_score


agents = [Agent(*input().split()) for _ in range(5)]
print(*Agent.babo())	# 클래스 메서드 호출

```



## 🍔 객체 정렬

파이썬은 sort()의 key에 lambda를 활용한다.

객체 리스트가 있을 때 객체의 해당 변수를 기준으로 정렬시킬 수 있다.

`students.sort(key=lambda x: x.변수)`



## 🍟 파이썬 클래스의 print 메서드

`__str__()`를 정의한다. 정의하지 않으면 `__repr__()`이 반환된다. rerp는 클래스 이름과 객체의 주소를 반환한다.

```python
class Student():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):		# 파이썬의 __str__ : print에 대한 값 정의
        return f"{self.name} {self.height} {self.weight}"


n = int(input())
students = [Student(*input().split()) for _ in range(n)]
students.sort(key=lambda x: x.height)	# 객체 정렬

for i in range(n):
    print(students[i])
```

