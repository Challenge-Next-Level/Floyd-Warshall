import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int[][] board = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int[][] dir = {{1, -1}, {1, 0}, {1, 1}};
    Stack<Info> stack = new Stack<>();
    int answer = Integer.MAX_VALUE;
    for (int i = 0; i < m; i++) {
      stack.push(new Info(0, i, board[0][i], -1));
    }
    while (!stack.isEmpty()) {
      Info info = stack.pop();
      if (info.y >= n - 1) {
        answer = Math.min(answer, info.cost);
        continue;
      }
      for (int i = 0; i < 3; i++) {
        if (info.beforeDir != i) {
          int ny = info.y + dir[i][0];
          int nx = info.x + dir[i][1];
          if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
            stack.push(new Info(ny, nx, info.cost + board[ny][nx], i));
          }
        }
      }
    }

    System.out.println(answer);
  }

  public class Info {
    private int y;
    private int x;
    private int cost;
    private int beforeDir;
    public Info(int y, int x, int cost, int beforeDir) {
      this.y = y;
      this.x = x;
      this.cost = cost;
      this.beforeDir = beforeDir;
    }
  }


  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}