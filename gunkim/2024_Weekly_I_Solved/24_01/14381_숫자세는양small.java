// INSOMNIA케이스를 도대체 어떻게 찾는 건가? 때문에 풀이를 찾아봤다
// 그냥 적당히 돌려보고 안되면 INSOMNIA 케이스로 해결하라는 풀이밖에 찾을 수 없었다
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());

    for (int i = 0; i < t; i++) {
      int n = Integer.parseInt(br.readLine());
      StringBuilder sb = new StringBuilder();
      sb.append("Case #").append(i + 1).append(": ");

      int idx = 1;
      Set<Integer> set = new HashSet<>();
      boolean flag = false;

      // 적당히 100까지 idx를 높이며 곱해줬다
      while (idx < 100) {
        int num = n * idx;
        while (num > 0) {
          int remain = num % 10;
          if (!set.contains(remain)) {
            set.add(remain);
          }
          num /= 10;
        }

        // set 사이즈가 10이면 모두 채워진거기 때문에 백트래킹 조건
        if (set.size() == 10) {
          sb.append(n * idx);
          System.out.println(sb);
          break;
        }
        idx++;

        // 마지막까지 조건을 돌렸다면 flag로 체크
        if (idx == 99) flag = true;
      }

      // 마지막까지 조건을 돌린 숫자는 INSOMNIA
      if (flag) {
        sb.append("INSOMNIA");
        System.out.println(sb);
      }
    }

  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}