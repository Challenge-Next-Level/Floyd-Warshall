// 고전적인 다익스트라 문제이지만 한 가지 고려를 해야 함
// '최적의 해'를 구하기 위해선 경로가 같을 때도 체크를 한 번 해야했음
// 이 문제를 풀기 전 22868(산책 small)을 푸는걸 추천한다
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int m;
    private ArrayList<Node>[] nodes;
    private int start;
    private int end;
    private boolean[] visit;
    private int[] beforeNode;
    private int[] distance;
    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nodes = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            nodes[nodeA].add(new Node(nodeB, cost));
            nodes[nodeB].add(new Node(nodeA, cost));
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        // 입력 받은 경로를 정렬한다 -> 사전순 경로를 찾는데 최적의 재료가 되기 때문
        for (int i = 1; i <= n; i++) {
            Collections.sort(nodes[i]);
        }

        answer = 0;
        visit = new boolean[n + 1];
        beforeNode = new int[n + 1]; // 어떤 노드에서 왔는지 [이전 노드]를 저장
        distance = new int[n + 1]; // 해당 노드까지의 최소 거리 저장
        for (int i = 0; i < n + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        // dijkstra 탐색 (s -> e)
        dijkstra(start, end);
        answer += distance[end];

        // 위에서 찾은 최단 경로를 체크하기 위해 새롭게 visit 정의
        for (int i = 0; i <= n; i++) {
            visit[i] = false;
            distance[i] = Integer.MAX_VALUE;
        }
        int checkedNode = beforeNode[end];
        while (checkedNode > 0 && checkedNode != start) {
            visit[checkedNode] = true;
            checkedNode = beforeNode[checkedNode];
        }

        // dijkstra 최단 거리를 계산 (e -> s)
        dijkstra(end, start);
        answer += distance[start];
        checkedNode = beforeNode[start];
        while (checkedNode > 0 && checkedNode != end) {
            visit[checkedNode] = true;
            checkedNode = beforeNode[checkedNode];
        }

        System.out.println(answer);
    }

    private void dijkstra(int from, int to) {
        distance[from] = 0;
        PriorityQueue<Info> pq = new PriorityQueue<>();
        pq.add(new Info(from, 0, 0));

        while (!pq.isEmpty()) {
            Info info = pq.poll();
            if (visit[info.node]) continue;
            visit[info.node] = true;

            if (info.node == to) break;

            // 노드와 연결된 간선 정보들을 불러와 최적의 거리 값으로 갱신이 가능한지 확인
            for (int i = 0; i < nodes[info.node].size(); i++) {
                Node target = nodes[info.node].get(i);

                // *문제를 해결한 부분*
                // 예를 들어, "1-2-3-4-5-6"과 "1-2-5-6" 경로의 총 길이가 같을때
                // 5에 distance 값이 4로 미리 저장이 되었다면 후에 경로가 갱신되지 않는 이상 "1-2-5-6"이 beforeNode로 저장될 것
                // 하지만 정답 경로는 "1-2-3-4-5-6"이 되어야 하기 때문에 경로 갱신을 해야 함
                // 따라서 distance값이 같을 때도 거리 갱신을 '고려'해야 함
                if (distance[target.node] == distance[info.node] + target.cost) { // 더 작은 숫자로의 경로가 가능하면 갱신
                    if (info.node > beforeNode[target.node] && info.node < target.node) {
                        beforeNode[target.node] = info.node;
                    }
                }

                if (distance[target.node] > distance[info.node] + target.cost) { // 기본적인 distance 갱신
                    distance[target.node] = distance[info.node] + target.cost;
                    beforeNode[target.node] = info.node;
                    pq.add(new Info(target.node, info.depth + 1, distance[target.node]));
                }
            }
        }

    }

    private class Node implements Comparable<Node> {
        private int node;
        private int cost;

        public Node(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    private class Info implements Comparable<Info> {
        private int node;
        private int depth;
        private int total;

        public Info(int node, int depth, int total) {
            this.node = node;
            this.depth = depth;
            this.total = total;
        }

        @Override
        public int compareTo(Info o) {
            if (this.total != o.total) {
                return this.total - o.total;
            }
            return this.node - o.node;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}