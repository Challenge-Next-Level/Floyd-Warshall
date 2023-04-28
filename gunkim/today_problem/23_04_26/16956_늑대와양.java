import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    char[][] board = new char[n][m];
    List<Location> wolf = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      String row = br.readLine();
      for (int j = 0; j < m; j++) {
        board[i][j] = row.charAt(j);
        if (board[i][j] == 'W') wolf.add(new Location(i, j));
      }
    }

    boolean possible = true;
    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    boolean[][] visit = new boolean[n][m];
    for (Location loc : wolf) {
      if (!possible) break;
      int y = loc.y;
      int x = loc.x;
      for (int i = 0; i < 4; i++) {
        int ny = y + dir[i][0];
        int nx = x + dir[i][1];
        if (ny >= 0 && ny < n && nx >= 0 && nx < m && !visit[ny][nx]) {
          if (board[ny][nx] == 'S') {
            possible = false;
            break;
          } else if (board[ny][nx] == '.') {
            board[ny][nx] = 'D';
            visit[ny][nx] = true;
          }
        }
      }
    }

    if (!possible) System.out.println(0);
    else {
      StringBuilder sb = new StringBuilder();
      sb.append("1\n");
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          sb.append(board[i][j]);
        }
        sb.append('\n');
      }
      System.out.println(sb);
    }

  }

  class Location{
    private int y;
    private int x;

    public Location(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}