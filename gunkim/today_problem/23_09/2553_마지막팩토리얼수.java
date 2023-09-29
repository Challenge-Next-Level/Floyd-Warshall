// 완전 수학 문제라 생각한다
// 해당 공식이 왜 그런지 증명도 체크해야 할 것 같다
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[20001];
        dp[0] = dp[1] = 1;
        dp[2] = 2;
        dp[3] = 6;
        dp[4] = 4;

        for (int i = 5; i <= N; i++) {
            if (i % 5 == 0) {
                int q = i / 5;
                dp[i] = ((int) Math.pow(2, q % 4) * dp[q]) % 10; // 공식 사용.
            } else {
                int before = (i / 5) * 5; // i보다 작은 최대 5의 배수를 구함.
                int total = 1;
                for (int j = i; j > before; j--) {
                    total *= (j % 10);
                }
                total *= dp[before];
                dp[i] = total % 10;
            }
        }

        System.out.println(dp[N]);
    }




    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}