// 일반 bfs
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private int k;
  private int[][] board;
  private int count = 0;
  private List<Integer> list = new ArrayList<>();

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    m = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    // board 초기화
    board = new int[m + 1][n + 1];
    for (int i = 0; i < m + 1; i++) {
      for (int j = 0; j < n + 1; j++) {

        if (i == 0 || j == 0) board[i][j] = 1;

      }
    }
    // 직사각형 그리기
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      int x1 = Integer.parseInt(st.nextToken()) + 1;
      int y1 = Integer.parseInt(st.nextToken()) + 1;
      int x2 = Integer.parseInt(st.nextToken());
      int y2 = Integer.parseInt(st.nextToken());

      for (int j = y1; j <= y2; j++) {
        for (int l = x1; l <= x2; l++) {
          board[j][l] = 1;
        }
      }
    }

    // 색칠되지 않은 부분에서 bfs 탐색
    for (int i = 1; i < m + 1; i++) {
      for (int j = 1; j < n + 1; j++) {
        if (board[i][j] == 0) {
          bfs(i, j);
        }
      }
    }

    // 결과 출력
    System.out.println(count);
    Collections.sort(list);
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < list.size(); i++) {
      sb.append(list.get(i)).append(" ");
    }
    System.out.println(sb);

  }

  private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

  private void bfs(int y, int x) {
    board[y][x] = 1;
    int size = 1;
    // bfs를 위해 deque 사용
    Deque<Coordinate> dq = new ArrayDeque<>();
    dq.add(new Coordinate(y, x));

    while (!dq.isEmpty()) {
      Coordinate coordinate = dq.pollFirst();
      for (int i = 0; i < 4; i++) {
        int ny = coordinate.y + dir[i][0];
        int nx = coordinate.x + dir[i][1];
        if (ny <= 0 || ny > m || nx <= 0 || nx > n || board[ny][nx] == 1) continue;

        size++;
        board[ny][nx] = 1;
        dq.add(new Coordinate(ny, nx));
      }
    }

    list.add(size);
    count++;
    return;
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