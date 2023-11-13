// 우선 도착지로 가는 경로는 최소의 비용으로 탐색하는 것이 좋다 (갖고있는 돈의 제한이 있기 때문)
// 자연스럽게 '우선순위큐'를 통한 '다익스트라'탐색을 떠올렸다
// 하지만 문제는 이런 탐색을 하면서 '언제가' 가장 최적의해(수치심을 가장 덜 지불하는)가 되는 경로인지를 판별하는가? 이다
// 모든 경로를 탐색하면 딱 봐도 시간초과 같은 에러가 발생할 것 같았다 (n, m의 조건이 너무 크기 때문)
// 해결을 찾아 보았고 kotlin으로 풀이한 것을 참고했다
// 답을 미리 정해두고 해당 답을 도출할 수 있는 경로가 있는지 판별하는 것이다
// 그리고 그 답은 이분 탐색으로 빠르게 최적의 해를 찾아가는 것이다

import java.util.*;
import java.io.*;

public class Main {


    private boolean[] visit;
    private ArrayList<Node>[] bridges;
    private int n;
    private int m;
    private int a;
    private int b;
    private int c;
    private int answer;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 교차로 수
        n = Integer.parseInt(st.nextToken());
        // 골목 수
        m = Integer.parseInt(st.nextToken());
        // 시작 교차로
        a = Integer.parseInt(st.nextToken());
        // 도착 교차로
        b = Integer.parseInt(st.nextToken());
        // 가진 돈
        c = Integer.parseInt(st.nextToken());

        bridges = new ArrayList[n + 1]; // 간선 저장
        for (int i = 1; i <= n; i++) {
            bridges[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int bill = Integer.parseInt(st.nextToken());
            bridges[A].add(new Node(B, bill));
            bridges[B].add(new Node(A, bill));
        }



        int start = 1;
        int end = 20;
        int mid; // 이 값이 미리 정해두는 답이 된다
        answer = Integer.MAX_VALUE;
        while (start <= end) {
            mid = (start + end) / 2;
            if (dijkstra(mid)) { // 해당 값이 탐색시 유효한지 판별
                answer = Math.min(answer, mid);
                end = mid - 1; // 유효하다면 값을 줄여본다
            } else start = mid + 1;
        }

        if (answer == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);

    }

    public boolean dijkstra(int minCost) {
        PriorityQueue<Node> pq = new PriorityQueue<>(); // 다익스트라 탐색을 위한 우선순위 큐 이용
        visit = new boolean[n + 1]; // 탐색을 계속 새로하기 때문에 이곳에서 visit 초기화
        pq.add(new Node(a, 0, 0));
        visit[a] = true;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            for (Node next : bridges[cur.target]) {
                if(visit[next.target]) continue;

                int sumCost = cur.cost + next.cost;
                int maxCost = Math.max(cur.maxCost, next.cost);
                // 비용 내 갈 수 없거나
                // 정해진 최소 비용을 초과하면
                // 다른 길 탐색
                if (sumCost > c || maxCost > minCost) continue;

                // 도착지라면
                if (next.target == b) return true;

                pq.add(new Node(next.target, sumCost, maxCost));
                visit[next.target] = true;
            }
        }

        return false;
    }


    public class Node implements Comparable<Node> {
        private int target;
        private int cost; // 다리의 비용 or 현재까지 거쳐온 비용의 합
        private int maxCost; // 현재까지 거쳐온 비용의 최댓값

        public Node(int target, int cost) {
            this.target = target;
            this.cost = cost;
        }
        public Node(int target, int cost, int maxCost) {
            this.target = target;
            this.cost = cost;
            this.maxCost = maxCost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}