// 시간 초과가 발생해서 답답했던 문제
// 빙산이었던 곳이 녹아서 '바다'가 되면 다른 빙산을 어떻게 쉽게 녹일 수 있는 걸까? 에 대한 고뇌
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;

  private int[][] board;
  private boolean[][] visit;
  private int cnt;
  private int result = 0;

  public class Coordinate {
    private int y;
    private int x;

    public Coordinate(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new int[n][m];

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }


    while (true) {
      // 대륙의 수 카운트
      cnt = countIsland();

      if (cnt >= 2) { // 2개 이상은 break
        break;
      } else if (cnt == 0) { // 대륙이 그냥 없는 경우
        result = 0;
        break;
      }

      bfs(); // 빙산을 녹이자
      result++;
    }

    System.out.println(result);

  }

  private int countIsland() {
    visit = new boolean[n][m];

    int count = 0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (!visit[i][j] && board[i][j] > 0) {
          dfs(i, j);
          count++;
        }
      }
    }

    return count;
  }

  private void dfs(int y, int x) {
    visit[y][x] = true;

    for (int i = 0; i < 4; i++) {
      int ny = y + dir[i][0];
      int nx = x + dir[i][1];

      if (!visit[ny][nx] && board[ny][nx] > 0) {
        dfs(ny, nx);
      }
    }
  }

  private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

  // 1. 빙산인 곳을 체크하기
  // 2. 빙산인 곳을 녹이기
  private void bfs() {
    Deque<Coordinate> dq = new ArrayDeque<>();
    visit = new boolean[n][m]; // 빙산이었던 곳을 체크하는 기능

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (board[i][j] > 0) {
          dq.add(new Coordinate(i, j));
          visit[i][j] = true;
        }
      }
    }

    while (!dq.isEmpty()) {
      Coordinate c = dq.pollFirst();

      int sea = 0;

      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];

        // 빙산이 아닌 순수 바다였던 자리라면
        if (!visit[ny][nx] && board[ny][nx] == 0) {
          sea++;
        }
      }

      board[c.y][c.x] = Math.max(0, board[c.y][c.x] - sea);
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}