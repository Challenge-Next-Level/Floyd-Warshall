// MST(최소 스패닝 트리)가 만들어지지 않는 경우도 생각해야 한다!
import java.io.*;
import java.util.*;

public class Main {


    private int[] parent;
    private int[] rank;
    private List<Bridge> bridges;
    private char[] schools;
    private int n;
    private int m;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        schools = new char[n + 1];
        for (int i = 1; i <= n; i++) { // 노드 저장
            schools[i] = st.nextToken().charAt(0);
        }

        bridges = new ArrayList<>();
        for (int i = 0; i < m; i++) { // 간선 저장
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            if (schools[from] != schools[to])
                bridges.add(new Bridge(from, to, cost));
        }

        Collections.sort(bridges); // 간선 정렬

        parent = new int[n + 1];
        rank = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }

        int answer = 0;
        for (int i = 0; i < bridges.size(); i++) { // 비용이 작은 간선 부터 union-find 진행
            int from = bridges.get(i).from;
            int to = bridges.get(i).to;
            if (find(from) != find(to)) {
                union(from, to);
                answer += bridges.get(i).cost;
            }
        }

        // parent 배열을 설정(?)하기 위해 모든 노드에 대해 find 진행
        for (int i = 1; i <= n; i++) {
            find(i);
        }

        // 모든 노드가 같은 root 노드를 갖고 있지 않다면 MST(최소 스패닝 트리)가 만들어지지 않은 것
        for (int i = 1; i < n; i++) {
            if (parent[i] != parent[i + 1]) {
                System.out.println(-1);
                return;
            }
        }
        System.out.println(answer);

    }

    public void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (rank[root1] > rank[root2]) {
            parent[root2] = root1;
        } else {
            parent[root1] = root2;
            if (rank[root1] == rank[root2]) {
                rank[root2]++;
            }
        }
    }

    public int find(int node) {
        if (node != parent[node]) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    public class Bridge implements Comparable<Bridge> {
        private int from;
        private int to;
        private int cost;

        public Bridge(int from, int to, int cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Bridge o) {
            return this.cost - o.cost;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}