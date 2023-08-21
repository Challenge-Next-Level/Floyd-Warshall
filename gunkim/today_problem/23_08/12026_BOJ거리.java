// 처음 시도때 '시간초과'가 발생했다. 백트래킹이나 다른 조건을 추가해야 할 것 같은 느낌이 들었다. 로직 자체는 괜찮았기 때문이다.
import java.io.*;
import java.util.*;
public class Main {

  private char[] boj;
  private String bridge;
  private int[] dp;
  private int n;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    bridge = br.readLine();

    boj = new char[] {'B', 'O', 'J'};
    dp = new int[n];
    for (int i = 0; i < n; i++) {
      dp[i] = -1;
    }

    dp[0] = 0;
    dfs(0, 0);

    System.out.println(dp[n - 1]);

  }

  public void dfs(int idx, int bojIdx) {
    if (idx == n - 1) return;

    int nextBojIdx = (bojIdx + 1) % 3;
    int nextBoj = boj[nextBojIdx];

    for (int i = idx + 1; i < n; i++) {
      if (bridge.charAt(i) == nextBoj) {
        // 백트래킹(?) : 이미 해당 돌을 적은 비용을 통해 지나간 경우가 있다면 현재 진행하려는 경우는 최적의 경우가 될 수 없음
        if (dp[i] != -1 && dp[i] <= dp[idx] + (i - idx) * (i - idx)) continue;
        dp[i] = dp[idx] + (i - idx) * (i - idx);
        dfs(i, nextBojIdx);
      }
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}