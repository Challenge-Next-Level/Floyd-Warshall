// 물을 옮기는 과정을 '간단한 코드로 구현'하는 것이 은근히 복잡했음
// bfs 문제였고 1 try 1 solve !!!
import java.io.*;
import java.util.*;

public class Main {

  private int[] maxBowl;
  private boolean[][][] visit;
  private Set<Integer> set = new HashSet<>();

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    maxBowl = new int[3];

    maxBowl[0] = Integer.parseInt(st.nextToken());
    maxBowl[1] = Integer.parseInt(st.nextToken());
    maxBowl[2] = Integer.parseInt(st.nextToken());

    // 각 물통에 담긴 물의 양을 visit 처리하기 위함
    visit = new boolean[201][201][201];
    bfs();

    // 정답 출력
    List<Integer> list = new ArrayList<>(set);
    Collections.sort(list);
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < list.size(); i++) {
      sb.append(list.get(i)).append(" ");
    }
    System.out.println(sb);

  }

  // 몇 번째(as) 물통에서 몇 번째(be) 물통으로 옮길지에 대한 인덱스
  private int[][] asToBe = {{0, 1}, {0, 2}, {1, 0}, {1, 2}, {2, 0}, {2, 1}};
  private void bfs() {
    Deque<int[]> dq = new ArrayDeque<>();
    int[] arr = new int[3];
    arr[0] = 0;
    arr[1] = 0;
    arr[2] = maxBowl[2];
    dq.add(arr);
    visit[0][0][maxBowl[2]] = true;

    while (!dq.isEmpty()) {
      int[] bowl = dq.pollFirst();

      // a 물통이 비어있다면 c 물통을 set에 기록
      if (bowl[0] == 0)
        set.add(bowl[2]);

      // 6가지 경우의 수에 대해 bfs 탐색
      for (int i = 0; i < 6; i++) {
        int[] nArr = new int[3];
        nArr[0] = bowl[0];
        nArr[1] = bowl[1];
        nArr[2] = bowl[2];

        int as = asToBe[i][0];
        int be = asToBe[i][1];

        // 옮기려는 물통이 비어있거나 담으려는 물통이 꽉차있다면 탐색 불가능
        if (bowl[as] == 0 || bowl[be] == maxBowl[be]) continue;
        int give = bowl[as]; // 줄 수 있는 최대치의 양
        int take = maxBowl[be] - bowl[be]; // 받을 수 있는 최대치의 양

        if (take >= give) {
          nArr[as] = 0;
          nArr[be] = bowl[be] + give;
        } else {
          nArr[as] = give - take;
          nArr[be] = maxBowl[be];
        }

        if (visit[nArr[0]][nArr[1]][nArr[2]]) continue;

        visit[nArr[0]][nArr[1]][nArr[2]] = true;
        dq.add(nArr);

      }
    }

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}