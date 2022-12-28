import java.util.*;
import java.io.*;

public class Main {

    public class Bridge implements Comparable<Bridge> {
        private int start;
        private int end;
        private int cost;

        public Bridge(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Bridge o) {
            return this.cost - o.cost;
        }
    }

    public int find(int node, int[] parent) {//최종 root node를 찾아 반환
        if (parent[node] == node) return node;
        parent[node] = find(parent[node], parent);
        return parent[node];
    }

    public void union(int node1, int node2, int[] parent, int[] rank) {//두 개의 트리를 합친다.
        int root1 = find(node1, parent);
        int root2 = find(node2, parent);

        if (root1 != root2) { //높이가 작은 트리를 높이가 튼 크리에 붙인다.
            if (rank[root1] > rank[root2]) {
                parent[root2] = root1;
            } else {
                parent[root1] = root2;
                if (rank[root1] == rank[root2]) rank[root2] += 1; //두 개의 트리 모두 높이가 같다면 한 쪽을 높여서 붙인다.
            }
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) { //입력은 여러개의 테스트케이스로 구분되어 있음. m,n이 모두 0일 때 테스트 종료
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            if (m == 0 && n == 0) {
                break;
            }

            List<Bridge> bridges = new ArrayList<>();
            int totalCost = 0; //모든 간선의 가중치 합 저장
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int z = Integer.parseInt(st.nextToken());

                bridges.add(new Bridge(x, y, z));
                totalCost += z;
            }

            bridges.sort(Bridge::compareTo);//간선의 가중치 순으로 정렬

            int[] parent = new int[m];//나의 최종 root node를 저장
            int[] rank = new int[m];//내가 속한 tree의 높이(rank)를 저장
            for (int i = 0; i < m; i++) {
                parent[i] = i;//자기 자신으로 초기화
                rank[i] = 0;//0으로 초기화
            }

            int mstCost = 0;//최소신장트리(MST)의 cost
            for (int i = 0; i < n; i++) {//MST 만들기
                Bridge bridge = bridges.get(i);

                if (find(bridge.start, parent) != find(bridge.end, parent)) { //두 노드의 root node가 다르다면 union
                    union(bridge.start, bridge.end, parent, rank);
                    mstCost += bridge.cost;//간선 비용 추가
                }
            }
            System.out.println(totalCost - mstCost);

        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}