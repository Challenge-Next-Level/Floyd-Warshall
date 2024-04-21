// 중위순회 개념
// 카운트를 어떻게 하면 되는지가 중요한 문제
import java.io.*;
import java.util.*;

public class Main {

  private class Node{
    int left;
    int right;
    public Node(int left, int right) {
      this.left = left;
      this.right = right;
    }
  }
  private int n;
  private List<Node>[] nodes;
  private List<Integer> inOrder;
  private int cnt = 0;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());

    nodes = new ArrayList[n+1];
    for(int i=0; i<=n; i++) {
      nodes[i] = new ArrayList<>();
    }

    StringTokenizer st;
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int parent = Integer.parseInt(st.nextToken());
      int left = Integer.parseInt(st.nextToken());
      int right = Integer.parseInt(st.nextToken());
      nodes[parent].add(new Node(left, right));
    }

    inOrder = new ArrayList<>();
    dfs(1, true);
    dfs(1, false);

  }

  private void dfs(int current, boolean flag) {
    for(Node node : nodes[current]) {
      if(node.left != -1) {
        dfs(node.left, flag);
        if(!flag) cnt++;
      }
      if(flag) {
        //중위순회로 노드 기록
        inOrder.add(current);
      } else {
        //탐색의 끝
        if(inOrder.get(inOrder.size()-1) == current) {
          System.out.println(cnt);
          return;
        }
        cnt++;
      }
      if(node.right != -1) {
        dfs(node.right, flag);
        if(!flag) cnt++;
      }
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}