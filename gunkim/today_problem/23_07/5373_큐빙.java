// 2차원 평면의 회전 좌표 값을 '점화식'으로 계산할 수 있다는 것을 알게 됨
// 3차원 육면체, 즉 큐브의 회전이 다른 2차원 평면에서 어떻게 swap을 할 수 있는지 알게 됨
// 자칫 빡구현 문제로 볼 수 있지만 위와 같이 도출해 내야 하는 공식과 개념이 뒷받침 되어야 했음
import java.io.*;
import java.util.*;

public class Main {

  private int test;
  private int n;

  static final int U = 0, D = 1, F = 2, B = 3, L = 4, R = 5;
  static char[][][] cube;
  static char[] colors = {'w', 'y', 'r', 'o', 'g', 'b'};
  private StringTokenizer st;


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    test = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < test; i++) {
      // 큐브 초기화
      cube = new char[6][3][3];
      for (int a = 0; a < 6; a++) {
        for (int b = 0; b < 3; b++) {
          for (int c = 0; c < 3; c++) {
            cube[a][b][c] = colors[a];
          }
        }
      }

      // 입력
      n = Integer.parseInt(br.readLine());
      st = new StringTokenizer(br.readLine());

      // 회전
      for (int j = 0; j < n; j++) {
        turn(st.nextToken());
      }

      // 출력
      for (int a = 0; a < 3; a++) {
        for (int b = 0; b < 3; b++) {
          sb.append(cube[U][b][2- a]); // 출력의도에 맞게 반시계 회전
        }
        sb.append("\n");
      }
    }

    System.out.println(sb);
  }

  static void alter(int f, int u, int l, int d, int r, boolean clk) { // (u,l,d,r 순서는 상관없음, 움직여지는 순서만 맞으면 됨)
    char[][] tmp = new char[3][3];
    char[] tmp2 = new char[3];

    if (clk) {
      // 면을 시계방향으로 돌림
      for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j) {
          tmp[i][j] = cube[f][2 - j][i]; // 정사각형 보드판을 회전하면 항상 이 공식대로 좌표는 계산된다.
        }
      // 바깥 4개 면을 시계방향 회전
      // 어떤 기준으로 4개의 면을 swap할 때 인덱스 값을 적절히 넣어준 걸까?
      // 나름의 기준을 유추해 보았다.
      // 하나의 면을 기준으로 바깥 4개의 면이 회전되며 swap 된다.
      // 아래 면은 결국 해당 면의 '위'가 될 것이고, 오른쪽 면은 해당 면의 '왼쪽'이 될 것이다.
      // 이를 이용해 아래 면의 '위' 부분과 , 오른쪽 면의 '왼쪽' 부분을 swap을 하는 것 같다.
      for (int i = 0; i < 3; ++i) // 처음 값은 백업
        tmp2[i] = cube[u][i][0];
      for (int i = 0; i < 3; ++i)
        cube[u][i][0] = cube[l][0][2 - i]; // 아래 면의 '위' 부분과 , 오른쪽 면의 '왼쪽' 부분을 swap
      for (int i = 0; i < 3; ++i)
        cube[l][0][2 - i] = cube[d][2][i];
      for (int i = 0; i < 3; ++i)
        cube[d][2][i] = cube[r][2 - i][2];
      for (int i = 0; i < 3; ++i)
        cube[r][2 - i][2] = tmp2[i];
    } else {
      // 면을 반시계방향으로 돌림
      for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j) {
          tmp[i][j] = cube[f][j][2 - i];
        }
      // 바깥 4개 면을 반계방향 회전
      for (int i = 0; i < 3; ++i)
        tmp2[i] = cube[u][i][0];
      for (int i = 0; i < 3; ++i)
        cube[u][i][0] = cube[r][2 - i][2];
      for (int i = 0; i < 3; ++i)
        cube[r][2 - i][2] = cube[d][2][i];
      for (int i = 0; i < 3; ++i)
        cube[d][2][i] = cube[l][0][2 - i];
      for (int i = 0; i < 3; ++i)
        cube[l][0][2 - i] = tmp2[i];
    }
    cube[f] = tmp;
  }

  static void turn(String s) {
    boolean flag = s.charAt(1) == '+';

    switch (s.charAt(0)) { // 정면에서 봤을 때 바깥 쪽 면은 왼쪽으로 회전하는 순서로 기입
      case 'U':
        alter(U, L, F, R, B, flag);
        break;
      case 'D':
        alter(D, B, R, F, L, flag);
        break;
      case 'F':
        alter(F, U, L, D, R, flag);
        break;
      case 'B':
        alter(B, R, D, L, U, flag);
        break;
      case 'L':
        alter(L, F, U, B, D, flag);
        break;
      case 'R':
        alter(R, D, B, U, F, flag);
        break;
    }

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}