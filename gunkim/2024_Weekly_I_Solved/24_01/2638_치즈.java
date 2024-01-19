// 평범한 덱 문제. 근데 조금 귀찮은...
import java.io.*;
import java.util.*;

public class Main {

  private int[][] check;
  private boolean[][] visit;
  private boolean isCheese;
  private int n;
  private int m;
  private int[][] board;

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

    int time = 0;


    while (true) { // 치즈가 모두 녹을 때 까지 반복
      isCheese = false; // 이번 시간에 치즈가 녹았는지 확인
      check = new int[n][m];
      visit = new boolean[n][m];

      bfs(); // 외부 공기를 탐색하면서 공기와 닿는 치즈를 체크한다

      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (check[i][j] >= 2){ // 2개의 면과 접촉한 치즈는 삭제
            board[i][j] = 0;
            isCheese = true;
          }
        }
      }

      if (!isCheese) break; // 녹은 치즈가 없다면 반복문 종료
      else time += 1; // 있다면 시간 증가
    }

    System.out.println(time);
  }

  private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  public void bfs() {
    Deque<Coordinate> dq = new ArrayDeque<>();
    dq.add(new Coordinate(0, 0));

    while (!dq.isEmpty()) {
      Coordinate c = dq.pollFirst();
      if (visit[c.y][c.x]) continue;
      visit[c.y][c.x] = true;

      // 상하좌우에 치즈가 있는지 살펴보자
      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
        if (board[ny][nx] == 1) check[ny][nx] += 1; // 치즈가 있다면
      }

      for (int i = 0; i < 4; i++) { // 이곳이 본격적인 그래프 탐색
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny < 0 || ny >= n || nx < 0 || nx >= m || visit[ny][nx] || board[ny][nx] != 0) continue;

        dq.add(new Coordinate(ny, nx));
      }

    }
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