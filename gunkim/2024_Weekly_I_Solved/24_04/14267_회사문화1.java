// 질문 게시판의 힌트가 도움됨
// 한 직원은 여러번 칭찬받을 수 있습니다
import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int m;
    private int[] parent;
    private List<Integer>[] child;
    private int[] compliment;
    private int[] dp;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        child = new List[n + 1];
        for (int i = 0; i < n + 1; i++) {
            child[i] = new ArrayList<Integer>();
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            int p = Integer.parseInt(st.nextToken());
            parent[i] = p;
            if (p == -1) continue;
            child[p].add(i);
        }

        compliment = new int[n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int child = Integer.parseInt(st.nextToken());
            int score = Integer.parseInt(st.nextToken()); // 최소 1이상
            compliment[child] += score; // 딱 이곳만 수정했음
        }

        dp = new int[n + 1];
        bfs();

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(dp[i]).append(" ");
        }

        System.out.println(sb);

    }

    private void bfs() {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(1); // root 부터 시작

        while (!dq.isEmpty()) {
            int node = dq.pollFirst();

            for (int i = 0; i < child[node].size(); i++) {
                int ch = child[node].get(i);

                dp[ch] = dp[node] + compliment[ch];
                dq.add(ch);

            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}