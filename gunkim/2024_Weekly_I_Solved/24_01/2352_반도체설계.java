// LIS(가장 긴 증가하는 부분 수열) 문제인데 일반 DP에 '이분 탐색'을 곁들이면 더 좋은 풀이를 만들 수 있었다
// 아무리 생각해도 이분 탐색을 어디에 적용 할 수 있는지 알수 없었고 풀이를 검색했다
// 일반 dp를 이용하면 o(n^2) 의 시간이 걸리지만 이를 최적화할 수 있는 것이다
// 관련 개념을 적용하는데 시간이 조금 걸렸다
import java.io.*;
import java.util.*;

public class Main {

  private int[] dp;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];

    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i=0; i<n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    dp = new int[n+1];
    int len =0;
    int idx =0;
    for(int i=0; i<n; i++) {
      if(arr[i]> dp[len]) {
        dp[++len] = arr[i];
      }else {
        idx = binarySearch(0, len, arr[i]);
        // System.out.println(idx);
        dp[idx] = arr[i];
      }
    }
    System.out.println(len);
  }

  int binarySearch(int left, int right, int key) {
    // System.out.println(left + " : " + right + " : " + key);
    int mid =0;
    while(left<right) {
      mid = (left+right)/2;
      if(dp[mid] < key) {
        left = mid+1;
      }else {
        right = mid;
      }
    }
    return right;
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}