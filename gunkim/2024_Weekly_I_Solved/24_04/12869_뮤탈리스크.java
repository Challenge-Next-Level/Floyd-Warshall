// bfs 보단 재귀로 푸는 게 맞는 것 같은 문제
// 근데 이상한 점 발견
// attack 시 9,3,1 순이 가장 먼저 실행되지 않으면 정답이 틀림. 왜 그런걸까?
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int[] scv = new int[3];
  private boolean[][][] visited = new boolean[61][61][61];
  private int result = Integer.MAX_VALUE;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());

    for (int i = 0; i < n; i++) {
      scv[i] = Integer.parseInt(st.nextToken());
    }

    attack(scv[0], scv[1], scv[2], 0);

    System.out.println(result);
  }

  private void attack(int a, int b, int c, int count) {
    // 음수값은 0으로 처리
    a = Math.max(0, a);
    b = Math.max(0, b);
    c = Math.max(0, c);

    // scv가 모두 죽으면 정답 수정
    if (a == 0 && b == 0 && c == 0) {
      result = Math.min(result, count);
      return;
    }

    // visit 관리시 중요한 점
    // scv의 체력들이 [4,6,8]인 경우와 [8,6,4]인 경우는 같은 케이스
    // 따라서 정렬을 통해 visit을 기록
    Integer[] arr = {a, b, c};
    Arrays.sort(arr, Collections.reverseOrder());
    int one = arr[0];
    int two = arr[1];
    int three = arr[2];

    if (visited[one][two][three] || result < count) return;

    visited[one][two][three] = true;
    attack(one - 9, two - 3, three - 1, count + 1);
    attack(one - 9, two - 1, three - 3, count + 1);
    attack(one - 3, two - 1, three - 9, count + 1);
    attack(one - 3, two - 9, three - 1, count + 1);
    attack(one - 1, two - 9, three - 3, count + 1);
    attack(one - 1, two - 3, three - 9, count + 1);

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}