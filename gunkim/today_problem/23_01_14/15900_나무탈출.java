import java.util.*;
import java.io.*;

public class Main {
    public void dfs(int n, int count, boolean[] visited) {
        visited[n] = true;

        for (int nextNode : node.get(n)) {
            if (!visited[nextNode]) dfs(nextNode, count + 1, visited);
        }
        //root node가 아니고, 연결된 node가 한 개 밖에 없는 노드는 leaf node 이다.
        if (n != 1 && node.get(n).size() == 1) result += count;
    }

    ArrayList<ArrayList<Integer>> node;//2중 ArrayList가 핵심인 것 같음. 처음 사용해봄.
    int result = 0;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        node = new ArrayList<>();
        for (int i = 0; i <= n; i++) {//node ArrayList 초기화
            node.add(new ArrayList<>());
        }

        StringTokenizer st;
        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            //양방향 node list 구현
            node.get(node1).add(node2);
            node.get(node2).add(node1);
        }

        boolean[] visit = new boolean[n + 1];
        dfs(1, 0, visit);

        if (result % 2 == 0) System.out.println("No");
        else System.out.println("Yes");
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}