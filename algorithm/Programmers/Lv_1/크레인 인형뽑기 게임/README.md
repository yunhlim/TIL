# [Programmers] Lv1. 크레인 인형뽑기 게임 [2019 카카오 개발자 겨울 인턴십] - JAVA

## 📚 문제 : [크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061#)

## 📖 풀이

스택을 구현해서 해결하는 문제이다.

### 스택 배열 선언 방법

2차원 스택을 구현하고 싶어 한 참을 헤맸다. java에서 객체 배열을 선언하는 방법은 객체에 `[]`를 붙이면 된다.

그렇지만 stack은 제네릭을 붙여줘야 한다. 여기서 int를 담을 것이기 때문에 Integer로 선언한다. 그리고 반복문을 돌며 배열 뿐 아니라 각각 스택을 선언해줘야 한다.

```java
// stack 배열 선언
Stack<Integer>[] board_stacks = new Stack[board.length];
for(int i = 0; i < board.length; i++) {
    board_stacks[i] = new Stack<Integer>();
}
```

입력으로 주어진 board의 반복문을 역순으로 돌며 하나씩 채워준다. 0은 없으니 채우지 않고, 있는 값만 채워준다.

stack의 메서드로 4가지를 사용한다.

- push : 삽입
- pop : 삭제(peek값 반환)
- empty : 값이 없으면 true, 있으면 false 반환
- peek : peek 값 반환

인형뽑기를 진행해 담을 바구니 스택을 하나 만든다.

바구니 스택에 담아줄 때, peek 값과 같은 값을 넣으면 peek 값을 삭제하고 아니면 스택에 담는다.

사라지는 인형의 개수를 출력해야 하니 삭제할 때마다 2를 더해준다.

## 📒 코드

```java
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        // 뽑은 인형을 담을 바구니 스택
        Stack<Integer> baguni = new Stack<Integer>();
        // 2차원 stack 선언
        Stack<Integer>[] board_stacks = new Stack[board.length];
        for(int i = 0; i < board.length; i++) {
        	board_stacks[i] = new Stack<Integer>();
        }
        
        for (int i = board.length - 1; i >= 0; i--) {
            for (int j = 0; j < board[0].length; j++) {
                int doll = board[i][j];
                // 인형이 있을 때
                if (doll != 0) {
                    board_stacks[j].push(doll);
                }
            }
        }
        
        // 사라진 인형의 개수
        int cnt = 0;
        for (int i = 0; i < moves.length; i++) {
            // 해당 칸이 비어있을 땐 아무것도 하지 않는다.
            if (board_stacks[moves[i] - 1].empty()) {
                continue;
            }
            
            // 꺼낸 인형
            int doll = board_stacks[moves[i] - 1].pop();

            
            // 바구니가 비어있지 않고, peek 값이 꺼낸 인형과 같을 때 peek 인형 제거
            if (!baguni.empty() && baguni.peek() == doll) {
                baguni.pop();
                cnt += 2;
            } else {    // 아니면 바구니에 담는다.
                baguni.push(doll);
            }
        }

        return cnt;
    }
}
```

