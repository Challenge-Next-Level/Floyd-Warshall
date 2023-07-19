// 처음 구현시 visitVirus 부분을 ArrayList를 이용해 바이러스의 좌표를 저장하는 용도로 활용했다. 하지만 add, remove라는 과정 때문에 시간초과 발생
// 현재 코드처럼 간단히 방문했는지 체크 용도로 변경 후 이를 이용해 bfs에서 virus와 visitVirus를 통해 바이러스의 좌표를 알아내면 됐다.
import java.io.*;
import java.util.*;

public class Main {

  private ArrayList<Coordinate> virus;
  private int n;
  private int m;
  private int[][] board;
  private int answer;
  private int emptySpace;
  private boolean[] visitVirus;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    board = new int[n][n];
    virus = new ArrayList<>();
    emptySpace = 0;

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        int num = Integer.parseInt(st.nextToken());
        board[i][j] = num;
        if (num == 2) {
          virus.add(new Coordinate(i, j, 0));
        }
        if (num == 0) {
          emptySpace++;
        }
      }
    }
    emptySpace = emptySpace + virus.size();
    answer = Integer.MAX_VALUE;
    visitVirus = new boolean[virus.size()]; // 해당 지점에 바이러스를 둘 것인지 체크
    if (emptySpace - m == 0) { // 채워야 하는 공간 == 바이러스라면 0초만에 완료
      answer = 0;
    } else {
      // 조합으로 경우의 수 만들기
      combination(0, 0);
    }

    if (answer == Integer.MAX_VALUE) { // 모두 감염시키는 경우가 없다면
      System.out.println(-1);
    } else {
      System.out.println(answer);
    }
  }

  public void combination(int depth, int start) {
    if (depth == m) { // m개 만큼 선택했을 때
      // 바이러스 확산 탐색하기
      bfs();
      return;
    }
    for (int i = start; i < virus.size(); i++) {
      visitVirus[i] = true;
      combination(depth + 1, i + 1);
      visitVirus[i] = false;
    }
  }

  int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  public void bfs() {
    ArrayDeque<Coordinate> deque = new ArrayDeque<>();
    boolean[][] visit = new boolean[n][n];
    for (int i = 0; i < virus.size(); i++) { // virus와 visitVirus를 통해 바이러스가 분포된 좌표 추가하기
      if (visitVirus[i]) {
        Coordinate c = virus.get(i);
        visit[c.y][c.x] = true;
        deque.add(c);
      }
    }

    int virusSpace = 0;
    int maxCount = 0;
    while (!deque.isEmpty()) {
      Coordinate c = deque.poll();
      virusSpace++;
      if (c.count > maxCount) {
        maxCount = c.count;
      }
      if (maxCount > answer) { // 백트래킹
        break;
      }
      for (int i = 0; i < 4; i++) {
        int ny = c.y + dir[i][0];
        int nx = c.x + dir[i][1];
        if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visit[ny][nx] && board[ny][nx] != 1) {
          visit[ny][nx] = true;
          deque.add(new Coordinate(ny, nx, c.count + 1));
        }
      }
    }
    if (virusSpace == emptySpace && maxCount < answer) { // 모든 구역을 감염시켰을 때 답을 갱신
      answer = maxCount;
    }
  }
  public class Coordinate {
    private int y;
    private int x;
    private int count;

    public Coordinate(int y, int x, int count) {
      this.y = y;
      this.x = x;
      this.count = count;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}