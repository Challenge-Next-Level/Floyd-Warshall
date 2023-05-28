// 브루트포스로 풀어도 될까? 하면서 알고리즘 분류를 봤지만 dp를 보고 생각을 했다.
// 파이프의 길이에 대해 작은 숫자부터 채우려고 dp를 설계하니까 도저히 해결되지 않았다.
// 큰 길이 부터 생각해서 dp를 만들어 나가야 했다.
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int D = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int[] dp = new int[D + 1];
        dp[0] = Integer.MAX_VALUE;
        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());

            int length = Integer.parseInt(st.nextToken());
            int capacity = Integer.parseInt(st.nextToken());

            for (int j = D; j >= length; j--) {
                dp[j] = Math.max(dp[j], Math.min(capacity, dp[j - length]));
            }
        }

        System.out.println(dp[D]);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}