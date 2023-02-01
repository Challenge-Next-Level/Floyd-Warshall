//처음에 dfs로 구현하다 시간초과, 극복을 위해 백트래킹을 어느 정도 고려했으나 역시 실패
//dp인가 생각은 해보았지만 dp구현에 경우의 수가 너무 많지 않나 하고 해결법을 검색
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int[] p;
    private int result = Integer.MAX_VALUE;
    private int[] dp = new int[10001];

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        p = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            p[i] = Integer.parseInt(st.nextToken());
            dp[i] = p[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.min(dp[i], p[j] + dp[i - j]);
            }
        }
        result = Math.min(result, dp[n]);
        System.out.println(result);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}