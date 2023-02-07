//군대를 보낼 때 길이 넓은 곳을 우선으로 보낼 것
//그렇게 다리를 선정하다보면 도착하는 동선이 만들어질 것이고 선정한 다리 중 가장 좁은 다리를 선택
import java.util.*;
import java.io.*;

public class Main {

    private int[] parent;

    public class Bridge{
        private int node1;
        private int node2;
        private int width;

        public Bridge(int node1, int node2, int width) {
            this.node1 = node1;
            this.node2 = node2;
            this.width = width;
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        PriorityQueue<Bridge> bridges = new PriorityQueue<>((o1, o2) -> o2.width - o1.width);
        for (int i = 0; i < w; i++) {
            st = new StringTokenizer(br.readLine());
            bridges.offer(new Bridge(Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())));
        }
        parent = new int[p];
        for (int i = 0; i < p; i++) {
            parent[i] = i;
        }
        int answer = 0;
        while (!bridges.isEmpty()) {
            Bridge b = bridges.poll();

            union(b.node1, b.node2);
            if (find(c) == find(v)) {
                answer = b.width;
                break;
            }
        }
        System.out.println(answer);
    }

    private int find(int node) {
        if (parent[node] == node) return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }

    private void union(int node1, int node2) {
        int node1Parent = find(node1);
        int node2Parent = find(node2);
        if (node1Parent != node2Parent) parent[node2Parent] = node1Parent;
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}