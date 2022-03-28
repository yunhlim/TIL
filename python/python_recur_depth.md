# [Python] 재귀 깊이 제한 변경하기

python은 재귀의 깊이가 1000까지로 제한되어있다.

그 깊이보다 더 깊게 들어가면 `Recursion Error`가 발생한다.

따라서 해제하기 위해선 system 라이브러리를 사용한다.

## 📌 주의사항

> SWEA는 sys 사용이 불가능하여 사용할 수 없다.
>
> DFS나 BFS를 반복문으로 활용해야한다.

## 📒 코드

```python
import sys
sys.setrecursionlimit(5000)
```

위 코드를 삽입하여 재귀 제한을 변경할 수 있다.

외우기보단 sys를 검색 후 자동완성하여 사용하면 된다.