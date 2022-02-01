# [Alogorithm] input 속도 개선[Python]

파이썬(python) 백준 문제를 풀면 입력이 많을 때 시간초과가 발생한다.

입력으로 input()만 쓰는 대신

```python
import sys
input = sys.stdin.readline
```

이걸 맨 위에 적어준 후

나머지는 똑같이 input()으로 사용하면 input이 sys.stdin.readline으로 동작한다.