// dp를 갱신하는 방법이 떠올리기 어려웠음
// K값이 최소값으로 계산해야 하는데 max로 가져오는 것이 처음에 이해하기 어려웠다
// 하지만 이동하는 중간 발생하는 power의 최대값을 가져오는 것이 맞기 때문에 결국 이해했다
import java.io.*;
import java.util.*;

public class Main {

  private long[] a;
  private long[] dp;
  private int n;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    a = new long[n + 1];
    dp = new long[n + 1];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; i++) {
      a[i] = Long.parseLong(st.nextToken());
      dp[i] = -1;
    }

    System.out.println(findMinPower(1));
  }

  public long findMinPower(int start) {
    if (start == n) return 0; // 도착지점의 비용은 0이다.
    if (dp[start] != -1)
      return dp[start];

    dp[start] = Long.MAX_VALUE;
    for (int i = start + 1; i <= n; i++) {
      // dp값은 결국 최소 K 값을 갱신해나간다.
      // 출발지에서 도착지 까지 소모하는 파워 비교 => 출발지에서 중간 목적지까지 파워 vs 도달한 중간 목적지에서의 dp
      // 비교해서 값을 가져올 때는 최댓값을 가져와야함
      dp[start] = Math.min(dp[start], Math.max(findMinPower(i), (i - start) * (1 + Math.abs(a[start] - a[i]))));
    }

    return dp[start];
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}