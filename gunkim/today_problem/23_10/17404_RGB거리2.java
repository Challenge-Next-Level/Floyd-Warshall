// 순환하는 배열에 대한 dp 값을 구하면 되는 문제
// 구현 문제라고 생각이 들 정도의 쉬운 dp긴 했음
import java.util.*;
import java.io.*;

public class Main {


    private int n;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        int[][] cost = new int[n + 1][3]; // 0:빨, 1:초, 2:파
        StringTokenizer st;
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            cost[i][0] = Integer.parseInt(st.nextToken());
            cost[i][1] = Integer.parseInt(st.nextToken());
            cost[i][2] = Integer.parseInt(st.nextToken());
        }

        int answer = Integer.MAX_VALUE;
        int[][] dp;
        for (int i = 0; i < 3; i++) { // 1번 집이 빨, 파, 초
            // dp 초기화
            dp = new int[n + 1][3];
            for (int j = 1; j <= n; j++) {
                Arrays.fill(dp[j], Integer.MAX_VALUE);
            }
            // 1번 집 비용
            dp[1][i] = cost[1][i];
            // 2번 집 비용
            for (int j = 0; j < 3; j++) {
                if (j == i) continue;
                dp[2][j] = dp[1][i] + cost[2][j];
            }
            // 모든 집 dp 구하기
            for (int j = 3; j <= n; j++) {
                if (j == n) {
                    if (i != 0) dp[j][0] = Math.min(dp[j - 1][1], dp[j - 1][2]) + cost[j][0];
                    if (i != 1) dp[j][1] = Math.min(dp[j - 1][0], dp[j - 1][2]) + cost[j][1];
                    if (i != 2) dp[j][2] = Math.min(dp[j - 1][0], dp[j - 1][1]) + cost[j][2];
                } else {
                    dp[j][0] = Math.min(dp[j - 1][1], dp[j - 1][2]) + cost[j][0];
                    dp[j][1] = Math.min(dp[j - 1][0], dp[j - 1][2]) + cost[j][1];
                    dp[j][2] = Math.min(dp[j - 1][0], dp[j - 1][1]) + cost[j][2];
                }
            }

            int result = Integer.MAX_VALUE;
            for (int j = 0; j < 3; j++) {
                result = Math.min(result, dp[n][j]);
            }

            answer = Math.min(answer, result);
        }


        System.out.println(answer);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}