# [SWEA] 1288. 새로운 불면증 치료법 [D2] - JAVA

## 📚 문제 : [새로운 불면증 치료법](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN)

## 📖 풀이

0부터 9까지의 boolean 배열을 만들어 방문표시를 한다.

0부터 9까지의 모든 수를 확인했는지 체크하고 다 True이면 그 때의 횟수를 출력한다.

입력으로 주어진 수의 각각의 숫자를 확인하기 위해 java에서는 **charAt()**를 활용한다. 그리고 각각을 정수로 바꿔주기 위해 **Character.*getNumericValue*()**을 사용한다.

> 📌 **헷갈리지 말 것!**
>
> **String**인 경우는 **Interger.paseInt()**를 사용하지만
>
> **Character**는 **Character.*getNumericValue*()**를 사용!

## 📒 코드

```java
import java.util.Scanner;

// 1288. 새로운 불면증 치료법
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int tc = 1; tc <= t; tc++) {
			int cnt = 0;
			int ans = 0;
			boolean[] visited = new boolean[10];
			int n = sc.nextInt();
			int num = 0;
			
			while(cnt < 10) {
				ans += 1;
				num += n;
				String string_num = Integer.toString(num);
				for (int i = 0; i < string_num.length(); i++) {
					int number = Character.getNumericValue(string_num.charAt(i));
					if (!visited[number]) {
						visited[number] = true;
						cnt += 1;
					}
				}
			}
			System.out.println("#" + tc + " " + num);		
		}
		sc.close();
	}
}
```