//내 방식대로 투 포인터를 이용해 풀었을 때는 역시나 '틀렸습니다'를 보았다.
//dp로 푸는게 맞겠지.. 생각은 했지만 아래와 같이 2중 배열로 이용해 풀어낸다는 것을 상상도 못했다.
import java.io.*;
import java.util.*;

public class Main {

  private int[][] dp;
  private int[] v;

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    v = new int[n + 1];
    for (int i = 1; i < n + 1; i++) {
      v[i] = Integer.parseInt(br.readLine());
    }

    dp = new int[n + 1][n + 1];
    int answer = topDown(1, n, 1);
    System.out.println(answer);
  }

  public int topDown(int start, int end, int count) {
    if (start > end) return 0;
    if (dp[start][end] != 0) return dp[start][end];

    int first = topDown(start + 1, end, count + 1) + v[start] * count;
    int last = topDown(start, end - 1, count + 1) + v[end] * count;

    dp[start][end] = Math.max(first, last);
    return dp[start][end];
  }


  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}