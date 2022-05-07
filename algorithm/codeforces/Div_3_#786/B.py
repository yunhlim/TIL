t = int(input())
for _ in range(t):
    result = 0
    word = input()
    result += 25 * (ord(word[0]) - ord('a'))
    if ord(word[1]) > ord(word[0]):
        result += ord(word[1]) - ord('a')
    else:
        result += ord(word[1]) - ord('a') + 1
    print(result)