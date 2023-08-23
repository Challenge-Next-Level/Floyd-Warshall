// 핵심은 MST(최소 스패닝 트리)를 만들면 되는 거였음
// 간선 정보를 저장한 뒤 정렬하여 find, union 과정을 거쳐 total cost를 구하면 된다
// 하지만 간선 정보를 단순히 for 문 2개를 통해 저장하면 '메모리 초과'가 발생한다
// n이 최대 100,000이 될 수 있기 때문
// 따라서 간선을 x, y, z 각각 따로 정렬/비교를 통해 간선을 저장해야 한다
// 감(?)으로 이해해야 하지만 바로 옆 노드끼리만 비교를 하는 이유는 해당 간선 정보만으로 '최소 스패닝 트리'가 완성되는 것이 자명하기 때문
import java.io.*;
import java.util.*;

public class Main {


    private int[] parent;
    private int[] rank;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Node[] nodes = new Node[n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            nodes[i] = new Node(i, x, y, z);
        }

        // n개의 노드들을 n-1개의 간선을 이용해 연결하면 최소 비용이 나올 것
        // '최소 스패닝 트리'를 만들기 위해 간선들에 대한 정보를 저장
        ArrayList<Bridge> bridges = new ArrayList<>();

        // x, y, x 각각의 좌표들끼리 정렬 및 비교
        Arrays.sort(nodes, (n1, n2) -> n1.x - n2.x);
        for (int i = 0; i < n - 1; i++) {
            int cost = Math.abs(nodes[i].x - nodes[i + 1].x);
            bridges.add(new Bridge(nodes[i].num, nodes[i + 1].num, cost));
        }

        Arrays.sort(nodes, (n1, n2) -> n1.y - n2.y);
        for (int i = 0; i < n - 1; i++) {
            int cost = Math.abs(nodes[i].y - nodes[i + 1].y);
            bridges.add(new Bridge(nodes[i].num, nodes[i + 1].num, cost));
        }

        Arrays.sort(nodes, (n1, n2) -> n1.z - n2.z);
        for (int i = 0; i < n - 1; i++) {
            int cost = Math.abs(nodes[i].z - nodes[i + 1].z);
            bridges.add(new Bridge(nodes[i].num, nodes[i + 1].num, cost));
        }

        // 위에서 노드 사이에 간선이 여러개 들어가면 뭔가 이상해질 것 같죠?
        // union시 어차피 연결된 node는 건너뛰게 된다.

        // 간선들을 가중치가 낮은 것부터 사용하기 위해 정렬한다
        // 이렇게 가중치가 낮은 간선은 우선적으로 사용하는 알고리즘을 일명 '크루스칼 알고리즘'이라고도 한다.
        Collections.sort(bridges);

        // 내가 속한 트리의 root 노드 번호
        parent = new int[n];
        // 내가 속한 트리의 높이
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }

        int total = 0;
        for (int i = 0; i < bridges.size(); i++) {
            int node1 = bridges.get(i).from;
            int node2 = bridges.get(i).to;
            if (find(node1) != find(node2)) {
                union(node1, node2);
                total += bridges.get(i).cost;
            }
        }

        System.out.println(total);

    }

    public void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);

        if (rank[root1] > rank[root2]) {
            parent[root2] = root1;
        } else {
            parent[root1] = root2;
            if (rank[root1] == rank[root2]) rank[root2]++;
        }
    }

    public int find(int node) { // 해당 노드가 속한 트리의 root 노드를 찾는다
        if (parent[node] != node) {
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


    public class Node {
        private int num;
        private int x;
        private int y;
        private int z;

        public Node(int num, int x, int y, int z) {
            this.num = num;
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}