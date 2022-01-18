input_string = 'abcdef'
dic = dict(zip(input_string, range(6)))

for key in dic:   # 딕셔너리 for문 응용
    print(f'{key}: {dic[key]}')