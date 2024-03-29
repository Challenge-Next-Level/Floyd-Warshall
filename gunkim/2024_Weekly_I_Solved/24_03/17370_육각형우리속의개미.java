// https://howtolivelikehuman.tistory.com/249#recentEntries
// 육각형의 이동 경로를 좌표로 해석하면 좋았을 문제
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  //50,50에서 시작
  private boolean[][] board = new boolean[51][51];

  // 남 / 남서 / 남동 / 북 / 북서 / 북동
  private int[] moveX = {0,-1,1,0,-1,1};
  private int[] moveY = {1,1,1,-1,-1,-1};

  // 어느 방향으로 이동한 후 그 다음 이동 가능한 경로
  // ex) 0번째 방향 이동을 했다 (=남쪽 이동을 했다)
  // 그러면 남서 or 남동 이동 밖에 못한다 (= 1번째 or 2번째 방향 이동 밖에 못한다)
  private int[][] availableMove = {{2,1},{0,4},{5,0},{4,5},{1,3},{3,2}};
  private int answer = 0;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());

    // 시작 지점
    board[25][25] = true;
    // pastMove = 3 : 북쪽이동으로 시작했기 때문
    // x = 25, y = 24 : 시작 지점에서 북쪽 이동했기 때문
    seeking(0,3,25,24);
    System.out.println(answer);

  }

  private void seeking(int count, int pastMove, int x, int y){
    // 방문했던 곳이라면
    if(board[y][x]){
      if(count == n){
        answer++;
      }
      return;
    }

    // 방문했던 지점에 도착도 못했는데 n번 회전 했다면
    if(count == n) return;

    board[y][x] = true;
    for (int i = 0; i < 2; i++) {
      int nextMoveIdx = availableMove[pastMove][i];
      seeking(count + 1, nextMoveIdx,
          x + moveX[nextMoveIdx], y + moveY[nextMoveIdx]);
    }
    board[y][x] = false;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}