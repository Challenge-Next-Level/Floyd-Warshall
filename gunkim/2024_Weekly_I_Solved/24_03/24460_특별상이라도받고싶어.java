// 분할 정복 (재귀)
import java.io.*;
import java.util.*;

public class Main {

  static int[][] seats;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    final int n = Integer.parseInt(br.readLine());

    seats = new int[n][n];

    for (int i = 0 ; i < n ; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0 ; j < n ; j++) {
        seats[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int seat = selectSeat(n, 0, 0);
    System.out.println(seat);
  }

  private static int selectSeat(int size, int y, int x) {
    if (size < 2) {
      return seats[y][x];
    }

    final int half = size / 2;
    int[] tmp = new int[4];

    tmp[0] = selectSeat(half, y, x);
    tmp[1] = selectSeat(half, y + half, x);
    tmp[2] = selectSeat(half, y, x + half);
    tmp[3] = selectSeat(half, y + half, x + half);

    Arrays.sort(tmp);
    return tmp[1];
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}