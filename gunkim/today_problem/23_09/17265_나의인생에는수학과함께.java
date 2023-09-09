// 1 try 1 solve 한 문제
// dfs를 구현하는데 연산자와 피연산자를 구분하여 진행하는 것이 핵심이었음
import java.io.*;
import java.util.*;
public class Main {

  private static int[][] dir = {{1, 0}, {0, 1}};
  private static char[][] board;
  private static int maxNum = Integer.MIN_VALUE;
  private static int minNum = Integer.MAX_VALUE;
  private static int n;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    n = Integer.parseInt(br.readLine());
    board = new char[n][n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        board[i][j] = st.nextToken().charAt(0);
      }
    }

    dfs(0, 0, board[0][0] - '0', ' ');

    StringBuilder sb = new StringBuilder();
    sb.append(maxNum).append(" ").append(minNum);
    System.out.println(sb);
  }

  private static void dfs(int y, int x, int result, char op) {
    if (y == n - 1 && x == n - 1) {
      minNum = Math.min(minNum, result);
      maxNum = Math.max(maxNum, result);
      return;
    }

    for (int i = 0; i < 2; i++) {
      int ny = y + dir[i][0];
      int nx = x + dir[i][1];
      if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
      if (op == ' ') {
        dfs(ny, nx, result, board[ny][nx]);
      } else {
        int calculatedNum = calculate(result, board[ny][nx] - '0', op);
        dfs(ny, nx, calculatedNum, ' ');
      }
    }
  }

  private static int calculate(int a, int b, char op) {
    if (op == '+') {
      return a + b;
    } else if (op == '-') {
      return a - b;
    }
    return a * b;
  }

  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}