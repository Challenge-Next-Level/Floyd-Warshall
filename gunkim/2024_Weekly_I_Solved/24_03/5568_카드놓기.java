import java.io.*;
import java.util.*;

public class Main {

  private int n;
  private int k;
  private int[] arr;
  private boolean[] visit;
  private int[] result;
  private Map<Integer, Boolean> map = new HashMap<>();

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    k = Integer.parseInt(br.readLine());

    arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(arr);

    result = new int[k];
    visit = new boolean[n];

    search(0);

    System.out.println(map.size());
  }

  private void search(int depth) {
    if (depth == k) { // 모두 뽑았으면 정수 만들기
      int total = 0;
      for (int num : result) {
        total *= (int)Math.pow(10, (int)( Math.log10(num)+1 ));
        total += num;
      }
      map.put(total, true);
      return;
    }
    // 뽑아야하는 수 고르기
    for (int i = 0; i < n; i++) {
      if (!visit[i]) {
        result[depth] = arr[i];

        visit[i] = true;
        search(depth + 1);
        visit[i] = false;
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}