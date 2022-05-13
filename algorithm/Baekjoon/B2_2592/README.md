# [Baekjoon] 2592. 대표값 [B2]

## 📚 문제 : [대표값](https://www.acmicpc.net/problem/2592)

## 📖 풀이

평균은 다 더한 후 나눠주면 된다.

최빈값을 구할 때는 가장 많이 나온 수를 구하는 것이므로 딕셔너리에 수를 key로 개수를 값으로 담아준다.

딕셔너리를 순회하며 가장 값이 큰 key를 출력한다.

## 📒 코드

```python
dic = {}
total = 0
for i in range(10):
    x = int(input())
    dic[x] = dic.get(x, 0) + 1
    total += x

print(total//10)

many_cnt = 0
many_value = 0
for key, value in dic.items():
    if value > many_cnt:
        many_cnt = value
        many_value = key
        
print(many_value)
```

## 🔍 결과

![image-20220513181351711](README.assets/image-20220513181351711.png)