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

