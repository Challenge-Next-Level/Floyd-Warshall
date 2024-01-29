// 기호 1번의 표를 어떻게 증가시키지? 라는 물음이 있었는데...
// 그냥 pq에 저장하는게 아닌 따로 관리를 하면 되었음..
import java.io.*;
import java.util.*;

public class Main {



  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    int numberOne = Integer.parseInt(br.readLine()); // 기호 1번 표 저장

    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    for (int i = 1; i < n; i++) { // 나머지 후보의 표는 우선순위 큐(Max heap)에 저장
      pq.add(Integer.parseInt(br.readLine()));
    }

    int cnt = 0;
    // 가장 많은 표를 갖고 있는 후보가 기호 1번 표보다 크거나 같다면
    while (!pq.isEmpty() && pq.peek() >= numberOne) {
      int peek = pq.poll() - 1;
      numberOne += 1;
      cnt++;
      pq.add(peek);
    }

    System.out.println(cnt);

  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}