# [Algorithm] 재귀(recur)

재귀는 알고리즘 설계 및 구현에서 유용하게 사용하며 기초이다.

자기 자신을 호출하는 함수를 만들어서 사용한다.

1개 이상의 **base case**(기저 케이스)가 존재하고 수렴하도록 작성한다.

대표적인 것이 `factorial`

## 📒 코드

```python
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
```

`4!`의 결과 : 24

---

알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수 사용한다.

즉 점화식으로 쉽게 표현할 수 있으면 재귀함수로 표현하기 쉽다.

### 장점

- 변수 사용을 줄일 수 있다는 장점이 있다. 재귀를 거치며 각각의 호출마다 값을 따로 저장한다. 각각 스택 메모리에 저장할 수 있으니 따로 생각해주지 않아도 된다.(반복문은 따로 저장해서 사용해야 하니 저장해야할 변수가 늘어난다.)
- 점화식으로 표현되는 경우 간단하게 직관적으로 표현할 수 있다.

### 단점

- 스택 메모리를 사용하니 메모리 양이 많아진다. 
- 함수를 호출하고 불러오는 시간이 부가적으로 걸린다. 반복문에 비해 오래 걸리니 시간복잡도를 생각하며 사용해야 한다.
- 파이썬의 경우 재귀의 깊이 제한이 있다.