// 세그먼트 트리 개념 및 구현 실력이 있어야 함
// 내가 참고한 사람의 풀이에 따르면 변형 구현도 필요. 어려운 문제다
import java.io.*;
import java.util.*;

public class Main {

  static int[] arr;
  static int[] tree;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());

    StringTokenizer st = new StringTokenizer(br.readLine());
    arr = new int[n + 1];
    for (int i = 1; i <= n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    // 세그먼트 트리를 만드려면 (n개의 데이터보다 큰 제곱수 * 2)만큼의 사이즈가 필요함
    // 이걸 대충 곱하기 4만큼의 사이즈로 지정을 하는 것 같음
    tree = new int[n * 4];

    // 세그먼트 트리 만들기
    // 그런데 일반적인 세그먼트 트리가 아님. 노드는 해당 노드의 하위 노드 중 가장 작은 값을 갖게 만든다
    // 즉, 루트 노드는 가장 작은 값을 가지게 될 것
    init(1, n, 1);


    int m = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      if (a == 1) { // 숫자 변경
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        arr[b] = c;

        update(1, n, 1, b);
      } else { // 가장 작은 값 출력
        sb.append(tree[1]).append("\n");
      }
    }
    System.out.println(sb);


  }

  private static int init(int start, int end, int node) {
    if (start == end) {
      return tree[node] = start;
    }
    int mid = (start + end) / 2;
    return tree[node] = minIndex(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1));
  }

  private static int minIndex(int x, int y) {
    if (arr[x] == arr[y]) {
      return Math.min(x, y);
    } else {
      return arr[x] < arr[y] ? x : y;
    }
  }

  private static int update(int start, int end, int node, int index) {
    if (start > index || end < index) {
      return tree[node];
    }
    if (start == end) {
      return tree[node] = index;
    }
    int mid = (start + end) / 2;
    return tree[node] = minIndex(update(start, mid, node * 2, index), update(mid + 1, end, node * 2 + 1, index));
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}