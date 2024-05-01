// 순환 그래프일 때 끊는 과정을 처음에 만들지 않았었음
import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int m;
    private int[] parent;
    private int[] depth;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        depth = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            depth[i] = 1;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            // 이미 같은 트리에 속해있던 거라면 다시 잇는 과정을 하지 말아야 함
            // 즉 끊는 과정으로 카운트 + 1
            if (!union(left, right)) {
                answer++;
            }
        }


        // 노드 1이랑 다 비교
        for (int i = 2; i <= n; i++) {
            if (find(1) != find(i)) {
                union(1, i);
                answer += 1;
            }
        }

        System.out.println(answer);


    }

    private int find(int node) {
        if (parent[node] != node) {
            return parent[node] = find(parent[node]);
        }
        return node;
    }

    private boolean union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);

        if (root1 == root2) return false;

        if (depth[root1] > depth[root2]) {
            parent[root2] = root1;
            depth[root2] = depth[root1];
        } else {
            parent[root1] = root2;
            if (depth[root1] == depth[root2]) {
                depth[root2] += 1;
            }
            depth[root1] = depth[root2];
        }
        return true;
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}