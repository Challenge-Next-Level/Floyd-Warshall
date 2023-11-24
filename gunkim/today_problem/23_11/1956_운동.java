// 모든 노드가 어떤 사이클을 갖고 있는지 파악해야 함
// dfs와 dp로 풀어야 하는 건가...하고 시도하다 실패
// 결론은 플로이드-와샬 알고리즘이 필요했음
import java.util.*;
import java.io.*;

public class Main {


    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        // i에서 j로 가는 비용 초기화
        int[][] dp = new int[v + 1][v + 1];
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                if(i != j)
                    dp[i][j] = Integer.MAX_VALUE;
            }
        }

        // 입력 값으로 배열을 초기화
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            dp[from][to] = dist;
        }

        // 플로이드 와샬 알고리즘
        for (int i = 1; i <= v; i++) { // 경유하는 노드
            for (int j = 1; j <= v; j++) { // 시작 노드
                for (int k = 1; k <= v; k++) { // 도착 노드
                    if (k == j) continue;
                    // 이 조건을 추가하지 않으면 아래 조건에서 연산시 overflow 발생으로 원치 않는 결과를 얻을 수 있다
                    if (dp[j][i] == Integer.MAX_VALUE || dp[i][k] == Integer.MAX_VALUE) continue;

                    if (dp[j][k] > dp[j][i] + dp[i][k]) {
                        dp[j][k] = dp[j][i] + dp[i][k];
                    }
                }
            }
        }

        answer = Integer.MAX_VALUE;
        // 사이클이 생기는 구간 중 최솟값 구하기
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                if (i == j) continue;
                // 서로 갈 수 있다면 사이클이 존재한다는 의미이다
                if (dp[i][j] != Integer.MAX_VALUE && dp[j][i] != Integer.MAX_VALUE) {
                    answer = Math.min(answer, dp[i][j] + dp[j][i]);
                }
            }
        }

        if (answer == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}