bloods = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
bloods_dic = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

for i in bloods:
    if i == 'A':
        bloods_dic['A'] += 1
    elif i == 'O':
        bloods_dic['O'] += 1
    elif i == 'B':
        bloods_dic['B'] += 1
    else:
        bloods_dic['AB'] += 1

print(bloods_dic)