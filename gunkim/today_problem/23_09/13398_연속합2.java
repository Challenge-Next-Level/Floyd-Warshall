// dp를 생각해 접근 및 시도는 잘 했는데 너무 돌아가는 해결법으로 풀었었음. 결국 시간초과
// 아래와 같이 간단하게 풀면 되는 거였음...
import java.util.*;
import java.io.*;

public class Main {


    private static int n;
    private static int[] nums;
    private static int[][] dp;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[2][n];
        dp[0][0] = dp[1][0] = nums[0];

        int answer = nums[0];
        for (int i = 1; i < n; i++) {
            dp[0][i] = Math.max(dp[0][i - 1] + nums[i], nums[i]);
            dp[1][i] = Math.max(dp[1][i - 1] + nums[i], dp[0][i - 1]);

            answer = Math.max(answer, Math.max(dp[0][i], dp[1][i]));
        }

        System.out.println(answer);

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}