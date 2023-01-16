# [Programmers] Lv 1 [1차] 비밀지도 [2018 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [[1차] 비밀지도](https://school.programmers.co.kr/learn/courses/30/lessons/17681)

## 📖 2진법으로 바꾸어 푼 풀이

이진법으로 바꾸기 위해 재귀함수를 사용했다.

주어진 n을 이용해 n번 재귀함수를 거치며 답을 구했다.

나머지를 오른쪽에 붙이며, 몫을 다시 재귀함수에 담아 n번이 넘으면 종료했다.

수가 작은 경우도 n번 거쳐야 하니 조금 비효율적이라, 몫이 0인 순간 길이만큼 0을 붙여주면 시간을 더 줄일 수는 있겠다. 어차피 주어진 n이 작아서 큰 상관은 없었다.

## 📒 2진법 변환 코드

```python
def solution(n, arr1, arr2):
    def tenTotwo(cur, x):
        if cur == n:
            return ""
        mok = x // 2
        nameji = x % 2
        return f"{tenTotwo(cur + 1, mok)}{nameji}"
    
    answer = ["" for _ in range(n)]
    
    for i in range(n):
        line1 = tenTotwo(0, arr1[i])
        line2 = tenTotwo(0, arr2[i])
        
        for j in range(n):
            if int(line1[j]) or int(line2[j]):
                answer[i] += "#"
            else:
                answer[i] += " "
                
    return answer
```

## 📖 비트 연산자를 활용한 풀이

비트 연산자를 활용하면 더 쉽게 풀 수 있을거란 생각이 떠올라 새로 풀어보았다.

`x & (1 << j)`를 활용해 특정 비트에 값이 있는지 비교한다. 이는 2진법의 자리 수가 있는지 확인하는 방법이다.

따라서 n번 반복문을 돌며(역으로 돌아야 큰 자리 수부터 확인 가능하다.) 위의 특정 비트에 값이 있는 지 확인하여 1이 둘 중 하나라도 있으면 #을 붙이고 아니면 공백을 붙여서 출력한다.

## 📒 비트 연산자 코드

```python
def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    for i in range(n):
        num1 = arr1[i]
        num2 = arr2[i]
        for j in range(n)[::-1]:
            if num1 & (1 << j) or num2 & (1 << j):
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer
```

