# [SWEA] 3316. 동아리실 관리하기 [D4] - java

## 📚 문제 : [동아리실 관리하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnFuhqxE8DFAWr)

## 📖 탑다운 DP 풀이 - 메모리 초과

생각나는 대로 일단 재귀로 풀이했다. 재귀 깊이가 너무 깊어 스택 메모리 초과에 걸려 후에 반복문으로 바꾸었다. 

### JAVA라 까다로웠던 점..

Python으로만 풀다가 Java로 풀이하려니, 시간이 오래 걸렸다.

java로 알고리즘을 풀며 까다로운 부분은 전역변수였다.

먼저 출력할 main 함수가 static이라 전역으로 사용할 변수들을 static으로 선언해주어야 한다. 또한 함수들도 static으로 선언하지 않으면 main 함수에서 불러올 수가 없다. 따라서 함수들도 static으로 선언해서 사용해야 한다!

그리고 dp를 0이 아닌 -1로 초기화하려고 했는데 그러기 위해서 **Arrays.fill()** 함수를 사용해서 -1로 초기화 해주었다.

### DP 사용법

dp를 2차원으로 선언해 A와 D가 참여할 경우의 수가 총 2^4이니 16이다. 따라서 N * 16의 배열을 선언해주었다.

N이 10000이니 16 * 10000이면 시간 안에 충분히 돌아갈 수 있다.



### 비트마스킹 사용

ABCD가 포함되는지는 각 비트로 나타내었다.

A는 첫 번째 비트 ... D는 네 번째 비트로 담아주면 된다. (DCBA 라면 각각 4321비트이다.)

A와 C가 있는 건 0101이다.

D만 있으면 1000이다.

- ((member & (1 << managers.charAt(cur) - 'A')) == 0)

  특정 멤버가 있는지 & 연산자로 확인한다. 0이면 없다는 것이니 이 때 continue로 넘겨준다.



### 첫째 날에 A가 열쇠 가지고 있으니 조심!

A가 열쇠 가지고 있는지 모르고 한참을 헤맸다.. ㅠ



## 📒 재귀 코드 - 메모리 초과

```java
import java.util.Scanner;

public class Solution {
	// 재귀 방법 : 런타임 에러
 	static String managers;
	static int[][] dp;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			managers = sc.next();
			// dp 초기화
			dp = new int[managers.length()][16];
			for (int i = 0; i < dp.length; i++) {
				Arrays.fill(dp[i], -1);
			}
			// A가 열쇠를 가지고 있으니 시작은 1
			System.out.println("#" + tc + " " + recur(0, 1));
		}
		sc.close();
	}
	
	
	static int recur(int cur, int prv_member) {
		if (cur == managers.length()) {
			return 1;
		}
		// 과거에 연산한 값인 경우
		if (dp[cur][prv_member] != -1) {
			return dp[cur][prv_member];
		}
		
		int ans = 0;
		
		for (int member = 1; member < 16; member++) {
			// 책임자가 포함됐는지 확인
			if ((member & (1 << managers.charAt(cur) - 'A')) == 0) {
				continue;	// 포함 안됐으면 pass
			}
			// 이전의 멤버와 이번 멤버 중 겹치는 사람 있는지 확인
			if ((member & prv_member) == 0) {
				continue;	// 겹치는 멤버가 없다면 pass
			}

			ans += recur(cur + 1, member);
			ans %= 1000000007;
		}
		dp[cur][prv_member] = ans;
		return ans;
	}
}
```

## 📖 반복문 풀이

재귀를 반복문으로 바꿀 때 형태가 거의 비슷하다. 재귀가 도는 부분을 for문 하나만 더해주면 된다.

초기화 부분만 신경써서 바꿔준다.

뒤에부터 넣어주는 탑다운 방식이어서 앞부터 채우는 방법으로 바꾸었다.



## 📒 반복문 코드

```java
import java.util.Scanner;

// 3316. 동아리실 관리하기
public class Solution {
	static String managers;
	static int[][] dp;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			managers = sc.next();
			// dp 초기화
			dp = new int[managers.length() + 1][16];	// 처음엔 0으로 초기화	
			// A가 열쇠를 가지고 있으니 시작은 1
			System.out.println("#" + tc + " " + solution());
		}
		sc.close();
	}
	
	static int solution() {
		// 1일차 값 넣어주기
		for (int i = 1; i < 16; i++) {
			if ((i & 1) == 0) {		// A가 처음에 열쇠를 가지고 있으니 A만 1을 넣어준다.
				continue;
			}
			if ((i & (1 << managers.charAt(0) - 'A')) == 0) {
				continue;
			}
			dp[0][i] = 1;
		}
		
		for (int i = 1; i < managers.length(); i++) {
			for (int j = 1; j < 16; j++) {
				for (int k = 1; k < 16; k++) {
					// 매니저가 포함되는 지 확인
					if ((j & (1 << managers.charAt(i) - 'A')) == 0) {
						continue;
					}
					// 이전 조합과 겹치는 것이 없는 경우
					if ((j & k) == 0) {
						continue;
					}
					dp[i][j] += dp[i - 1][k];
					dp[i][j] %= 1000000007;
				}
			}
		}
		
		// dp 마지막 날의 값을 다 더해서 출력
		int result = 0;
		for (int i = 1; i < 16; i++) {			
			result += dp[managers.length() - 1][i];
			result %= 1000000007;
		}
		
		return result;
	}
}
```

