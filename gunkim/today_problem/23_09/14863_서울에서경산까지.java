// dp로 하는 건가 처음 생각했는데 시간을 기준으로 배열을 생성하면 OOME가 발생할 것 같아 그냥 greedy하게 풀었더니 시간초과가 발생
// 방문 지점과 시간을 관계로 dp 배열을 생성해 만들어야 했음
// 이때 갱신하는 값이 좀 어려워 유의해야함
import java.io.*;
import java.util.*;
public class Main {

  private int n;
  private int k;
  private int answer;
  private int[][] dp;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    dp = new int[n + 1][k + 1];
    int t1, m1, t2, m2;
    for (int i = 1; i <= n; i++) {
      st = new StringTokenizer(br.readLine());
      t1 = Integer.parseInt(st.nextToken());
      m1 = Integer.parseInt(st.nextToken());
      t2 = Integer.parseInt(st.nextToken());
      m2 = Integer.parseInt(st.nextToken());
      if (i == 1) {
        dp[i][t1] = m1;
        dp[i][t2] = Math.max(dp[i][t2], m2);
      } else {
        for (int j = 0; j <= k; j++) {
          if (dp[i - 1][j] == 0) // 이전 do 값에서 더해져야 하기 때문에
            continue;
          // dp 값을 구한다
          if (j + t1 <= k) { // 제한 시간 내 경우
            dp[i][j + t1] = Math.max(dp[i][j + t1], dp[i - 1][j] + m1);
          }
          if (j + t2 <= k) {
            dp[i][j + t2] = Math.max(dp[i][j + t2], dp[i - 1][j] + m2);
          }
        }
      }
    }
    for (int i = 0; i <= k; i++) {
      answer = Math.max(answer, dp[n][i]);
    }
    System.out.println(answer);

  }





  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}