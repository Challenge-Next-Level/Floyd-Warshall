import java.io.*;
import java.util.*;

public class Main {

  private int count;
  private int maxSize;
  private boolean[][] visit;
  private int[][] board;
  private int n;
  private int m;

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

    count = 0;
    maxSize = 0;
    visit = new boolean[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (board[i][j] == 1 && !visit[i][j]) {
          bfs(i, j);
        }
      }
    }

    StringBuilder sb = new StringBuilder();
    sb.append(count).append("\n").append(maxSize);
    System.out.println(sb);
  }

  int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  public void bfs(int y, int x) {
    Queue<Coordinate> queue = new LinkedList<>();
    queue.offer(new Coordinate(y, x));
    visit[y][x] = true;
    int size = 0;
    while (!queue.isEmpty()) {
      Coordinate c = queue.poll();
      size++;
      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny >= 0 && ny < n && nx >= 0 && nx < m && !visit[ny][nx] && board[ny][nx] == 1) {
          queue.offer(new Coordinate(ny, nx));
          visit[ny][nx] = true;
        }
      }
    }
    maxSize = Math.max(maxSize, size);
    count++;
  }

  public static class Coordinate {
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