# [Baekjoon] 2592. λνκ° [B2]

## π λ¬Έμ  : [λνκ°](https://www.acmicpc.net/problem/2592)

## π νμ΄

νκ· μ λ€ λν ν λλ μ£Όλ©΄ λλ€.

μ΅λΉκ°μ κ΅¬ν  λλ κ°μ₯ λ§μ΄ λμ¨ μλ₯Ό κ΅¬νλ κ²μ΄λ―λ‘ λμλλ¦¬μ μλ₯Ό keyλ‘ κ°μλ₯Ό κ°μΌλ‘ λ΄μμ€λ€.

λμλλ¦¬λ₯Ό μννλ©° κ°μ₯ κ°μ΄ ν° keyλ₯Ό μΆλ ₯νλ€.

## π μ½λ

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

## π κ²°κ³Ό

![image-20220513181351711](README.assets/image-20220513181351711.png)