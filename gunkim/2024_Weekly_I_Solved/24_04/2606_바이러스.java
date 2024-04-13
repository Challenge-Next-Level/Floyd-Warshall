// 쉬운 bfs
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private List<Integer>[] nodes;
  private boolean[] visit;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    m = Integer.parseInt(br.readLine());

    nodes = new List[n + 1];
    for (int i = 0; i <= n; i++) {
      nodes[i] = new ArrayList<>();
    }

    StringTokenizer st;
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      nodes[a].add(b);
      nodes[b].add(a);
    }

    visit = new boolean[n + 1];
    System.out.println(bfs());
  }


  private int bfs() {
    Deque<Integer> dq = new ArrayDeque<>();
    // 1번 컴퓨터 감염으로 시작
    dq.add(1);
    visit[1] = true;

    int count = 0;
    while (!dq.isEmpty()) {
      int node = dq.pollFirst();

      for (int i = 0; i < nodes[node].size(); i++) {
        int next = nodes[node].get(i);
        if (visit[next]) continue;

        count++;
        visit[next] = true;
        dq.add(next);
      }
    }
    return count;
  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}