// 특정 노드에 dp 값을 어떻게 산출할 수 있을까에 대한 어려움이 많았음
// 특정 노드의 dp값은 자식 노드의 dp값의 합이다 라고 생각하기
import java.util.*;
import java.io.*;

public class Main {

    private int[][] dp;
    private int[] ability;
    private ArrayList<Integer>[] bridges;
    private int n;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        bridges = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            bridges[i] = new ArrayList<>();
        }

        // 사수, 부사수 관계를 저장 (부모 노드에 자식 노드들을 저장)
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 2; i <= n; i++) {
            int parent = Integer.parseInt(st.nextToken());
            bridges[parent].add(i);
        }

        // 판매원의 실력 저장
        ability = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            ability[i] = Integer.parseInt(st.nextToken());
        }

        // 0: 부모 노드와 시너지 형성 하지 않은 경우
        // 1: 부모 노드와 시너지 형성한 경우
        dp = new int[n + 1][2];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i], -1);
        }

        // 루트 노드는 부모가 없기 때문에 isBind는 0으로 고정
        int answer = dfs(1, 0);

        System.out.println(answer);
    }


    public int dfs(int cur, int isBind) {
        if (dp[cur][isBind] != -1) return dp[cur][isBind];

        dp[cur][isBind] = 0;
        // 현재 노드를 자식 노드와 연결하지 않은 경우
        for (Integer next : bridges[cur]) {
            dp[cur][isBind] += dfs(next, 0); // 그럼 자식 노드들의 dp값을 모두 더하면 된다
        }

        // 현재 노드가 부모 노드와 시너지 형성을 안한경우
        if (isBind == 0) {
            int value = dp[cur][isBind];
            // 자식 노드와 시너지 형성을 생각해본다
            for (Integer next : bridges[cur]) {
                int num = value - dfs(next, 0); // 해당 자식과 시너지를 맺으면 위에서 더한 자식의 dp값을 우선 뺀다
                num += dfs(next, 1) + (ability[cur] * ability[next]); // 자식 노드와의 시너지 형성값을 더한다
                dp[cur][isBind] = Math.max(dp[cur][isBind], num);
            }
        }

        return dp[cur][isBind];
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}