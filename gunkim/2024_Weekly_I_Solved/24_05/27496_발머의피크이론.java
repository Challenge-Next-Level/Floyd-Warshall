// 매우 간단한 누적합 문제
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int l = Integer.parseInt(st.nextToken());

    int sum = 0;
    int[] alcohol = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      alcohol[i] = Integer.parseInt(st.nextToken());
    }

    int time = 0;
    for (int i = 0; i < n; i++) {
      sum += alcohol[i];
      if (i >= l) sum -= alcohol[i - l];

      if (sum >= 129 && sum <= 138) time += 1;
    }

    System.out.println(time);

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}