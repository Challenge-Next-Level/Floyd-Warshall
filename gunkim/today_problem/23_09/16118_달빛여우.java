// 시간초과가 발생하는데 도대체 이유를 모르겠음
// 42퍼에서 발생함
import java.io.*;
import java.util.*;
public class Main {

  private static int[] foxTime;
  private static int[][] wolfTime;
  private static List<Bridge>[] nodeBridges;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    // 그루터기가 갖는 오솔길 경로 설정
    nodeBridges = new ArrayList[n + 1];
    for (int i = 1; i <= n; i++) {
      nodeBridges[i] = new ArrayList<>();
    }
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      // 거리를 2로 곱하는 이유: 늑대가 느리게 달릴 때 홀수 거리에 대한 계산이 소수점으로 나옴
      // 형 변환에 대한 시간이 성능적으로 좋지 않기 때문 + 편리하게 계산하기 위함
      int distance = Integer.parseInt(st.nextToken()) * 2;
      nodeBridges[nodeA].add(new Bridge(nodeB, distance));
      nodeBridges[nodeB].add(new Bridge(nodeA, distance));
    }

    foxTime = new int[n + 1];
    wolfTime = new int[2][n + 1];

    Arrays.fill(foxTime, Integer.MAX_VALUE);
    Arrays.fill(wolfTime[0], Integer.MAX_VALUE);
    Arrays.fill(wolfTime[1], Integer.MAX_VALUE);

    dijkstra();
    dijkstraWolf();

    int answer = 0;
    for (int i = 1; i <= n; i++) {
      if (foxTime[i] < Math.min(wolfTime[0][i], wolfTime[1][i])) {
        answer++;
      }
    }
    System.out.println(answer);
  }

  private static void dijkstraWolf() {
    Queue<Info> q = new PriorityQueue<>();
    q.offer(new Info(1, 0, 0));
    wolfTime[0][1] = 0;

    while (!q.isEmpty()) {
      Info info = q.poll();
      int currentNode = info.target;
      long currentTime = info.time;
      int currentIsFast = info.isFast;

      if (currentTime > wolfTime[currentIsFast][currentNode]) continue;

      for (Bridge b : nodeBridges[currentNode]) {
        int cost = wolfTime[currentIsFast][currentNode];
        if (currentIsFast == 0) { // 느리게 달려왔으니 빠르게 달릴 차례, 시간을 단축시킨다
          cost += b.time / 2;
        } else { // 빠르게 달려왔으니 느리게 달릴 차례, 시간을 연장시킨다
          cost += b.time * 2;
        }

        int nextIsFast = 1 - currentIsFast;
        if (cost >= wolfTime[nextIsFast][b.to]) continue;
        wolfTime[nextIsFast][b.to] = cost;
        q.offer(new Info(b.to, cost, nextIsFast));
      }
    }
  }

  private static void dijkstra() {
    Queue<Bridge> q = new PriorityQueue<>();
    q.offer(new Bridge(1, 0));
    foxTime[1] = 0;

    while (!q.isEmpty()) {
      Bridge bridge = q.poll();
      if (bridge.time > foxTime[bridge.to]) continue;
      for (Bridge b : nodeBridges[bridge.to]) {
        int cost = b.time + foxTime[bridge.to];
        if (cost >= foxTime[b.to]) continue;
        foxTime[b.to] = cost;
        q.offer(new Bridge(b.to, cost));
      }
    }
  }

  static class Info implements Comparable<Info> {
    private int target;
    private int time;
    private int isFast; // 0: 느리게 달려왔을 때, 1: 빠르게 달려왔을 때

    public Info(int target, int time, int isFast) {
      this.target = target;
      this.time = time;
      this.isFast = isFast;
    }

    @Override
    public int compareTo(Info o) {
      return this.time - o.time;
    }
  }

  static class Bridge implements Comparable<Bridge> {
    private int to;
    private int time;

    public Bridge(int to, int time) {
      this.to = to;
      this.time = time;
    }

    @Override
    public int compareTo(Bridge o) {
      return this.time - o.time;
    }
  }




  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}