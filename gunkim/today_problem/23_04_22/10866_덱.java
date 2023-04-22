import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    Deque<Integer> deque = new ArrayDeque<>();
    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      String command = st.nextToken();
      if (command.equals("push_back")) {
        int num = Integer.parseInt(st.nextToken());
        deque.offerLast(num);
      } else if (command.equals("push_front")) {
        int num = Integer.parseInt(st.nextToken());
        deque.offerFirst(num);
      } else if (command.equals("pop_front")) {
        if (deque.size() == 0) System.out.println(-1);
        else System.out.println(deque.pollFirst());
      } else if (command.equals("pop_back")) {
        if (deque.size() == 0) System.out.println(-1);
        else System.out.println(deque.pollLast());
      } else if (command.equals("size")) {
        System.out.println(deque.size());
      } else if (command.equals("empty")) {
        if (deque.isEmpty()) System.out.println(1);
        else System.out.println(0);
      } else if (command.equals("front")) {
        if (deque.size() == 0) System.out.println(-1);
        else System.out.println(deque.peekFirst());
      } else if (command.equals("back")) {
        if (deque.size() == 0) System.out.println(-1);
        else System.out.println(deque.peekLast());
      }
    }

  }



  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}