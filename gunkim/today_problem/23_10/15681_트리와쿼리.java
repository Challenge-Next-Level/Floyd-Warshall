// 문제가 너무 길고 무슨 말을 하는 지 몰랐지만 차분히 읽어 보고 해결
// 결국 서브 쿼리 즉, 해당 노드 아래로 모든 자식 노드의 수를 반환하면 됐음
// 트리를 순회하며 dp 값으로 자식의 수를 저장했음
import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int[] dp;
    static boolean[] visit;
    static List<Integer>[] list;


    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 노드 수
        int root = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        visit = new boolean[n + 1];
        list = new List[n + 1];
        for (int i = 0; i < n + 1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            list[nodeA].add(nodeB);
            list[nodeB].add(nodeA);
        }

        // 각 노드가 몇 개의 자식을 갖고있는지 dp를 구한다
        dp = new int[n + 1];
        findChildNode(root);

        for (int i = 0; i < q; i++) {
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp[num]);
        }

    }

    static int findChildNode(int node) {
        int cnt = 0;
        visit[node] = true;

        for (Integer child : list[node]) {
            if (visit[child]) continue;
            cnt += findChildNode(child);
        }

        if (cnt == 0) dp[node] = 1;
        else dp[node] = cnt + 1;
        return dp[node];
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}