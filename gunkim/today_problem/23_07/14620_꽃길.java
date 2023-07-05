import java.io.*;
import java.util.*;

public class Main {

  private boolean[][] visit;
  private int answer;
  private int n;
  private int[][] board;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    board = new int[n][n];

    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    visit = new boolean[n][n];
    answer = Integer.MAX_VALUE;
    // 재귀를 이용한 완전 탐색 진행
    graphSearch(0, 1, 0, 0);

    System.out.println(answer);
  }

  int[][] dir = {{0, 0}, {0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // 꽃이 피는 5방향 좌표
  public void graphSearch(int depth, int y, int x, int total) {
    if (total >= answer) { // 총 비용에 대한 백트래킹
      return;
    }
    if (depth >= 3) { // 모든 꽃을 심었다면 최저 비용 갱신
      answer = total;
      return;
    }
    for (int i = y; i < n - 1; i++) { // 꽃을 심을 자리 탐색
      for (int j = 1; j < n - 1; j++) {
        if (i == y && j <= x) {
          continue;
        }
        boolean flag = true;
        int cost = 0;
        for (int k = 0; k < 5; k++) { // 꽃 심는 자리가 겹치지 않는지 확인
          int ny = i + dir[k][0];
          int nx = j + dir[k][1];
          if (visit[ny][nx]) {
            flag = false;
            break;
          }
          cost += board[ny][nx];
        }
        if (flag) {
          for (int k = 0; k < 5; k++) { // visit 체크
            int ny = i + dir[k][0];
            int nx = j + dir[k][1];
            visit[ny][nx] = true;
          }
          graphSearch(depth + 1, i, j, total + cost); // 다음 꽃을 심는다
          for (int k = 0; k < 5; k++) { // visit 체크 해제
            int ny = i + dir[k][0];
            int nx = j + dir[k][1];
            visit[ny][nx] = false;
          }
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}