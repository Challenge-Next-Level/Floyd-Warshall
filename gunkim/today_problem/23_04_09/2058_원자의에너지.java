//트리의 독립집합을 이해하면 개념을 그대로 적용하여 풀 수 있다.
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {


  private ArrayList<Integer>[] list;
  private int[][] node;
  private int[] weight;
  private boolean[] visit;

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    //노드의 가중치(에너지) 저장
    weight = new int[n];
    HashMap<Integer, Integer> bridge = new HashMap(); //해당 에너지 준위에 대해 체크
    for (int i = 0; i < n; i++) {
      int w = Integer.parseInt(br.readLine());
      weight[i] = w;
      bridge.put(w, i);
    }
    ArrayList<Integer> energy = new ArrayList<>(); //양성자 에너지 저장
    for (int i = 0; i < m; i++) {
      energy.add(Integer.parseInt(br.readLine()));
    }
    list = new ArrayList[n];
    for (int i = 0; i < n; i++) {
      list[i] = new ArrayList<>();
    }
    for (int i = 0; i < n; i++) { //가중치에서
      for (int j = 0; j < m; j++) { //양성자 +, - 하면 에너지 준위가 있는지 확인
        int plus = weight[i] + energy.get(j);
        int minus = weight[i] - energy.get(j);
        if (bridge.get(plus) != null) {
          list[i].add(bridge.get(plus));
          list[bridge.get(plus)].add(i);
        }
      }
    }

    node = new int[n][2];
    visit = new boolean[n];
    traversal(0);
    System.out.println(Math.max(node[0][0], node[0][1]));

  }

  public void traversal(int cur) {
    int childSize = list[cur].size();
    node[cur][0] = 0;
    node[cur][1] = weight[cur];

    if (childSize == 0) return;

    visit[cur] = true;
    for (int child : list[cur]) {
      if (!visit[child]) {
        traversal(child);
        //현재 노드가 참석하지 않는 경우
        if (node[child][0] > node[child][1]) node[cur][0] += node[child][0];
        else node[cur][0] += node[child][1];
        //현재 노드가 참석하는 경우
        node[cur][1] += node[child][0];
      }
    }
    visit[cur] = false;
  }


  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}