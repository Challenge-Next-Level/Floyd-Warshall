//A의 숫자가 B의 정렬된 리스트에서 어느 위치에 있으면 되는지 이분 탐색으로 찾는 문제였음
//다른 분의 풀이를 가져와서 이상한 해결법을 제출하게 됨, 다음 번에는 간단한 이분 탐색으로 진행하면 될 것 같음
//이 풀이는 TreeSet 을 이용한 풀이
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.util.Arrays.stream;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < t; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());

      ArrayList<Integer> A = stream(br.readLine().split(" "))
          .mapToInt(Integer::parseInt)
          .boxed()
          .collect(Collectors.toCollection(ArrayList::new));

      TreeSet<Integer> B = stream(br.readLine().split(" "))
          .mapToInt(Integer::parseInt)
          .boxed()
          .collect(Collectors.toCollection(TreeSet::new));

      long sum = 0L;

      for (Integer num : A) {
        long result = num;
        if (!B.contains(num)) {
          B.add(num);
          Integer lower = B.lower(num);
          Integer higher = B.higher(num);

          if (lower == null) result = higher;
          else if (higher == null) result = lower;
          else {
            if (Math.abs(num - lower) <= Math.abs(num - higher)) result = lower;
            else result = higher;
          }

          B.remove(num);
        }
        sum += result;
      }
      sb.append(sum).append('\n');

    }
    System.out.println(sb);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}