// 단순 dfs로 풀면 시간 초과가 발생. 역시나 dp... 문제다
// 간단한 예로 dp 값을 어떻게 찾으면 될지 설명하자면,
// 만약 2번을 건너 뛰어 n위치에 도달한 dp 값을 구하고 싶을 때
// 1. (n-1 번째에서 2번 건너뛴 dp 값) + (n-1에서 n까지 거리)
// 2. (n-2 번째에서 1번 건너뛴 dp 값) + (n-2에서 n까지 거리)
// 3. (n-3 번째에서 0번 건너뛴 dp 값) + (n-3에서 n까지 거리)
// 위 경우를 비교한 최소값을 dp로 정하면 된다.
import java.io.*;
import java.util.*;

public class Main {

    private int n;
    private int k;
    private int answer;
    private Coordinate[] coordinates;
    private int[][] dp;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        coordinates = new Coordinate[n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            coordinates[i] = new Coordinate(y, x);
        }

        // dp 초기화
        dp = new int[n + 1][k + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < k + 1; j++) {
                dp[i][j] = -1;
            }
        }

        dfs(n, k);

        System.out.println(dp[n][k]);
    }

    public int dfs(int idx, int count) {
        // 출발지 dp 값은 무조건 0
        if (idx == 1) return 0;
        if (dp[idx][count] != -1) return dp[idx][count];

        // 가장 최소 거리를 dp에 저장해야 함
        int minDist = Integer.MAX_VALUE;

        for (int i = 0; i <= k; i++) { // 0 ~ k개 건너뛰었다는 가정하에 dp 계산
            // i : 건너뛴 노드 수
            int beforeIdx = idx - 1 - i;
            if (beforeIdx < 1 || count - i < 0) break;
            Coordinate beforeNode = coordinates[beforeIdx];
            Coordinate currentNode = coordinates[idx];
            int distance = Math.abs(beforeNode.x - currentNode.x) + Math.abs(beforeNode.y - currentNode.y);
            minDist = Math.min(minDist, dfs(beforeIdx, count - i) + distance);
        }

        dp[idx][count] = minDist;
        return minDist;
    }


    public class Coordinate {
        private int y;
        private int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}