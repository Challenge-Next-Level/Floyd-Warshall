// dp라고 생각했다. 2차원 배열을 통해 풀어야 되나?라는 접근까지 했지만 '건너뛰는 점프의 수'에 대한 메모리 비용이 상당히 커 아니라 판단했다
// dp값을 만들 때 '최소 카운트 수'와 '이전 점프'를 기록하는 Info 클래스를 만들어 저장하며 dp값을 정해나갔다
// 제출시 80%을 찍고 틀렸습니다를 보았고 다른 분의 풀이를 보았다
// 2차원 배열을 이용하여 dp값을 만들어나가는 것이었고 메모리 비용을 줄이기 위해 범위를 계산하는 묘수가 필요했다
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        boolean[] isSmall = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(br.readLine());
            isSmall[x] = true;
        }

        // 불필요한 메모리, 연산을 최소화하기 위해 범위를 제한할 필요가 있다
        // 등차수열의 합공식을 이용해 가장 빠르게 갈 수 있는 최적의 카운트를 계산한다
        // n(2a + (n-1)d) / 2 = Sn
        // 이를 n에 대해 정리하면 n = root(2 Sn - n) 이다.
        // n이 어떤 값이든 위 식은 결국 n <= root(2 Sn) 를 만족한다.
        // Sn은 등차수열 합의 결과값이니 문제로 따졌을때 도착지점이라 봐도 무방하다. 따라서 아래와 같은 range를 만들 수 있다
        int range = (int) Math.sqrt(2 * n);

        int[][] dp = new int[n + 1][range + 2]; // +2 까지 하는 이유: 뒤에서 계산을 편하게 하기위해
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= range + 1; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[1][0] = 0;

        // 각 지점의 dp값을 구한다
        for (int i = 2; i <= n; i++) {
            // 도착 못하는 곳이라면 continue
            if (isSmall[i]) continue;

            for (int j = 1; j <= range; j++) { // 해당 지점에 1 ~ range 만큼의 건너뛰기로 올 수 있다
                if (i - j <= 0) break;
                dp[i][j] = Math.min(Math.min(dp[i - j][j - 1], dp[i - j][j]), dp[i - j][j + 1]);
                if (dp[i][j] != Integer.MAX_VALUE) dp[i][j]++;
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int i = 1; i <= range; i++) {
            answer = Math.min(answer, dp[n][i]);
        }

        if (answer == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}