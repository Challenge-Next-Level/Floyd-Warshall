// 트리의 지름을 구하는 방법을 아는 것이 첫 번째
// 거기에 구현 방법만 추가하면 되는 문제 였음
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private List<Node>[] list;


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    list = new ArrayList[n+1];
    for (int i = 1; i <= n; i++) {
      list[i] = new ArrayList<>();
    }

    StringTokenizer st;
    for (int i = 1; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int d = Integer.parseInt(st.nextToken());

      list[a].add(new Node(b, d));
      list[b].add(new Node(a, d));
    }

    Node first = bfs(1,0); // 1에서 가장 먼 노드를 찾는다
    Node second = bfs(first.target,0); // first에서 가장 먼 노드를 찾는다

    // 트리의 지름을 담당하는 각각의 끝 정점에서 서로를 제외하고 가장 먼 노드를 찾는다
    int dis1 = bfs(first.target, second.target).cost;
    int dis2 = bfs(second.target, first.target).cost;
    System.out.println(Math.max(dis1, dis2));
  }

  public Node bfs(int s, int e) {
    Queue<Node> q = new LinkedList<>();
    boolean[] visited = new boolean[n+1];
    Node endNode = new Node(s,0);
    q.add(endNode);
    visited[s] = true;

    while(!q.isEmpty()) {
      Node p = q.poll();

      if(p.cost > endNode.cost && p.target != e) {
        endNode.target = p.target;
        endNode.cost = p.cost;
      }

      for(Node nxt : list[p.target]) {
        if(visited[nxt.target]) continue;
        visited[nxt.target] = true;
        q.add(new Node(nxt.target, p.cost + nxt.cost));
      }
    }
    return endNode;
  }

  public class Node{
    int target;
    int cost;

    public Node(int target, int cost) {
      this.target = target;
      this.cost = cost;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}