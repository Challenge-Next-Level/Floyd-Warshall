// 무난한 구현 문제
// 종이에 적으면서 해야지 머릿속에서는 생각보다 굴러가지가 않음
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    Deque<Integer> dq = new ArrayDeque<>();
    dq.add(n);

    int num = n - 1;
    while (num > 0) {
      dq.addFirst(num);
      for (int i = 0; i < num; i++) {
        int backNum = dq.pollLast();
        dq.addFirst(backNum);
      }
      num--;
    }

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < n; i++) {
      sb.append(dq.poll()).append(" ");
    }
    System.out.println(sb);


  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}