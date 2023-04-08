import java.util.*;
import java.io.*;

public class Main {

  private int[] location;
  private int n;

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    int m = Integer.parseInt(br.readLine());
    location = new int[m];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      location[i] = Integer.parseInt(st.nextToken());
    }

    int left = 0, right = n;
    int answer = Integer.MAX_VALUE;
    while (left <= right) {
      int mid = (left + right) / 2;
      if(possible(mid)) {
        answer = mid;
        right = mid - 1;
      }
      else
        left = mid + 1;
    }

    System.out.println(answer);

  }

  boolean possible(int target) {
    int prev = 0; // 이전 가로등이 비춘 마지막 지점, 0 지점부터 모두 비춰주어야 하기 때문에 0부터 시작

    for (int i = 0; i < location.length; i++) {
      if (location[i] - target <= prev) {
        prev = location[i] + target;
      } else {
        return false;
      }
    }
    return n - prev <= 0;
  }

  public static void main(String[] args) throws Exception {
    new Main().solution();

  }

}