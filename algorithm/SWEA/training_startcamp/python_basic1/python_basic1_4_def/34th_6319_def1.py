word = input()


def reverse(word) :
    word_rev = ''
    for c in word:
        word_rev = c+word_rev
    print(word_rev)
    if word == word_rev :
        print('입력하신 단어는 회문(Palindrome)입니다.')
        
        
reverse(word)