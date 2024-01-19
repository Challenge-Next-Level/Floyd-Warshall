// 평범한 bfs
import java.io.*;
import java.util.*;

public class Main {


  private boolean[][] visit;

  private int n;
  private int m;
  private char[][] board;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new char[n][m];
    Coordinate start = null;
    for (int i = 0; i < n; i++) {
      String str = br.readLine();
      for (int j = 0; j < m; j++) {
        board[i][j] = str.charAt(j);
        if (str.charAt(j) == 'I')
          start = new Coordinate(i, j);
      }
    }

    visit = new boolean[n][m];
    int answer = bfs(start.y, start.x);

    if (answer == 0)
      System.out.println("TT");
    else
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

      if (board[c.y][c.x] == 'P') size += 1;

      for (int i = 0; i < 4; i++) { // 이곳이 본격적인 그래프 탐색
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny < 0 || ny >= n || nx < 0 || nx >= m || visit[ny][nx] || board[ny][nx] == 'X') continue;

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