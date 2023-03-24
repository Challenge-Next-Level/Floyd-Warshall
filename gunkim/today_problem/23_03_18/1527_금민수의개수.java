import java.util.*;
import java.io.*;

public class Main {
  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());

    int answer = 0;
    for (int i = A; i <= B; i++) {
      int num = i;
      boolean flag = true;
      while (num > 0) {
        if (num % 10 == 4 || num % 10 == 7) {
          num /= 10;
        } else {
          flag = false;
          break;
        }
      }
      if (flag) answer += 1;
    }

    System.out.println(answer);

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}