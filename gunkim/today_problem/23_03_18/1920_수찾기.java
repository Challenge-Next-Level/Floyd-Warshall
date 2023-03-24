import java.util.*;
import java.io.*;

public class Main {
  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    HashSet<Integer> set = new HashSet<>();
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      set.add(Integer.parseInt(st.nextToken()));
    }

    int m = Integer.parseInt(br.readLine());
    int[] B = new int[m];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      B[i] = Integer.parseInt(st.nextToken());
    }

    for (Integer num : B) {
      if (set.contains(num)) System.out.println(1);
      else System.out.println(0);
    }

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}