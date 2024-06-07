// 값이 작은 동전 부터 차례대로 dp 를 갱신하는 문제
// 배낭 문제(?)의 정석 문제
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int q = 0; q < t; q++) {
      int n = Integer.parseInt(br.readLine());
      StringTokenizer st = new StringTokenizer(br.readLine());
      int[] coins = new int[n+1];
      for (int i = 1; i <= n; i++) {
        coins[i] = Integer.parseInt(st.nextToken());
      }
      int m = Integer.parseInt(br.readLine());

      int[] dp = new int[m+1];
      for (int i = 1; i <= n; i++) { // 작은 값의 동전부터 dp 갱신하기
        for (int j = 1; j <=m; j++) { // 목표치까지 모든 구간에 대해 dp 계산하기
          if (j - coins[i] > 0) {
            dp[j] = dp[j] + dp[j-coins[i]];
          } else if (j - coins[i] == 0) {
            dp[j]++;
          }
        }
      }
      sb.append(dp[m] + "\n");
    }
    System.out.print(sb);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}