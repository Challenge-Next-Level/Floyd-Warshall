// 부모-자식이란 관계 표현 없이 간선들을 저장해서 dp 계산시 '이전노드'에 대한 정보를 넣어줘야 함
// dp 값을 구해도 포함되는 정점 리스트를 출력해야 해서 메서드를 하나 더 만들어야 함
// 중간에 코드 구현을 살짝 잘못해서 찾는데 시간을 좀 오래 썼다 ㅠㅠ
import java.util.*;
import java.io.*;

public class Main {


    private int[][] dp;
    private ArrayList<Integer>[] bridges;
    private int[] weight;
    private int n;
    private ArrayList<Integer> answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        weight = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            weight[i] = Integer.parseInt(st.nextToken());
        }

        bridges = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            bridges[i] = new ArrayList<>();
        }
        String input = "";
        while((input = br.readLine()) != null && !input.isEmpty()) {
            st = new StringTokenizer(input);
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            bridges[from].add(to);
            bridges[to].add(from);
        }

        // 모든 정점에 대해 dp 저장
        // 0: 해당 정점을 포함하지 않는 경우
        // 1: 해당 정점을 포함한 경우
        dp = new int[2][n + 1];
        Arrays.fill(dp[0], -1);
        Arrays.fill(dp[1], -1);

        answer = new ArrayList<>();
        if (dfs(-1, 1, 0) > dfs(-1, 1, 1)) {
            findNode(-1, 1, 0);
        } else {
            answer.add(1);
            findNode(-1, 1, 1);
        }

        System.out.println(Math.max(dp[0][1], dp[1][1]));

        Collections.sort(answer);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < answer.size(); i++) {
            sb.append(answer.get(i)).append(" ");
        }
        System.out.println(sb);

    }

    public int dfs(int before, int cur, int isInclude) {
        if (dp[isInclude][cur] != -1) return dp[isInclude][cur];

        // 첫 계산이라면 0으로 초기화 후 계산 시작
        if (isInclude == 0) dp[isInclude][cur] = 0;
        else dp[isInclude][cur] = weight[cur];

        // 연결된 정점들을 포함하지 않을 때 dp 값을 계산해본다
        for (Integer to : bridges[cur]) {
            if(to == before) continue;
            dp[isInclude][cur] += dfs(cur, to, 0);
        }

        // 해당 노드가 포함되지 않을 때 자식을 포함/미포함 선택할 수 있음
        // 따라서 미포함 경우를 뺀 후 포함 경우의 dp 값을 구해와 비교를 해본다
        if (isInclude == 0) {
            for (Integer to : bridges[cur]) {
                if (to == before) continue;
                int value = dp[isInclude][cur] - dfs(cur, to, 0);
                value += dfs(cur, to, 1);
                dp[isInclude][cur] = Math.max(dp[isInclude][cur], value);
            }
        }

        return dp[isInclude][cur];
    }

    public void findNode(int before, int node, int isInclude) {
        for (Integer to : bridges[node]) {
            if (to == before) continue;
            if (isInclude == 1) {
                findNode(node, to, 0);
            } else {
                if (dp[0][to] > dp[1][to]) {
                    findNode(node, to, 0);
                } else {
                    answer.add(to);
                    findNode(node, to, 1);
                }
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}