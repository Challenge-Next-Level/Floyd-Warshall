import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    while (true) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      if (n == 0 && m == 0) {
        break;
      }

      int[][] board = new int[n + 1][m + 1];
      for (int i = 1; i <= n; i++) {
        st = new StringTokenizer(br.readLine());
        for (int j = 1; j <= m; j++) {
          board[i][j] = Integer.parseInt(st.nextToken());
        }
      }

      int result = 0;
      int[][] dp = new int[n + 1][m + 1];
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
          if (board[i][j] == 0) {
            dp[i][j] = 0;
          } else {
            dp[i][j] = Math.min((Math.min(dp[i - 1][j], dp[i][j - 1])), dp[i - 1][j - 1]) + 1;
          }
          if (dp[i][j] > result) {
            result = dp[i][j];
          }
        }
      }
      sb.append(result).append('\n');
    }
    System.out.println(sb);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}