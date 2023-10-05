// 완전 수학 문제라 생각한다
// 해당 공식이 왜 그런지 증명도 체크해야 할 것 같다
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 입력값의 최대는 20,000
        int[] dp = new int[20001];

        // 1! ~ 4! 까지 값을 미리 저장
        dp[0] = dp[1] = 1;
        dp[2] = 2;
        dp[3] = 6;
        dp[4] = 4;

        for (int i = 5; i <= N; i++) {
            // 목표 숫자가 5의 배수라면, 구하고자 하는 맨 뒷자리 수는 (2^a) * a! 이다.
            // 여기서 a는 목표 숫자를 5로 나눈 몫이다.
            if (i % 5 == 0) {
                int a = i / 5;
                // 여기서 2의 a제곱을 축약해 계산하고 있는데 이는 2의 제곱이 {2, 4, 8, 6}으로 반복되기 때문
                // 대신 6은 실제로 2^0 = 1 로 계산되어 1이 곱해지는 형태인데
                // dp값(짝수로 이루어짐)과 6을 곱하면 똑같이 dp값이 나오기 때문에 1을 곱하는 것과 같다.
                dp[i] = ((int) Math.pow(2, a % 4) * dp[a]) % 10; // 공식 사용.
            } else { // 목표 숫자가 5의 배수가 아닐 때
                int before = (i / 5) * 5; // i보다 작은 최대 5의 배수를 구함.
                int total = 1;
                // 예로 목표 숫자가 12라면 total = 12 * 11 이다.
                for (int j = i; j > before; j--) {
                    total *= (j % 10);
                }
                // dp[10]과 곱하면 되는 것
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