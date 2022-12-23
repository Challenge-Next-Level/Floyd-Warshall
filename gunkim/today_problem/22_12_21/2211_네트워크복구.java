import java.util.*;
import java.io.*;

public class Main {

    class Edge implements Comparable<Edge> {
        int to, cost;
        public Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
        @Override
        public int compareTo(Edge o) { //기본적인 정렬
            //더 큰 값이 뒤로 배치되는 오름 차순 정렬을 유도한다.
            return this.cost - o.cost;
        }
    }
    public void dijkstra(int start) {
        dist = new int[N + 1];
        path = new int[N + 1]; //갱신된 시점에 '출발한 노드'를 저장
        Arrays.fill(dist, Integer.MAX_VALUE); //거리 초기화
        dist[start] = 0; //시작지점의 비용 0
        Queue<Edge> pq = new PriorityQueue<>(); //우선순위 큐는 기본적으로 min Heap 구조이다. 따라서 가장 작은 값이 head에 배치.
        //add와 offer의 차이
        //add는 큐가 꽉 차 있으면 예외를 리턴
        //offer는 false를 리턴, 아마 예외 처리를 하기 싫어서 offer를 사용한 것 같다.
        pq.offer(new Edge(start, 0)); //첫번째 시작 노드로 가는데 비용이 0이 든다는 의미의 간선 추가

        while(!pq.isEmpty()) {
            //remove와 poll의 차이
            //역시나 remove는 큐가 비어있다면 예외 리턴, poll은 null를 리턴한다.
            Edge e = pq.poll();

            if (e.cost > dist[e.to]) continue;

            int from = e.to, curCost = e.cost;
            for (Edge ne : edgeList[from]) {
                if (dist[ne.to] > curCost + ne.cost) { //비용 갱신이 가능하다면
                    dist[ne.to] = curCost + ne.cost;
                    path[ne.to] = from; //경로 저장
                    pq.offer(new Edge(ne.to, dist[ne.to]));
                }
            }
        }
    }

    int N, M, cnt;
    int[] dist, path;
    List<Edge>[] edgeList;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //노드 갯수
        M = Integer.parseInt(st.nextToken()); //간선 갯수

        edgeList = new ArrayList[N + 1]; //크기 설정
        for (int i = 1; i <= N; ++i) {
            edgeList[i] = new ArrayList<>(); //각 배열 초기화
        }
        for (int i = 0; i < M; ++i) { //간선 리스트 생성
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            edgeList[A].add(new Edge(B, C));
            edgeList[B].add(new Edge(A, C));
        }

        dijkstra(1); //1번 노드에서 다익스트라 탐색

        StringBuilder sb = new StringBuilder();
        for (int v = 2; v <= N; v++) {
            if (path[v] == 0) continue; //이전 노드에 대한 값이 갱신되지 않은 것들은 continue
            cnt++;
            sb.append(v + " " + path[v] + "\n");
        }
        System.out.println(cnt + "\n" + sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}