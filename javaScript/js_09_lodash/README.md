# [JavaScript] lodash [EP 09]

## ๐ lodash library๋?

- https://lodash.com/
- CDN copyํ์ฌ ์ฌ์ฉ
- ๋ชจ๋์ฑ, ์ฑ๋ฅ ๋ฐ ์ถ๊ฐ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ JavaScript ์ ํธ๋ฆฌํฐ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
- array, object๋ฑ ์๋ฃ๊ตฌ์กฐ๋ฅผ ๋ค๋ฃฐ ๋ ์ฌ์ฉํ๋ ์ ์ฉํ๊ณ  ๊ฐํธํ ์ ํธ๋ฆฌํฐ ํจ์๋ค์ ์ ๊ณต
- `_.`์ ์ฌ์ฉํ๊ธฐ ๋๋ฌธ์ ๋ช์นญ์ด loadsh์ด๋ค!
- `reverse,` `sortBy`, `range`, `random`, `cloneDeep` ๋ฑ์ด ์๋ค.

```javascript
<body>
	<script src="<https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js>"></script>
	<script>
		// ์์ CDN import ๋ฅผ ํตํด _ (underscore) ์๋ณ์ ์ฌ์ฉ๊ฐ๋ฅ
		_.sample([1, 2, 3, 4]) // 3 (random 1 element)
		_.sampleSize([1, 2, 3, 4], 2) // [2, 3] (random 2 element)
		_.random(1, 6)		// 2 (1 ~ 6 random์ผ๋ก ํ๋ ๊ณ ๋ฅธ๋ค)

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

- lodash ๋ฅผ ์ฌ์ฉํ์ง ์์ ๊ฒฝ์ฐ, ๊น์ ๋ณต์ฌ๋ ์ง์  ํจ์๋ฅผ ๋ง๋ค์ด์ ๊ตฌํํด์ผ ํจ (๋ด์ฅ๋ ๊น์๋ณต์ฌ ๊ด๋ จ ํจ์ ์์)

---

## ๐ lodash ๊ด๋ จ ์ ๋ณด ๊ธ!

https://velog.io/@kysung95/%EC%A7%A4%EB%A7%89%EA%B8%80-lodash-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90