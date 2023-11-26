package org.example;


import java.io.*;
import java.util.*;

public class Main {

  private String answer;
  private String devil;
  private String angel;
  private int answerLen;
  private int bridgeLen;
  private int count;

  public static final int ANGEL = 0, DEVIL = 1;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    answer = br.readLine();
    devil = br.readLine();
    angel = br.readLine();

    answerLen = answer.length();
    bridgeLen = devil.length();

    count = 0;

    for (int select = 0; select <= 1; select++) {
      int[][] cnt = new int[answerLen + 1][bridgeLen + 1];
      Arrays.fill(cnt[0], 1);
      for (int i = 1; i <= answerLen; i++) {
        String cur;
        if (i == 1) cur = devil;
        else cur = angel;

        for (int j = 1; j <= cur.length(); j++)
          cnt[i][j] = cnt[i][j - 1] + (cur.charAt(j - 1) == answer.charAt(i - 1) ? cnt[i - 1][j - 1] : 0);
      }
      count += cnt[answerLen][bridgeLen];
    }
    System.out.println(count);

    // int[][][] dp = new int[2][bridgeLen][answerLen];
    //
    //
    // if (angel.charAt(0) == answer.charAt(0)) dp[ANGEL][0][0] = 1;
    // if (devil.charAt(0) == answer.charAt(0)) dp[DEVIL][0][0] = 1;
    //
    // for (int i = 1; i < bridgeLen; i++) { // 다리 시작 위치
    //
    //   if (angel.charAt(i) == answer.charAt(0)) dp[ANGEL][i][0] = dp[ANGEL][i - 1][0] + 1;
    //   else dp[ANGEL][i][0] = dp[ANGEL][i - 1][0];
    //   for (int j = 1; j < answerLen; j++) {
    //     if (angel.charAt(i) == answer.charAt(j)) dp[ANGEL][i][j] = dp[ANGEL][i - 1][j] + dp[DEVIL][i - 1][j - 1];
    //     else dp[ANGEL][i][j] = dp[ANGEL][i - 1][j];
    //   }
    //
    //   if (devil.charAt(i) == answer.charAt(0)) dp[DEVIL][i][0] = dp[DEVIL][i - 1][0] + 1;
    //   else dp[DEVIL][i][0] = dp[DEVIL][i - 1][0];
    //   for (int j = 1; j < answerLen; j++) {
    //     if (devil.charAt(i) == answer.charAt(j)) dp[DEVIL][i][j] = dp[DEVIL][i - 1][j] + dp[ANGEL][i - 1][j - 1];
    //     else dp[DEVIL][i][j] = dp[DEVIL][i - 1][j];
    //   }
    //
    // }
    //
    // int answer = dp[ANGEL][bridgeLen - 1][answerLen - 1] + dp[DEVIL][bridgeLen - 1][answerLen - 1];
    System.out.println(answer);
  }



  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}