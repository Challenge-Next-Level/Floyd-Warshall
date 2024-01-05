// 예제 풀이보고 해석했다
// 1try 1solve !!
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());

    Deque<Integer> dq = new ArrayDeque<>();
    for (int i = 1; i <= n; i++) {
      dq.add(i);
    }

    while (dq.size() > 1) {
      int first = dq.pollFirst();
      for (int i = 1; i < k; i++) {
        dq.pollFirst();
      }
      dq.add(first);
      if (dq.size() < k) { // 하나 빼고 전부 제거
        int curSize = dq.size();
        for (int i = 0; i < curSize - 1; i++) {
          dq.pollLast();
        }
      }
    }

    System.out.println(dq.pollFirst());

  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}