// 일반적인 BFS 문제
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private char[][] board;
  private int blue;
  private int white;
  private boolean[][] visit;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new char[m][n];
    for (int i = 0; i < m; i++) {
      String input = br.readLine();
      for (int j = 0; j < n; j++) {
        board[i][j] = input.charAt(j);
      }
    }

    visit = new boolean[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (!visit[i][j]) {
          bfs(i, j);
        }
      }
    }

    StringBuilder sb = new StringBuilder();
    sb.append(white).append(" ").append(blue);
    System.out.println(sb);
  }

  private class Coordinate {
    private int y;
    private int x;

    public Coordinate(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  private void bfs(int y, int x) {
    Deque<Coordinate> dq = new ArrayDeque<>();
    dq.add(new Coordinate(y, x));
    visit[y][x] = true;
    int size = 1;

    while (!dq.isEmpty()) {
      Coordinate c = dq.pollFirst();

      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];

        if (ny < 0 || ny >= m || nx < 0 || nx >= n || visit[ny][nx]) continue;
        if (board[y][x] != board[ny][nx]) continue;

        visit[ny][nx] = true;
        dq.add(new Coordinate(ny, nx));
        size++;
      }
    }

    if (board[y][x] == 'W') white += size * size;
    else blue += size * size;
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}