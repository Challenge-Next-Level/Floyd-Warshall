// 문제는 크게 2가지를 요구한다
// 1. 가장 마지막에 도착하는 사람이 걸리는 시간
// 2. 이때 지나칠 수 있는 다리의 갯수
// 1을 구하는 것은 '비싼 비용으로 경로를 다익스트라로 탐색'하기로 쉽게 알아낼 수 있었다
// 하지만 2를 구하는 것이 어려웠다
// 단순히 '출발지 -> 목적지'를 통해 지날 수 있는 모든 다리의 수를 세기 위해선 dfs(?)같은 탐색이 필요했기에
// 역순으로 '목적지 -> 출발지' 탐색을 통해 지나칠 수 있는 다리를 세면 중복 없이 카운트할 수 있게된다
import java.util.*;
import java.io.*;

public class Main {


    private int first;
    private int last;
    private boolean[] visit;
    private ArrayList<Info>[] bridges;
    private ArrayList<Info>[] reverseBridges; // 역탐색을 위해 필요
    private int[] dist; // 해당 노드에 가장 비싸게 오는 비용 저장

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        dist = new int[n + 1];
        bridges = new ArrayList[n + 1];
        reverseBridges = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            bridges[i] = new ArrayList<>();
            reverseBridges[i] = new ArrayList<>();
        }
        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            bridges[start].add(new Info(end, time));
            reverseBridges[end].add(new Info(start, time));
        }

        st = new StringTokenizer(br.readLine());
        first = Integer.parseInt(st.nextToken());
        last = Integer.parseInt(st.nextToken());

        // 비용이 비싼 순서로 경로를 탐색하는 다익스트라
        System.out.println(dijkstra());

        // 목적지에서 출발지까지 역추적을 하여 정답을 찾아낸다(도로의 수)
        visit = new boolean[n + 1];
        System.out.println(findRoute());

    }

    public int findRoute() {
        int count = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(last);
        visit[last] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (Info next : reverseBridges[cur]) {
                if (dist[cur] - next.cost == dist[next.target]) { // 해당 노드에 올 수 있는 다리만 탐색한다
                    count++; // 다리 추가
                    if (!visit[next.target]) { // 방문하지 않는 노드라면 queue에 추가
                        visit[next.target] = true;
                        q.add(next.target);
                    }
                }
            }
        }
        return count;
    }

    public int dijkstra() {
        // 다익스트라는 '우선순위큐'가 필요하다
        PriorityQueue<Info> pq = new PriorityQueue<>();
        pq.add(new Info(first, 0));

        while (!pq.isEmpty()) {
            Info cur = pq.poll();

            for (Info next : bridges[cur.target]) {
                // 가장 비싼 비용의 경로를 찾는다
                if (dist[next.target] < cur.cost + next.cost) {
                    dist[next.target] = cur.cost + next.cost;
                    pq.add(new Info(next.target, dist[next.target]));
                }
            }

        }
        return dist[last];
    }

    public class Info implements Comparable<Info> {
        private int target;
        private int cost;

        public Info(int target, int cost) {
            this.target = target;
            this.cost = cost;
        }

        @Override
        public int compareTo(Info o) {
            return o.cost - this.cost;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}