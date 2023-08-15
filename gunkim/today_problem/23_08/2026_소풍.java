// 비슷하게 문제 접근을 해서 풀었는데 정답이 제대로 출력되지 않았었다.
// 친구를 어떻게 저장해두지에 대한 고민을 했는데 dfs를 하니 visit을 통해 체크한 것을 바탕으로 친구가 어떤 놈인지 파악할 수 있었다.(난 이렇게 하지 못했었음)
// 그리고 친구를 추가할 때 그 전 친구들과의 관계를 따로 확인하지 않았어서 내 풀이는 아쉬웠던 것 같다.
import java.io.*;
import java.util.*;

public class Main {


  private int k;
  private int n;
  private int[] count;
  private boolean[] visit;
  private boolean[][] students;
  private boolean check;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    k = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());
    int f = Integer.parseInt(st.nextToken());
    students = new boolean[n + 1][n + 1];
    count = new int[n + 1];
    for (int i = 0; i < f; i++) {
      st = new StringTokenizer(br.readLine());
      int studentA = Integer.parseInt(st.nextToken());
      int studentB = Integer.parseInt(st.nextToken());
      students[studentA][studentB] = true;
      students[studentB][studentA] = true;
      count[studentA]++;
      count[studentB]++;
    }

    visit = new boolean[n + 1];
    for (int i = 1; i <= n; i++) {
      if (count[i] < k - 1) continue;
      if (check) break;

      visit[i] = true;
      dfs(i, 1);
      visit[i] = false;
    }

    if (!check) {
      System.out.println(-1);
    }
  }

  public void dfs(int studentNum, int cnt) {
    if (check) return;
    if (cnt == k) { // 전부 친구인 관계를 만족한다면
      // 바로 친구들을 출력한다.
      // 왜냐하면 1번 친구부터 차례로 dfs를 했기 때문에 최초 정답이 오름차순으로 가장 빠른 친구들이기 때문이다.
      check = true;
      StringBuilder sb = new StringBuilder();
      for (int i = 1; i <= n; i++) {
        if (visit[i]) {
          sb.append(i).append("\n");
        }
      }
      System.out.println(sb);
      return;
    }

    // 다음 친구를 선정
    for (int i = studentNum + 1; i <= n; i++) {
      if (students[studentNum][i] && isFriend(i)) {
        visit[i] = true;
        dfs(i, cnt + 1);
        visit[i] = false;
      }
    }
  }

  // 방문 체크로 정해둔 친구들과 현재 추가할 친구가 서로 친구인지 확인
  public boolean isFriend(int target) {
    for(int i = 1; i <= n; i++) {
      if(visit[i] && !students[target][i])
        return false;
    }
    return true;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}