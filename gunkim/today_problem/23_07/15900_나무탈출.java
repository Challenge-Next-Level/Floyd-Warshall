// 리프노드로 가는 간선의 수를 모두 더하면 됨
// 그 값이 홀수라면 무조건 이길 수 있다.
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    ArrayList<Integer>[] tree = new ArrayList[n + 1];

    for (int i = 1; i <= n ; i++) {
      tree[i] = new ArrayList();
    }

    // 간선 입력 받기
    StringTokenizer st;
    for (int i = 1; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      tree[nodeA].add(nodeB);
      tree[nodeB].add(nodeA);
    }

    // bfs로 모든 리프노드로 가는 간선 수 파악하기
    boolean[] visit = new boolean[n + 1];
    Deque<Info> dq = new ArrayDeque<>();
    dq.add(new Info(1, 0));
    visit[1] = true;
    int count = 0;
    while (!dq.isEmpty()) {
      Info info = dq.pollFirst();
      int flag = 0;
      for (int i = 0; i < tree[info.node].size(); i++) {
        int newNode = tree[info.node].get(i);
        if (!visit[newNode]) {
          flag++;
          visit[newNode] = true;
          dq.add(new Info(newNode, info.depth + 1));
        }
      }
      // 리프노드라면 depth를 count에 추가
      if (flag == 0) {
        count += info.depth;
      }
    }

    if (count % 2 == 0) {
      System.out.println("No");
    } else {
      System.out.println("Yes");
    }

  }

  private class Info {
    private int node;
    private int depth;

    public Info(int node, int depth) {
      this.node = node;
      this.depth = depth;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}