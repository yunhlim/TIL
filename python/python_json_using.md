# [Python] json 파일 사용

```python
import json

a_json = open('경로/a.json', encoding = 'utf-8')
a_dict = json.load(a_json)	#=> 파이썬 자료형(딕셔너리나 리스트)으로 반환
```

`open()`함수를 사용해 경로와 이름을 적고 파일을 불러온다.

`json.load()` 함수로 json 파일을 파이썬의 딕셔너리나 리스트 자료형으로 반환한다.