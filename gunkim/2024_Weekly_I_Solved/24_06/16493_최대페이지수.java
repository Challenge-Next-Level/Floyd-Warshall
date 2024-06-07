// 역시나 전형적인 배낭 문제
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    // 페이지 수, 날짜
    int[][] dp = new int[M + 1][N + 1];

    for (int i = 1; i <= M; i++) {
      st = new StringTokenizer(br.readLine());
      int day = Integer.parseInt(st.nextToken());
      int pages = Integer.parseInt(st.nextToken());

      for (int j = 1; j <= N; j++) {
        dp[i][j] = dp[i-1][j];
        if ((j - day) >= 0) {
          // (같은 날짜로 전에 계산한 dp 값) vs (현재 dp 값에서 소요되는 일 수를 뺀 값 + 현재 읽은 페이지 수)
          dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j - day] + pages);
        }
      }
    }
    System.out.print(dp[M][N]);


  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}