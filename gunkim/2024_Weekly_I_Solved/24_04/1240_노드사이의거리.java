// 노드 사이 거리를 잘 저장해두고
// 시작점 부터 도착점 까지 bfs로 탐색하며 거리만 계산하면 되는 문제
import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int m;
  private int distance[][];
  private boolean visited[];

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    distance = new int[n + 1][n + 1];

    for (int i = 0; i < n - 1; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int dis = Integer.parseInt(st.nextToken());

      distance[a][b] = dis;
      distance[b][a] = dis;
    }

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      bfs(start, end, n);
    }



  }

  private void bfs(int start, int end, int size){
    Queue<Integer> queue = new LinkedList<>();
    visited = new boolean[size+1];

    visited[start] = true;
    queue.add(start);
    int ans[] = new int[size+1];

    while(!queue.isEmpty()){
      int cur = queue.poll();

      for (int i = 1; i <= size; i++) {

        if (distance[cur][i] != 0 && !visited[i]) {// 만약 연결되어 있고 방문하지 않은 노드이면
          ans[i] += distance[cur][i] + ans[cur];// 거리를 갱신해준다.

          if (i == end) {// 만약 마지막 노드이면 종료
            System.out.println(ans[end]);
            return;
          }

          queue.add(i);
          visited[i] = true;
        }
      }
    }

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}