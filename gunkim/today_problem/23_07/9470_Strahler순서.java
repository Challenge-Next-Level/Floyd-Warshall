// 이 문제는 '위상 정렬'로 분류되는 문제이다. 그런데 이런 개념을 모르고 해결했다.
// 위상 정렬 문제는 큐를 이용한 풀이가 정석인데 나는 dp(재귀) 느낌으로 문제를 해결했다.
import java.io.*;
import java.util.*;

public class Main {

  private int[] orders;
  private ArrayList<Integer>[] nodes;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int test = Integer.parseInt(br.readLine());
    StringTokenizer st;
    for (int i = 0; i < test; i++) {
      st = new StringTokenizer(br.readLine());
      int k = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      int p = Integer.parseInt(st.nextToken());
      nodes = new ArrayList[m + 1];
      for (int j = 0; j < m + 1; j++) {
        nodes[j] = new ArrayList<>();
      }
      for (int j = 0; j < p; j++) {
        st = new StringTokenizer(br.readLine());
        int from = Integer.parseInt(st.nextToken());
        int to = Integer.parseInt(st.nextToken());
        // 간선의 정보를 거꾸로 저장. 내 노드로 어떤 강물이 흘러들어 오는지를 저장한다.
        nodes[to].add(from);
      }

      orders = new int[m + 1]; // 순서를 저장
      int answer = topToBottom(m); // m 노드의 순서를 계산하자

      // 출력
      StringBuilder sb = new StringBuilder();
      sb.append(k).append(" ").append(answer);
      System.out.println(sb);
    }
  }

  private int topToBottom(int node) {
    if (orders[node] != 0) { // 이미 방문해서 계산을 끝낸 곳이라면
      return orders[node];
    }
    if (nodes[node].size() == 0) { // 최상단 노드라면
      orders[node] = 1;
      return 1;
    }
    // 계산
    int maxNum = -1;
    int count = 0;
    for (int i = 0; i < nodes[node].size(); i++) {
      int from = nodes[node].get(i);
      if (orders[from] == 0) // 계산되지 않은 노드는 재귀로 계산하기
        topToBottom(from);

      if (orders[from] > maxNum) {
        maxNum = orders[from];
        count = 1;
      } else if (orders[from] == maxNum) {
        count++;
      }
    }

    if (count > 1) {
      orders[node] = maxNum + 1;
    } else {
      orders[node] = maxNum;
    }
    return orders[node];
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}