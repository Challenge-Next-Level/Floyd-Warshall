// min heap을 생각하여 priority queue를 이용해 해결했다
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int i = 0; i < n; i++) {
      pq.add(Integer.parseInt(br.readLine()));
    }

    int count = 0;
    while (pq.size() > 1) {
      int first = pq.poll();
      int second = pq.poll();
      pq.add(first + second);
      count += first + second;
    }

    System.out.println(count);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}