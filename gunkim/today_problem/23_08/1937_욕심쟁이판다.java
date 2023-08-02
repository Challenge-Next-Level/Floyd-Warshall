// (나의 dp 값)과 (이동하는 곳의 dp값 + 1)을 서로 비교하는 것이 핵심인 것 같음
import java.io.*;
import java.util.*;

public class Main {

  static int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  static int[][] dp;
  static int n;
  static int[][] board;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    board = new int[n][n];
    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    dp = new int[n][n];
    int answer = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        answer = Math.max(answer, dfs(i, j));
      }
    }
    System.out.println(answer);

  }

  // 최장거리를 구해야 하기 때문에 dfs 탐색
  static int dfs(int y, int x) {
    if (dp[y][x] != 0) {
      return dp[y][x];
    }

    dp[y][x] = 1;

    for (int i = 0; i < 4; i++) {
      int ny = y + dir[i][0];
      int nx = x + dir[i][1];
      if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
      // dp 갱신할 때 : (나의 dp 값)과 (이동하는 곳의 dp값 + 1)을 서로 비교하면 된다.
      if (board[y][x] < board[ny][nx]) {
        dp[y][x] = Math.max(dp[y][x], dfs(ny, nx) + 1);
      }
    }
    return dp[y][x];
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}