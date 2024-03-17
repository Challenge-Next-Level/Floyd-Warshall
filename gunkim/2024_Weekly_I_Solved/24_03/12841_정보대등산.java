// 일반 누적합
// 자료형 int -> long으로 변환하니 정답
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    int[] distance = new int[n];
    for (int i = 0; i < n; i++) {
      distance[i] = Integer.parseInt(st.nextToken());
    }

    st = new StringTokenizer(br.readLine());
    long[] left = new long[n];
    for (int i = 1; i < n; i++) {
      left[i] = left[i - 1] + Integer.parseInt(st.nextToken());
    }

    int[] rightInput = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i < n; i++) {
      rightInput[i] = Integer.parseInt(st.nextToken());
    }

    long[] right = new long[n];
    for (int i = 1; i < n; i++) {
      right[i] = right[i - 1] + rightInput[n - i];
    }

    long minCost = Long.MAX_VALUE;
    int idx = -1;
    for (int i = 0; i < n; i++) {
      long cost = left[i] + right[n - 1 - i] + distance[i];
      if (cost < minCost) {
        minCost = cost;
        idx = i;
      }
    }

    StringBuilder sb = new StringBuilder();
    sb.append(idx + 1).append(" ").append(minCost);
    System.out.println(sb);

  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}