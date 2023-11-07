// n값이 커서 단순 for문 해결은 당연히 아니라 생각했다
// 숫자가 갖을 수 있는 가장 큰 항을 찾아 dp에 저장하면 될 것 같아 binary search + dp를 이용했다
// 그러나 '시간초과'
// 문제에서 묻는 '항의 갯수'를 dp에 저장하는 것이 맞는 방법이었고 아래와 같이 반복문을 특별하게 이용해 dp를 찾는 것이 답이었다
// 처음 풀이 방법이 해답이 아니란게 조금 아쉽다
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int[] dp;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            dp[i] = i; // 초기화(중요 부분인 것 같음)
            for (int j = 1; j * j <= i; j++) {
                if (dp[i] > dp[i - j * j] + 1) {
                    dp[i] = dp[i - j * j] + 1;
                }
            }

        }

        System.out.println(dp[n]);

    }




    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}