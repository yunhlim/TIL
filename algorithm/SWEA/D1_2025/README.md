# SWEA 2025. N줄 덧셈

## 📚 문제

1부터 주어진 숫자만큼 모두 더한 값을 출력하시오. 단, 주어질 숫자는 10000을 넘지 않는다.

*[예제]* : 주어진 숫자가 10 일 경우 출력해야 할 정답은,

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

```
Input
10

Output
55
```

---

`for else` 구문을 사용해 본다. for문을 통과한 후 중간에 break에 걸리지 않으면 else문을 통과한다. else문을 통과할 때 print문을 출력한다.

## 📒 코드

```python
number = int(input())
result = 0
   
for i in range(1, number+1):
    result += i
else:
    print(result)
```

## 🔍 결과 : **Pass**