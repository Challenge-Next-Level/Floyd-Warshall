// 일반적인 그래프 탐색
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private List<Integer>[] nodes;
  // key: 자식, value: 부모
  private Map<Integer, Integer> map = new HashMap<>();


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    nodes = new List[n + 1];
    for (int i = 1; i <= n; i++) {
      nodes[i] = new ArrayList<>();
    }

    StringTokenizer st;
    for (int i = 1; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      nodes[a].add(b);
      nodes[b].add(a);
    }

    bfs();

    StringBuilder sb = new StringBuilder();
    for (int i = 2; i <= n; i++) {
      sb.append(map.get(i)).append("\n");
    }
    System.out.println(sb);

  }

  private void bfs() {
    Deque<Integer> dq = new ArrayDeque<>();
    boolean[] visit = new boolean[n + 1];
    dq.add(1);
    visit[1] = true;

    while (!dq.isEmpty()) {
      int parent = dq.pollFirst();

      for (int i = 0; i < nodes[parent].size(); i++) {
        int child = nodes[parent].get(i);
        if (visit[child]) continue;

        visit[child] = true;
        map.put(child, parent);
        dq.add(child);
      }

    }
  }





  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}