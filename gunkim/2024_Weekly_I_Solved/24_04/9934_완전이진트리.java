// 중위 순회 결과를 이용하는 문제
// 중위 순회 결과에서 중간 값은 root node 가 된다
import java.io.*;
import java.util.*;

public class Main {

  private int k;
  private int size;
  private int[] arr;
  private List<ArrayList<Integer>> nodes;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    k = Integer.parseInt(br.readLine());
    size = (int)Math.pow(2, k) - 1;
    arr = new int[size];

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < size; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    nodes = new ArrayList<>();
    for (int i = 1; i <= size; i++) {
      nodes.add(new ArrayList<>());
    }

    search(0, size - 1, 0);

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < k; i++) {
      for (int j : nodes.get(i)) {
        sb.append(j).append(" ");
      }
      sb.append("\n");
    }

    System.out.println(sb);
  }

  private void search(int start, int end, int depth) {
    if(depth == k) {
      return;
    }

    // 중간값 : 탐색 구간의 루트 노드가 된다
    int mid = (start + end) / 2;

    // depth에 맞게 노드 삽입
    nodes.get(depth).add(arr[mid]);

    // 왼쪽 노드(시작부터 중간 - 1 까지)
    search(start, mid - 1, depth + 1);
    // 오른쪽 노드 ( 중간 + 1 부터 끝까지)
    search(mid + 1, end, depth + 1);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}