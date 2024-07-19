import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int T;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            int[] files = new int[N + 1];
            int[] sum = new int[N + 1];
            int[][] dp = new int[N + 1][N + 1];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                files[j] = Integer.parseInt(st.nextToken());
                sum[j] = sum[j - 1] + files[j];
            }

            for (int n = 1; n <= N; n++) {
                for (int from = 1; from + n <= N; from++) {
                    int to = from + n;
                    dp[from][to] = Integer.MAX_VALUE;
                    for (int divide = from; divide < to; divide++) {
                        dp[from][to] = Math.min(dp[from][to], dp[from][divide] + dp[divide + 1][to] + sum[to] - sum[from - 1]);
                    }
                }
            }

            System.out.println(dp[1][N]);
        }

    }



}