cnt_input = int(input())
len_lst = [list() for _ in range(51)]   # 1차원 인덱스가 길이인 리스트에 문자열을 2차원에 담는다.
for _ in range(cnt_input):
    string = input()
    length = len(string)
    if string not in len_lst[length]:   # 중복된 값은 제거한다.
        len_lst[length].append(string)

for lst in len_lst:
    if len(lst):
        # sorted함수로 분류하여 join메서드로 문자열 사이에 개행문자를 넣고 print한다.
        print('\n'.join(sorted(lst)))
