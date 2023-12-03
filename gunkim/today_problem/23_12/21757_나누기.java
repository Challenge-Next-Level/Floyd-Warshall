
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n + 1];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    long[] sum = new long[n + 1];
    for (int i = 1; i <= n; i++) {
      sum[i] = sum[i - 1] + arr[i];
    }

    long target = sum[n] / 4;
    if (target * 4 != sum[n]) {
      System.out.println(0);
      return;
    }

    long[][] dp = new long[n + 1][4];
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
      dp[i][0] = 1;
      for (int j = 1; j < 4; j++) {
        dp[i][j] = dp[i - 1][j];
        if (target * j == sum[i])
          dp[i][j] += dp[i - 1][j - 1];
      }
    }

    System.out.println(dp[n - 1][3]);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}