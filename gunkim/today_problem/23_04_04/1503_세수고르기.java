//진짜 무슨 문제임 이거...
import java.util.*;
import java.io.*;

public class Main {

  private int[] location;
  private int n;

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    boolean[] check = new boolean[1002];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      int idx = Integer.parseInt(st.nextToken());
      check[idx] = true;
    }
    int answer = Integer.MAX_VALUE;
    for (int i = 1; i <= 1001; i++) {
      if (check[i]) continue;
      if (answer == 0) break;
      for (int j = i; j <= 1001; j++) {
        if (check[j]) continue;
        for (int k = j; k <= 1001; k++) {
          if (check[k]) continue;
          answer = Math.min(answer, Math.abs(n - i * j * k));
        }
      }
    }
    System.out.println(answer);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();

  }

}