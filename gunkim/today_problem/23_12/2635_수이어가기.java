// DP를 이용해 머리를 좀 써야할 것 같았는데 전혀 아니었다
// 단순 brute force 문제였는데
// 오히려 이렇게 쉬운 구간 문제로 오니 머리가 더 꼬이는 것 같다
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(br.readLine());

    List<Integer> answer = new ArrayList<>();
    int maxSize = 0;

    for (int i = 1; i <= num; i++) {

      List<Integer> list = new ArrayList<>();
      list.add(num);
      list.add(i);

      int prev = num;
      int cur = i;
      int count = 2;
      while (true) {
        int next = prev - cur;
        if (next < 0) break;

        list.add(next);
        prev = cur;
        cur = next;
        count++;
      }

      if (count > maxSize) {
        maxSize = count;
        answer = list;
      }

    }

    System.out.println(maxSize);
    StringBuilder sb = new StringBuilder();
    for (Integer number : answer) {
      sb.append(number).append(" ");
    }

    System.out.println(sb);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}