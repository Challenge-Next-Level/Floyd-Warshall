//dp로 접근은 했지만 m개를 사용한다는 점에서 생각해낼 수 없었음
//해결법을 찾은 후 말이 안될정도로 어려운 아이디어라 생각함
//만들 수 있는 가지수가 많아 자료형 저장을 int가 아닌 long으로 해야 한다
import java.util.*;
import java.io.*;

public class Main {

    private int t;
    private long[][] dp = new long[1001][1001];
    private int result = 0;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        dp[1][1] = 1;
        dp[2][1] = 1;
        dp[2][2] = 1;
        dp[3][1] = 1;
        dp[3][2] = 2;
        dp[3][3] = 1;
        for (int i = 4; i <= 1000; i++) {
            for (int j = 2; j <= i; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % 1000000009;
            }
            dp[i][i] = 1;//실수로 생각안할 수 있는 부분
        }
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            long count = 0;
            for (int j = 1; j <= m; j++) {
                count = (count + dp[n][j]) % 1000000009;
            }
            System.out.println(count);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}