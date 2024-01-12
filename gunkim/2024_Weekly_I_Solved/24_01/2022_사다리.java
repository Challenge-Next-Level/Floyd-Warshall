// 이분 탐색이 아니라 수학 문제다 그냥...
// 솔직히 제대로 이해 못했따
import java.io.*;
import java.util.*;

public class Main {

  private int[] dp;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    double x = Double.parseDouble(st.nextToken());
    double y = Double.parseDouble(st.nextToken());
    double c = Double.parseDouble(st.nextToken());

    double left = 0;
    double right = Math.min(x, y);

    while (right - left >= 0.001) {
      double a = (left + right) / 2;
      double h1 = Math.sqrt(Math.pow(x, 2) - Math.pow(a, 2));
      double h2 = Math.sqrt(Math.pow(y, 2) - Math.pow(a, 2));
      double resultC = (h1 * h2) / (h1 + h2);

      if (resultC >= c) left = a;
      else right = a;
    }

    System.out.println(String.format("%.3f", right));
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}