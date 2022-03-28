# [Python] json 파일 및 txt 파일 불러오기

## json 파일

```python
import json

a_json = open('경로/a.json', encoding = 'utf-8')
a_dict = json.load(a_json)	#=> 파이썬 자료형(딕셔너리나 리스트)으로 반환
```

`open()`함수를 사용해 경로와 이름을 적고 파일을 불러온다.

`json.load()` 함수로 json 파일을 파이썬의 딕셔너리나 리스트 자료형으로 반환한다.

---

## txt 파일

```python
import sys
sys.stdin = open("input.txt")
```

`open()` 함수를 사용해 파일을 불러온다.

알고리즘 문제를 풀 때 입력 txt 파일이 주어지는 경우, 이를 활용한다. (ex. SWEA)