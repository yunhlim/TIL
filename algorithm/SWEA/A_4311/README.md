# [SWEA] 4311. 오래된 스마트폰

## 📚 문제 : [오래된 스마트폰](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWL2vlPKMlQDFAUE&categoryId=AWL2vlPKMlQDFAUE&categoryType=CODE&problemTitle=4311&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 📖 풀이

A형 특유의 구현문제이다.

문제 구현 시 특이사항은 다음과 같다.

- 음수거나, 999를 넘어가면 문제가 발생한다.

- 연산 결과가 나오기 위해서는 무조건 =를 입력(연산하는 경우 마지막에만 =를 붙이면 된다.)

- 직접 숫자를 입력하여 만드는 경우는 =를 입력하지 않는다.

- 계산기 입력제한이 있어 터치 가능 최대 횟수는 M이다. (M은 20까지)

- 곱셈 나누기가 덧셈 뺄셈보다 우선적으로 실행되지 않고 순차적으로 실행된다.

터치 횟수마다 배열에 담아 준다.

될 수 없는 수는 제외한다!(가지치기)

위 처럼 푸려고 하면 메모리초과가 발생한다..

방법을 바꿔야 한다.

메모리 제한인 듯..?



새로운 방법

0~1000인 배열을 만든다.

누를 수 있는 숫자들로 만들 수 있는 숫자들을 먼저 다 찾는다. 배열에 1을 넣는다.

연산자를 활용해 그 숫자들과 계산한 결과를 배열에 2로 넣는다.

2인 것을 다시 연산해 3으로 넣는다.

숫자 연산자 숫자 =

1 + 1 =

3 * n + 1 < m번 하면된다.