// 수학적인 센스가 필요한 문제라고 생각한다.
// 2^n으로 딱 나눠지는 크기이기 때문에 분할정복이 당연했던 문제었다.
// 대신 답을 알고 풀이를 진행했을 때도 제대로 구현하지 못했다. 분할 정복 함수 안을 센스있게 구현하는 것도 필요했다.
import java.io.*;
import java.util.*;

public class Main {

  private int x;
  private int y;
  private int[][] answer;
  private int tileNum;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    // (0,0) 부터 시작하기 때문에 -1을 한다.
    x = Integer.parseInt(st.nextToken()) - 1;
    y = Integer.parseInt(st.nextToken()) - 1;

    int len = (int)Math.pow(2, n); // 샤워실 바닥 한 변의 길이
    answer = new int[len][len];
    answer[y][x] = -1; // 배수구 표시
    tileNum = 0;

    // 참고: 2^n 길이를 갖는 타일 바닥은 한 곳이 뚫린상태로 'ㄱ'자 모양 타일로 전부 채울 수 있음
    // 예제에서 2^1 타일 바닥을 채우는 경우와 2^2 타일 바닥을 채우는 경우를 보여주고 있다.
    // 이는 2^n 타일 바닥을 채울 수 있다면 2^(n+1) 타일 바닥을 채울 수 있다는 증명이다.
    // 따라서 타일 바닥을 4부분으로 나눠가며 분할정복을 하면 된다.
    divideAndConquer(0, 0, len);

    // 출력
    StringBuilder sb = new StringBuilder();
    for (int i = len - 1; i >= 0; i--) {
      for (int j = 0; j < len; j++) {
        sb.append(answer[i][j]);
        if (j != len - 1)
          sb.append(" ");
      }
      if (i != 0)
        sb.append("\n");
    }
    System.out.println(sb);
  }

  private void divideAndConquer(int sy, int sx, int size) {
    tileNum++;
    int half = size / 2;
    // 4구간으로 나눈 후 타일이 없다면 모서리에 같은 타일들로 3개 채운다.
    if (!isTileExist(sy, sx, half))
      answer[sy + half - 1][sx + half - 1] = tileNum;
    if (!isTileExist(sy + half, sx, half))
      answer[sy + half][sx + half - 1] = tileNum;
    if (!isTileExist(sy, sx + half, half))
      answer[sy + half - 1][sx + half] = tileNum;
    if (!isTileExist(sy + half, sx + half, half))
      answer[sy + half][sx + half] = tileNum;

    if (size == 2) return;

    divideAndConquer(sy, sx, half);
    divideAndConquer(sy, sx + half, half);
    divideAndConquer(sy + half, sx, half);
    divideAndConquer(sy + half, sx + half, half);
  }

  private boolean isTileExist(int ny, int nx, int size) {
    for (int i = ny; i < ny + size; i++) {
      for (int j = nx; j < nx + size; j++) {
        if (answer[i][j] != 0) { // 배수구 or 타일이 채워진 곳이라면 false 리턴
          return true;
        }
      }
    }
    return false;
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}