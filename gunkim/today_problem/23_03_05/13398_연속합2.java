import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int[] nums;
    private int[][] dp;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[n][2]; // i: 해당 i번 째 수, j: 수를 제거한 적이 있는지 여부
        dp[0][0] = dp[0][1] = nums[0]; // 수는 한 개 이상 선택해야 되기 때문

        int answer = nums[0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 1][0] + nums[i], nums[i]);
            dp[i][1] = Math.max(dp[i - 1][1] + nums[i], dp[i - 1][0]);

            answer = Math.max(answer, Math.max(dp[i][0], dp[i][1]));
        }

        System.out.println(answer);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}