# [JavaScript] lodash [EP 09]

## 📚 lodash library란?

- https://lodash.com/
- CDN copy하여 사용
- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- array, object등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
- `_.`을 사용하기 때문에 명칭이 loadsh이다!
- `reverse,` `sortBy`, `range`, `random`, `cloneDeep` 등이 있다.

```javascript
<body>
	<script src="<https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js>"></script>
	<script>
		// 위의 CDN import 를 통해 _ (underscore) 식별자 사용가능
		_.sample([1, 2, 3, 4]) // 3 (random 1 element)
		_.sampleSize([1, 2, 3, 4], 2) // [2, 3] (random 2 element)

		_.reverse([1, 2, 3, 4]) // [4, 3, 2, 1]

		_.range(5) // [0, 1, 2, 4]
		_.range(1, 5) // [1, 2, 3, 4]
		_.range(1, 5, 2) // [1, 3]
	</script>
</body>
<script src="<https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js>"></script>
<script>
	const original = { a: { b: 1 } }
	const ref = original
	const copy = _.cloneDeep(original)

	console.log(original.a.b, ref.a.b, copy.a.b) // 1, 1, 1
	ref.a.b = 10
	console.log(original.a.b, ref.a.b, copy.a.b) // 10, 10, 1
	copy.a.b = 100
	console.log(original.a.b, ref.a.b, copy.a.b) // 10, 10, 100
</script>
```

- lodash 를 사용하지 않을 경우, 깊은 복사는 직접 함수를 만들어서 구현해야 함 (내장된 깊은복사 관련 함수 없음)

---

## 📌 lodash 관련 정보 글!

https://velog.io/@kysung95/%EC%A7%A4%EB%A7%89%EA%B8%80-lodash-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90