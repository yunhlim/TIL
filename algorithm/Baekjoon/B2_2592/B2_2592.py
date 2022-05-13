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