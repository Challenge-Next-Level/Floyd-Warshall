// 평범한 구현 문제
// 대신 처음에 이분 탐색이라 착각했고 문제 분류에서 'brute force'를 보고 고민했었음
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private int b;

  private int[][] board;


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    b = Integer.parseInt(st.nextToken());

    board = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int minTime = Integer.MAX_VALUE;
    int maxHeight = 0;

    // 높이 0 ~ 256까지 모든 경우에 대해 탐색
    for (int i = 0; i < 257; i++) {
      int needs = 0; // 필요한 블럭양
      int get = 0; // 채굴한 블럭양
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < m; k++) {
          if (board[j][k] > i) get += board[j][k] - i;
          else if(board[j][k] < i) needs += i - board[j][k];
        }
      }

      // 갖고 있는 블럭이 필요한 블럭보다 적다면
      if (needs > b + get) continue;

      int time = get * 2 + needs;

      if (time <= minTime) {
        minTime = time;
        maxHeight = Math.max(maxHeight, i);
      }
    }

    System.out.println(minTime + " " + maxHeight);

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}