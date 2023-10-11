// 정말 보편적으로 유명한 배낭 문제이다. dp 맞다
// 그런데 난 아직도 새롭다... 이해하는데도 시간이 걸렸다.
// 점화식을 그냥 바로 세워버리는 방법이 나에겐 가장 편한 길인 것 같다
// 여러 개의 경우를 하나씩 채워가면서 패턴을 찾는게 아니라 그냥 첫 값을 채울 때 바로 점화식을 세우는게 최고다
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int k;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] w = new int[n + 1];
        int[] v = new int[n + 1];
        int[][] dp = new int[n + 1][k + 1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            w[i] = Integer.parseInt(st.nextToken());
            v[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - w[i] >= 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
                }
            }
        }

        System.out.println(dp[n][k]);

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}