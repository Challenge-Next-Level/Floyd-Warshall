//최대크기의 정사각형을 만들 수 있다는 규칙을 발견해서 점화식을 세우는 것이 관건이었지만 너무 어려웠다
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] board = new int[m][n];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] dp = new int[m + 1][n + 1];
        int answer = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (board[i - 1][j - 1] == 0) {//장애물이 없다면
                    dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
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