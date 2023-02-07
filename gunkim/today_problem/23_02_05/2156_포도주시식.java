//첫 번째, dp[3] 계산시 nums[1] + nums[2] 생각을 못했음
//두 번째, dp[i] 계산시 dp[i - 1] 생각을 못했음
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        if (n <= 2) {
            System.out.println(Arrays.stream(nums).sum());
        } else {
            int[] dp = new int[n + 1];
            dp[1] = nums[1];
            dp[2] = nums[1] + nums[2];
            dp[3] = Integer.max(nums[1] + nums[3], Integer.max(nums[1] + nums[2], nums[2] + nums[3]));
            for (int i = 4; i <= n; i++) {
                dp[i] = Integer.max(dp[i - 1], Integer.max(dp[i - 2] + nums[i], dp[i - 3] + nums[i - 1] + nums[i]));
            }

            System.out.println(dp[n]);
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}