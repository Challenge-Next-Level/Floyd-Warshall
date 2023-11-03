// longest common subsequence에 대해 찾아보았고 dp풀이로 이해했음
// 그런데 3개는 어떻게 해야하지? 라는 생각에 3차원으로 생각하니 dp가 가능한걸까? 해서 어려웠음
// 실제 구글링을 해도 이미지화 시킨 설명은 찾아볼 수 없음. 그냥 단순하게 2차원이랑 같이 생각만 하면 될듯
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();
        String s3 = br.readLine();

        int[][][] dp = new int[s1.length() + 1][s2.length() + 1][s3.length() + 1];

        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                for (int k = 0; k < s3.length(); k++) {
                    if (s1.charAt(i) == s2.charAt(j) && s1.charAt(i) == s3.charAt(k)) {
                        dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1;
                    } else {
                        dp[i + 1][j + 1][k + 1] = Math.max(Math.max(dp[i][j + 1][k + 1], dp[i + 1][j][k + 1]), dp[i + 1][j + 1][k]);
                    }
                }
            }
        }

        System.out.println(dp[s1.length()][s2.length()][s3.length()]);
    }




    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}