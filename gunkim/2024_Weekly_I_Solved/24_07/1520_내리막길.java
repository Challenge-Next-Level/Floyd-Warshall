import java.io.*;
import java.util.*;

public class Main {

  static int M, N;
  static int[][] arr, dp;
  static int[] dy = { -1, 0, 1, 0 };
  static int[] dx = { 0, 1, 0, -1 };


  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    M = Integer.parseInt(st.nextToken());
    N = Integer.parseInt(st.nextToken());

    arr = new int[M + 1][N + 1];
    for (int i = 1; i <= M; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 1; j <= N; j++) {
        arr[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    dp = new int[M + 1][N + 1]; // (x, y)에서 도착점으로 가는 경로의 개수
    for (int i = 0; i < M + 1; i++) {
      Arrays.fill(dp[i], -1);
    }

    System.out.println(DFS(1, 1));
  }


  public static int DFS(int y, int x) {
    if (y == M && x == N) {
      return 1;
    }

    if (dp[y][x] != -1) {
      return dp[y][x];
    }

    dp[y][x] = 0; // 현재 위치에서 끝점까지 도달하는 경로의 개수를 0으로 초기화.
    for (int i = 0; i < 4; i++) { // 동서남북 탐색
      int ny = y + dy[i];
      int nx = x + dx[i];

      if (ny < 1 || nx < 1 || ny > M || nx > N) {
        continue;
      }

      // arr[y][x]보다 arr[ny][nx]가 높이가 더 낮다면
      // arr[ny][nx]에서 끝점까지 도달하는 경로의 개수를 더한다.
      if (arr[y][x] > arr[ny][nx]) {
        dp[y][x] += DFS(ny, nx);
      }
    }

    return dp[y][x];
  }

}