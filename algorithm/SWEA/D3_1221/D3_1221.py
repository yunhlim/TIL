import sys
sys.stdin = open("GNS_test_input.txt")

# 문자를 정수로 치환하여 정렬
# def change_i(c):
#     chars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in range(10):
#         if c == chars[i]:
#             return i
#
#
# def change_str(num):
#     chars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in range(10):
#         if i == num:
#             return chars[i]
#
#
# T = int(input())
# for _ in range(T):
#     tc, N = input().split()
#     N = int(N)
#     nums = list(map(change_i, input().split()))
#     num_cnt = [0 for _ in range(10)]
#     strs = []
#     for i in nums:
#         num_cnt[i] += 1
#     for i in range(10):
#         strs += [i for _ in range(num_cnt[i])]
#
#     strs = map(change_str, strs)
#     print(tc)
#     print(*strs)


# T = int(input())
# num_chr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for _ in range(T):
#     tc, N = input().split()
#     N = int(N)
#     chrs = input().split()
#     sort_chrs = []
#     for i in range(10):
#         for c in chrs:
#             if num_chr[i] == c:
#                 sort_chrs.append(c)
#     print(tc)
#     print(*sort_chrs)


# T = int(input())
# num_chr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for _ in range(T):
#     tc, N = input().split()
#     N = int(N)
#     chrs = input().split()
#     sort_cnt = [0 for _ in range(10)]
#
#     for c in chrs:
#         for i in range(10):
#             if c == num_chr[i]:
#                 sort_cnt[i] += 1
#                 break
#     sort_chrs = []
#     for i in range(10):
#         sort_chrs += [num_chr[i]] * sort_cnt[i]
#
#     print(tc)
#     print(*sort_chrs)


# 딕셔너리 사용
T = int(input())
num_dict = {}   # 각각의 문자를 key로, 문자의 개수를 값으로 담을 딕셔너리
chr_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(T):
    tc, N = input().split()
    chrs = input().split()
    for c in chr_lst:   # 각각의 key 값을 입력하고 값은 0으로 초기화
        num_dict[c] = 0
    for c in chrs:  # 입력된 문자들과 같은 해당 key의 값에 1씩 개수를 추가해준다.
        num_dict[c] += 1
    sort_chrs = []  # 출력시킬 리스트
    for c in chr_lst:   # 딕셔너리의 key를 개수만큼 ZRO -> NIN 순서로 출력시킨다.
        sort_chrs += [c] * num_dict[c]
    print(tc)
    print(*sort_chrs)
