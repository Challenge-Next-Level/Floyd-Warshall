// 어떤 부분에서 백트래킹을 할 것 인가? 에 대한 답이 어려웠던 문제
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private int[] arr;
  private boolean[] visit;
  private int[] result;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    // 수열 입력 받기
    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for(int i = 0; i < n; i++)
      arr[i] = Integer.parseInt(st.nextToken());
    // 정렬
    Arrays.sort(arr);

    // 숫자들을 하나씩 뽑을 텐데 뽑은 숫자는 visit으로 check
    visit = new boolean[n];
    // 뽑은 숫자들을 저장해두는 곳
    result = new int[m];
    // 재귀 탐색을 하자
    dfs(0);

  }

  private void dfs(int depth) {
    if (depth == m) {
      for (int i = 0; i < m; i++)
        System.out.print(result[i] + " ");
      System.out.println();
    } else { // 동일한 depth에 숫자를 추가하는 과정
      int before = 0; // 10000보다 작은 자연수가 아닌 값으로 초기화
      for (int i = 0; i < n; i++) {
        // visit 체크 제외한 숫자들 중 추가를 해야 함
        if (visit[i]) {
          continue;
        }

        if (before != arr[i]) { // 해당 숫자를 추가
          result[depth] = arr[i];
          before = arr[i];

          visit[i] = true;
          dfs(depth + 1);
          visit[i] = false;
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}