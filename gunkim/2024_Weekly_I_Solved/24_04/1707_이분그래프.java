// 이분 그래프가 무엇인지 알게 됨
// bfs 탐색을 한다는 가정하에 같은 깊이의 탐색은 같은 색을 갖고
// 인접한 노드는 서로 다른 색이어야 함
// blue - red - blue - red 이런식으로
import java.io.*;
import java.util.*;

public class Main {

  private List<Integer>[] nodes;
  private boolean[] visit;
  private char[] color;
  private int v;
  private int e;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int k = Integer.parseInt(br.readLine());
    // k 개의 테스트 케이스
    for (int i = 0; i < k; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      v = Integer.parseInt(st.nextToken());
      e = Integer.parseInt(st.nextToken());

      nodes = new List[v + 1];
      for (int j = 0; j < v + 1; j++) {
        nodes[j] = new ArrayList<>();
      }

      // 연결되는 노드의 정보를 저장
      for (int j = 0; j < e; j++) {
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        nodes[a].add(b);
        nodes[b].add(a);
      }

      // bfs로 노드의 색을 정한다
      // 이때 모든 노드에 대해 bfs 탐색을 해봐야 함 (모든 노드가 연결되어 있다고 생각하지 말기)
      color = new char[v + 1];
      visit = new boolean[v + 1];
      for (int j = 1; j <= v; j++) {
        if (!visit[j])
          defineColorBFS(j);
      }


      // 인접한 노드들끼리는 같은 색을 갖고 있어야 함
      // 처음에 BFS를 한 번 더 해서 맞는지 검증하려 했음. 그러나 해당 방법은 시간 초과 발생
      boolean flag = true;
      for (int j = 1; j <= v; j++) {
        if(!flag) break;
        int curColor = color[j];
        for (int l = 0; l < nodes[j].size(); l++) {
          int connected = nodes[j].get(l);
          if (curColor == color[connected]) {
            flag = false;
            break;
          }
        }
      }

      if (flag)
        System.out.println("YES");
      else
        System.out.println("NO");
    }

  }

  private class Node {
    private int num;
    private int count;

    public Node(int num, int count) {
      this.num = num;
      this.count = count;
    }
  }



  private void defineColorBFS(int start) {
    Deque<Node> dq = new ArrayDeque<>();
    dq.add(new Node(start, 1));
    visit[start] = true;
    color[start] = 'b';

    while (!dq.isEmpty()) {
      Node node = dq.pollFirst();
      int curNum = node.num;
      int curCnt = node.count;

      for (int i = 0; i < nodes[curNum].size(); i++) {
        int next = nodes[curNum].get(i);
        if (visit[next]) continue;

        visit[next] = true;
        if (curCnt % 2 == 0)
          color[next] = 'b';
        else
          color[next] = 'r';
        dq.add(new Node(next, curCnt + 1));
      }
    }

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}