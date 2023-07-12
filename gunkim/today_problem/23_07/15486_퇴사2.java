// dp 문제는 진짜... 사고 방식이 턱턱 막히게 되는 것 같다
import java.io.*;
import java.util.*;

public class Main {

  private int[] dp;
  private int n;
  private int[] t;
  private int[] p;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    t = new int[n + 2];
    p = new int[n + 2];
    for (int i = 1; i <= n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      t[i] = Integer.parseInt(st.nextToken());
      p[i] = Integer.parseInt(st.nextToken());
    }

    dp = new int[n + 2]; // n + 2까지 늘려 dp 값을 계산하는 것 까지는 잘했음
    int max = 0; // 탐색한 곳 까지 최대 수익 <- 이걸 생각 못했음
    for (int i = 1; i < n + 2; i++) {

      // 현재 시점까지의 최대 수익을 알아야 i + T[i]까지 일했을 때 P[i]를 더해서 최대 수익을 낼 수 있다.
      if (max < dp[i]) {
        max = dp[i];
      }

      // day날까지 일했을 때, max + P[i]와 이미 구해진 그 날의 수익 중에 최대 수익을 택하자!
      int day = i + t[i];
      if (day < n + 2) {
        dp[day] = Math.max(dp[day], max + p[i]);
      }
    }

    System.out.println(max);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}