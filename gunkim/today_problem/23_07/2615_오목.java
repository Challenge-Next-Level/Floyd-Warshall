import java.io.*;
import java.util.*;

public class Main {

  private int[][] board;
  private int answer;
  private int answerY;
  private int answerX;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    board = new int[19][19];
    for (int i = 0; i < 19; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < 19; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    answer = 0;
    for (int i = 0; i < 19; i++) {
      for (int j = 0; j < 19; j++) {
        if (answer != 0) {
          break;
        }
        if (board[i][j] != 0) { // 돌이 있는 곳에서 탐색 시작
          for (int k = 0; k < 4; k++) { // 4개의 방향에 대해 탐색
            int ny = i + dir[k][0];
            int nx = j + dir[k][1];
            if (ny >= 0 && ny < 19 && nx >= 0 && nx < 19 && board[i][j] == board[ny][nx]) { // 뻗어 나가는 곳에 같은 색의 돌이 있다면
              // 이전 방향에서 해당 색의 돌이 있다면 이미 탐색을 진행한 곳이니 굳이 탐색 x
              // 그리고 이 탐색을 막는 것은 6목을 5목으로 판단하는 것을 막을 수 있음
              int my = i - dir[k][0];
              int mx = j - dir[k][1];
              if (my >= 0 && my < 19 && mx >= 0 && mx < 19 && board[i][j] == board[my][mx]) {
                continue;
              }
              graphSearch(2, ny, nx, k); // 재귀로 탐색 시작
            }
          }
        }
      }
    }

    if (answer == 0) {
      System.out.println(0);
    } else {
      StringBuilder sb = new StringBuilder();
      sb.append(answer).append("\n");
      sb.append(answerY).append(" ").append(answerX);
      System.out.println(sb);
    }

  }

  int[][] dir = {{1, -1}, {1, 0}, {1, 1}, {0, 1}};

  public void graphSearch(int depth, int y, int x, int d) {
    if (depth >= 6) {
      return;
    }

    int ny = y + dir[d][0];
    int nx = x + dir[d][1];
    if (ny >= 0 && ny < 19 && nx >= 0 && nx < 19 && board[y][x] == board[ny][nx]) { // 다음 돌이 계속 이어진다면 탐색
      graphSearch(depth + 1, ny, nx, d);
    } else { // 끊긴다면
      if (depth == 5) { // 그곳이 5목이라면
        answer = board[y][x];
        if (d == 0) {
          answerY = y + 1;
          answerX = x + 1;
        } else {
          answerY = y - (dir[d][0] * 4) + 1;
          answerX = x - (dir[d][1] * 4) + 1;
        }
        return;
      }
    }
    return;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}