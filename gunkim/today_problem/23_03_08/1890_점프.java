//dp 냄새가 풍겼지만 도저히 해결책이 떠오르지 않아 내 옛날 풀이(아마 이것도 참고했을거)를 보았다
//경우의 수가 2^63-1 까지 나올 수 있어 int 자료가 아닌 long으로 해야 풀 수 있었다
import java.util.*;
import java.io.*;

public class Main {

    int[][] dir = {{1, 0}, {0, 1}};
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] board = new int[n][n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long[][] dp = new long[n][n];
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == n - 1 && j == n - 1) break;
                int jump = board[i][j];
                if (i + jump < n) {
                    dp[i + jump][j] += dp[i][j];
                }
                if (j + jump < n) {
                    dp[i][j + jump] += dp[i][j];
                }
            }
        }

        System.out.println(dp[n - 1][n - 1]);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}