# [SWEA] 10726. 이진수 표현 [D3] - Java

## 📚 문제 : [이진수 표현](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS)

## 📒 풀이

과거 python으로 풀었던 문제이다. 그 때는 그냥 풀었지만 이번엔 **비트마스킹**을 통해 풀어보았다.

### 비트 확인 : m & (1 << i)

1 << i는 시프트 연산자로 i만큼 이동시킨 것이다.

&연산자는 두 수의 같은 비트끼리 비교해 둘 다 1인 경우만 1을 만들고 나머진 0을 만든다.

즉 m * (1 << i)는 숫자 m의 i번째 비트가 1인 경우 그 비트를 1로 만들고 아니면 0이다.

따라서 그 결과가 0보다 크면 확인하고 싶은 비트가 1인 것으로,  0이면 비트가 0으로 판단했다.

하나라도 0이면 OFF를 출력하고 다 1이면 ON을 출력한다.

## 📒 코드

```java
import java.util.Scanner;

// 10726. 이진수 표현
public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			String result = "ON";
			
			for (int i = 0; i < n; i++) {
				if (!((m & (1 << i)) > 0)) {
					result = "OFF";
					break;
				}
			}
			System.out.println("#" + tc + " " + result);
			
		}
		sc.close();
	}

}
```

