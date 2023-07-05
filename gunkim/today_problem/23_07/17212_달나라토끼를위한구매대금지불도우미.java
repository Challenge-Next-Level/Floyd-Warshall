import java.io.*;
import java.util.*;

public class Main {

  private int count;
  private int n;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    int[] dp = new int[n + 8]; // dp[7]까지 설정하기 위해 배열 크기 조정
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 2;
    dp[5] = 1;
    dp[6] = 2;
    dp[7] = 1;

    if (n <= 7) {
      System.out.println(dp[n]);
    } else {
      int num = 8;
      while (num <= n) {
        int a = Math.min(dp[1] + dp[num - 1], dp[2] + dp[num - 2]);
        int b = Math.min(dp[5] + dp[num - 5], dp[7] + dp[num - 7]);
        dp[num] = Math.min(a, b);
        num++;
      }
      System.out.println(dp[n]);
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}