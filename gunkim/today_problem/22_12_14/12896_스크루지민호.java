//소방서의 최적의 위치를 찾고, 답을 찾는 해결법이 아니다.
//트리의 지름이라는 특성을 이용해 '트리의 지름' 값이 결국 답과 같은 결론을 맺게 되어 다른 방식으로 접근하는 문제이다.
import java.util.*;
import java.io.*;

public class Main {
  static class Pair {
    int v, cost; //목적지,비용
    public Pair(int v, int cost) {
      this.v = v;
      this.cost = cost;
    }
  }
  static List<Pair>[] list; //List<Pair> 형 배열
  static boolean[] visit;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int n = Integer.parseInt(br.readLine());

    //1.배열에 도시마다의 Pair를 저장
    list = new ArrayList[n + 1];
    visit = new boolean[n + 1];
    for (int i = 0; i <= n; i++) {
      list[i] = new ArrayList<>(); //list란 배열을 ArrayList로 초기화
    }
    for (int i = 0; i < n - 1; i++) { //n-1 개의 도로
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());
      list[u].add(new Pair(v, 1));
      list[v].add(new Pair(u, 1));
    }

    //2.랜덤한 노드(여기선 1번 노드)를 선택하여 가장 거리가 먼 노드를 찾는다.
    Pair p = dfs(1);
    visit = new boolean[n + 1];
    //3.위에서 찾은 노드에서 가장 거리가 먼 노드를 다시 찾는다. 이 거리는 곧, 트리의 지름이 된다.
    //결국 정답은 트리의 지름을 묻고 있는 것이다.
    Pair r = dfs(p.v);
    //4.트리의 지름 값을 반으로 나눈 값이 정답이 된다.
    System.out.println((1 + r.cost) / 2);
  }


  static Pair dfs(int cur) {
    Pair result = new Pair(cur, 0);
    visit[cur] = true; // 노드 방문처리
    for (Pair next : list[cur]) { //cur 도시에서 갈 수 있는 도시 탐색
      if (visit[next.v]) continue;
      Pair x = dfs(next.v); //방문하지 않은 곳 dfs 탐색
      // 모든 자식까지 모두 방문이 끝나면 리프노드부터 부모노드의 비용을 더한다.
      x.cost += next.cost;
      // 항상 자식노드들 중 가장 큰 비용을 가진 자식을 리턴한다.
      if (x.cost > result.cost) result = x;
    }
    return result;
  }
}