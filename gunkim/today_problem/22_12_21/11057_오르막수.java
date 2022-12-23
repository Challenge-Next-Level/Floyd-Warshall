import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] dp = new int[n + 1][11];
        for (int i = 1; i < 11; i++) {
            dp[1][i] = 1;
        }
        int num = 2;
        while (num <= n) {
            for (int i = 1; i < 11; i++) {
                dp[num][i] = (dp[num][i - 1] + dp[num - 1][i]) % 10007;
            }
            num++;
        }
        int answer = 0;
        for (int i = 1; i < 11; i++) {
            answer += dp[n][i];
        }
        System.out.println(answer % 10007);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}