// 최소 스패닝 트리 문제. 다익스트라랑 착각했다...
// 항상 어려운 것 같다
import java.io.*;
import java.util.*;

public class Main {


  static int[] parent;
  static ArrayList<Edge> edgeList;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());

    Point[] points = new Point[N];
    StringTokenizer st;
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      double x = Double.parseDouble(st.nextToken());
      double y = Double.parseDouble(st.nextToken());

      points[i] = new Point(i, x, y);
    }

    // 모든 별들 간의 간선과 비용 정보를 edgeList에 넣어 둔다.
    edgeList = new ArrayList<>();
    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        double weight = distance(points[i], points[j]);

        edgeList.add(new Edge(points[i].num, points[j].num, weight));
      }
    }

    Collections.sort(edgeList); // 간선의 비용을 기준으로 오름차순 정렬.

    parent = new int[N];
    for (int i = 0; i < N; i++) {
      parent[i] = i; // 초기화
    }

    double ans = 0;

    // 크루스칼 알고리즘 수행.
    for (int i = 0; i < edgeList.size(); i++) {
      Edge edge = edgeList.get(i);

      if (find(edge.start) != find(edge.end)) {
        ans += edge.weight;
        union(edge.start, edge.end);
      }
    }

    System.out.println(String.format("%.2f", ans));

  }

  public static double distance(Point p1, Point p2) {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
  }

  public static int find(int x) {
    if (x == parent[x]) {
      return x;
    }
    parent[x] = find(parent[x]);
    return parent[x];
  }

  public static void union(int x, int y) {
    x = find(x);
    y = find(y);

    if (x != y) {
      parent[y] = x;
    }
  }

  class Point {
    int num;
    double x;
    double y;

    Point(int num, double x, double y) {
      this.num = num;
      this.x = x;
      this.y = y;
    }
  }

  class Edge implements Comparable<Edge> {
    int start;
    int end;
    double weight;

    Edge(int start, int end, double weight) {
      this.start = start;
      this.end = end;
      this.weight = weight;
    }

    @Override
    public int compareTo(Edge o) {
      if (weight < o.weight) {
        return -1;
      }
      return 1;
    }

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}