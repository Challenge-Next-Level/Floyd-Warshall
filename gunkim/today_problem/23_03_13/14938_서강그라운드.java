//다익스트라에 대한 개념을 다시 한 번 잡은 뒤
//우선 순위 큐로 깔끔하게 최단 경로를 가져오는 방법을 습득
import java.util.*;
import java.io.*;


public class Main {

  private int n;
  private int m;
  private ArrayList<Info>[] graph; //노드에 연결된 노드 정보를 저장
  private int[] items; //해당 노드에 떨어져 있는 아이템 수 저장

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    int r = Integer.parseInt(st.nextToken());

    items = new int[n + 1]; //아이템 수 정보 초기화
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; i++) {
      items[i] = Integer.parseInt(st.nextToken());
    }

    graph = new ArrayList[n + 1]; //간선 정보 초기화
    for (int i = 1; i <= n; i++) {
      graph[i] = new ArrayList<>(); //new 초기화 필수
    }
    for (int i = 0; i < r; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int l = Integer.parseInt(st.nextToken());
      graph[a].add(new Info(b, l));
      graph[b].add(new Info(a, l));
    }

    int answer = 0;
    for (int i = 1; i <= n; i++) { //각 노드에서 다익스트라 계산
      answer = Math.max(answer, dijkstra(i));
    }
    System.out.println(answer);
  }

  public int dijkstra(int node) {
    boolean[] visit = new boolean[n + 1]; //방문 체크
    int[] cost = new int[n + 1]; //최소 거리 체크
    for (int i = 0; i < n + 1; i++) { //최소 거리 초기화
      cost[i] = Integer.MAX_VALUE;
    }
    cost[node] = 0; //시작하는 node는 최소 거리가 0
    PriorityQueue<Info> pq = new PriorityQueue<>(); //우선 순위 큐를 통해 최단 거리에 있는 노드를 쉽게 찾는다.
    pq.add(new Info(node, 0));

    while (!pq.isEmpty()) { //본격적인 다익스트라 탐색
      Info cur = pq.poll();
      visit[cur.node] = true;
      for (Info next : graph[cur.node]) {
        if (!visit[next.node]) {
          cost[next.node] = Math.min(cost[next.node], cur.cost + next.cost);
          pq.add(new Info(next.node, cur.cost + next.cost));
        }
      }
    }

    int result = 0;
    for (int i = 1; i < n + 1; i++) {
      if (cost[i] <= m) result += items[i];
    }
    return result;
  }

  public class Info implements Comparable<Info> {
    private int node;
    private int cost;
    public Info(int node, int cost) {
      this.node = node;
      this.cost = cost;
    }
    @Override
    public int compareTo(Info info) {
      return cost - info.cost;
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}