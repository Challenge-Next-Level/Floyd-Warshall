// 정답이 음수일 수도 있기 때문에 answer의 초깃값 설정이 중요하다
// 최대 재귀 탐색이 10 * 10 = 100 제한이라 dfs로 풀었지만 더 좋은 해결법이 분명 있을 것 같다
import java.io.*;
import java.util.*;

public class Main {

  private int[][] board;
  private int n;
  private int m;
  private int k;
  private boolean[][] visit;
  private int answer;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n + 1][m + 1];
    for (int i = 1; i <= n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 1; j <= m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    answer = Integer.MIN_VALUE;
    visit = new boolean[n + 1][m + 1];
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        visit[i][j] = true;
        dfs(i, j, 1, board[i][j]);
        visit[i][j] = false;
      }
    }

    System.out.println(answer);

  }

  public void dfs(int y, int x, int count, int result) {
    if (count == k) {
      answer = Math.max(answer, result);
      return;
    }

    for (int i = y; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (i == y && j <= x) continue;
        if (visit[i - 1][j] || visit[i][j - 1]) continue;
        visit[i][j] = true;
        dfs(i, j, count + 1, result + board[i][j]);
        visit[i][j] = false;
      }
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}