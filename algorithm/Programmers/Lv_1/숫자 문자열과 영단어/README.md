# [Programmers] Lv 1. 숫자 문자열과 영단어 [2021 카카오 채용연계형 인턴십]

## 📚 문제 : [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301)

## 📖 풀이

문자열 **replace** 메서드를 이용해 각각 대응되는 문자를 숫자로 바꿔준다.

문자열을 다 숫자로 바꾼 후 int로 형변환하여 출력한다.

## 📒 코드

```python
def solution(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    return int(s)
```

