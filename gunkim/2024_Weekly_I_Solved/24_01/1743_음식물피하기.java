// 쉬운 bfs 문제
import java.io.*;
import java.util.*;

public class Main {


  private boolean[][] visit;

  private int n;
  private int m;
  private int[][] board;
  private int k;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][m];
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      int y = Integer.parseInt(st.nextToken());
      int x = Integer.parseInt(st.nextToken());
      board[y - 1][x - 1] = 1;
    }

    int answer = 0;
    visit = new boolean[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        // 쓰레기가 있는 곳에서 bfs 탐색
        if (board[i][j] == 1 && !visit[i][j]) {
          int size = bfs(i, j);
          answer = Math.max(answer, size); // 사이즈 갱신
        }
      }
    }

    System.out.println(answer);
  }

  private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  public int bfs(int y, int x) {
    Deque<Coordinate> dq = new ArrayDeque<>();
    dq.add(new Coordinate(y, x));
    int size = 0;

    while (!dq.isEmpty()) {
      Coordinate c = dq.pollFirst();
      if (visit[c.y][c.x]) continue;
      visit[c.y][c.x] = true;
      size += 1;

      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny < 0 || ny >= n || nx < 0 || nx >= m || visit[ny][nx] || board[ny][nx] != 1) continue;

        dq.add(new Coordinate(ny, nx));
      }
    }

    return size;
  }

  public class Coordinate {
    private int y;
    private int x;

    public Coordinate(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}