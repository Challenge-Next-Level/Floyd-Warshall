//union-find 알고리즘을 사용하는 풀이. 근데 내가 작성했던 블로그 글을 보며 풀었다...ㅠㅠ
import java.io.*;
import java.util.*;

public class Main {


  private int[] parent;
  private int[] rank;

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    parent = new int[n + 1];
    rank = new int[n + 1];
    for (int i = 0; i < n + 1; i++) {
      parent[i] = i;
      rank[i] = 0;
    }

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int command = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      if (command == 0) {
        union(a, b);
      } else if (command == 1) {
        if (find(a) == find(b)) System.out.println("yes");
        else System.out.println("no");
      }

    }
  }

  public void union(int v1, int v2) {
    int root1 = find(v1);
    int root2 = find(v2);
    if (root1 != root2) {
      if (rank[root1] > rank[root2]) {
        parent[root2] = root1;
      } else {
        parent[root1] = root2;
        if (rank[root1] == rank[root2]) rank[root2] += 1;
      }
    }
  }

  public int find(int v) {
    if (parent[v] != v) {
      parent[v] = find(parent[v]);
    }
    return parent[v];
  }



  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}