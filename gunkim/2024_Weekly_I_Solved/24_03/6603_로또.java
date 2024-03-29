// 도대체 백트래킹은 어디에??
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int[] arr;
  private boolean[] visit;
  private int[] result;
  private StringBuilder sb = new StringBuilder();

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    while (true) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      if (n == 0) break;

      arr = new int[n];
      for (int i = 0; i < n; i++) {
        arr[i] = Integer.parseInt(st.nextToken());
      }

      // 로또 번호는 총 6개 뽑아야 함
      result = new int[6];
      // 현재 뽑은 번호는 visit으로 체크
      visit = new boolean[n];

      search(0, 0);

      sb.append("\n");
    }

    System.out.println(sb);

  }

  private void search(int idx, int depth) {
    if (depth == 6) { // 모두 뽑았으면 출력
      for (int num : result) {
        sb.append(num).append(" ");
      }
      sb.append("\n");
      return;
    }
    // 뽑아야하는 수 고르기
    for (int i = idx; i < n; i++) {
      if (!visit[i]) {
        result[depth] = arr[i];

        visit[i] = true;
        search(i + 1, depth + 1);
        visit[i] = false;
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}