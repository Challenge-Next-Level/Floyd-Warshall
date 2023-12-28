// LCS 보다 쉬운 문제
// 간단하게 dp를 활용하면 풀 수 있는 문제였다
import java.io.*;
import java.util.*;

public class Main {

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    String t = br.readLine();

    int answer = 0;

    // 0번 째 열과 행은 비워두기 위해 넉넉히 공간 할당
    int[][] dp = new int[t.length() + 1][s.length() + 1];

    for (int i = 1; i <= t.length(); i++) {
      char wordT = t.charAt(i - 1);
      for (int j = 1; j <= s.length(); j++) {
        char wordS = s.charAt(j - 1);

        if (wordS != wordT) {
          dp[i][j] = 0;
        } else {
          dp[i][j] = dp[i - 1][j - 1] + 1;
          answer = Math.max(answer, dp[i][j]);
        }
      }
    }

    System.out.println(answer);
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}