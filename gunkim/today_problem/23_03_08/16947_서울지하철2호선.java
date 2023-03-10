//순환선을 기록해두는 방법 구현이 어려운 부분 같다, 이번 것도 풀지 못함
import java.util.*;
import java.io.*;

public class Main {

    private boolean[] isCycle;
    private ArrayList<Integer>[] list;
    private int n;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        list = new ArrayList[n + 1];
        for(int i = 1; i <= n; i++) {
            list[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            list[n1].add(n2);
            list[n2].add(n1);
        }

        isCycle = new boolean[n + 1]; //순환선 기록
        for(int i = 1; i <= n; i++) {
            if(checkCycle(i, i, i)) break;
            isCycle = new boolean[n + 1];
        }

        int[] result = new int[n + 1];
        for(int i = 1; i <= n; i++) { //순환선이 아닌 곳만 bfs 탐색으로 최소거리 찾기
            if(!isCycle[i]) result[i] = bfs(i);
        }

        for(int i = 1; i <= n; i++) System.out.print(result[i] + " ");

    }

    public int bfs(int node) {
        Queue<Node> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        q.add(new Node(node, 0));
        visited[node] = true;

        while(!q.isEmpty()) {
            Node current = q.poll();
            if(isCycle[current.v]) return current.count;

            for(int i = 0; i < list[current.v].size(); i++) {
                int next = list[current.v].get(i);
                if(!visited[next]) {
                    visited[next] = true;
                    q.add(new Node(next, current.count + 1));
                }
            }
        }
        return 0;
    }
    public boolean checkCycle(int prev, int node, int start) {
        isCycle[node] = true;

        for(int i = 0; i < list[node].size(); i++) {
            int next = list[node].get(i);

            if(!isCycle[next]) { //재귀로 연결된 노드 계속 탐색
                if(checkCycle(node, next, start)) return true;
            } else if(next != prev && next == start) return true; //바로 이전 노드가 아니면서 첫 노드로 돌아왔을 때
        }
        isCycle[node] = false;

        return false;
    }

    public class Node {
        int v;
        int count;

        public Node(int v, int count) {
            this.v = v;
            this.count = count;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}