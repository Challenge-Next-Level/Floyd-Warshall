// 편집 거리 알고리즘 : dp를 이용한 문제
import java.io.*;
import java.util.*;

public class Main {
  private int n;
  private int m;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    String request = br.readLine();
    String answer = br.readLine();

    int[][] dp = new int[n + 1][m + 1]; // dp 초기 세팅하기
    for (int i = 1; i <= m ; i++) {
      dp[0][i] = dp[0][i - 1] + 1;
    }
    for (int i = 1; i <= n ; i++) {
      dp[i][0] = dp[i - 1][0] + 1;
    }

    for (int i = 1; i <= n ; i++) { // 문자열의 문자를 탐색하며 비교
      for (int j = 1; j <= m ; j++) {
        char A = request.charAt(i - 1);
        char B = answer.charAt(j - 1);

        int minVal = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
        if (A == B || (A == 'i' && B == 'j') || (A == 'i' && B == 'l') || (A == 'v' && B == 'w')) { // 문자가 같다면
          dp[i][j] = dp[i - 1][j - 1]; // 해당 2개의 문자를 비교하기 전 dp 값을 그대로 가져온다
        } else { // 문자가 다르다면
          dp[i][j] = minVal + 1; // dp의 최소 값을 가져와 +1
        }
      }
    }

    System.out.println(dp[n][m]);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}