// dp + 투 포인터
// 어려운 문제
import java.io.*;
import java.util.*;

public class Main {

  static int N, K;
  static int[] arr;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    arr = new int[N];

    st = new StringTokenizer(br.readLine());
    for(int i =0;i<N;i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    int left = 0;
    int right = 1;

    // 시작은 첫 번째 음식 하나만 먹었을 때
    int sum = arr[left];

    // dp[K] : (K-1)번째 먹이까지 최대 탈피 에너지
    long[] dp = new long[N+1];

    while(right<=N) {

      if(sum>=K) {
        while (sum >= K) {
          // sum < K가 될 때 까지 left를 1씩 증가시키기

          dp[right] = Math.max(dp[right], dp[left] + sum - K);

          sum -= arr[left];
          left++;
        }
      }
      else {
        // sum < K이므로 arr[right] 음식을 먹여야 한다.
        // right 증가
        dp[right] = Math.max(dp[right], dp[right - 1]);

        if (right == N)
          break;

        sum += arr[right];
        right++;
      }
    }

    System.out.println(dp[N]);


  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}