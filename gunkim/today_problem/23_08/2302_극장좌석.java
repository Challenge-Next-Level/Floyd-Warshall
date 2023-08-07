// dp라는건 바로 직감하고 풀어보았다. 그리고 노가다를 통해 피보나치라는 것을 알아냈다.
// 그렇게 문제를 풀다가 틀려 질문게시판에서 "모든 좌석이 vip인 경우는 0이다"라는 말을 믿고 구현을 했는데 틀렸다.
// 다른 분의 풀이를 보니 1이 맞았다.
// 근데 다른 분의 풀이가 너무 깔끔해 참고하여 풀게 되었다.
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[] dp = new int[41];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        // n까지 dp값을 계산해 놓는다. 고정석이 없을 경우는 dp[n]까지 사용될 것이기 때문
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        int answer = 1;
        int beforeIdx = 0;
        // answer에 곱할 수를 계산하면 되는데 적절한 뺄셈을 통해 구간의 갯수를 알아내면 된다.
        for (int i = 0; i < m; i++) {
            int location = Integer.parseInt(br.readLine());
            answer *= dp[location - beforeIdx - 1];
            beforeIdx = location;
        }
        answer *= dp[n - beforeIdx];

        System.out.println(answer);


    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}