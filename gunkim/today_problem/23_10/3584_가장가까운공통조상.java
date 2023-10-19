// 알고리즘 문제 풀 때는 항상 종이에 적으면서 생각하는게 중요한 것 같음
// 머리로 풀 때는 간단한 구현 문제인가? 이런 생각을 했지만 막상 알고리즘 분류를 보니 그래프 탐색;;;
// 종이로 적어 생각하니 그래프 탐색이 맞았음. 1 try 1 solve 문제!
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());

            // 노드 배열에 부모만 리스트에 추가하도록 한다
            List<Integer>[] node = new List[n + 1];
            for (int j = 0; j <= n; j++) {
                node[j] = new ArrayList<>();
            }

            StringTokenizer st;
            for (int j = 0; j < n - 1; j++) {
                st = new StringTokenizer(br.readLine());
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                // 자식 노드에 부모만 추가한다
                node[child].add(parent);
            }

            st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());

            // nodeA의 부모를 visit 체크한 후 nodeB의 부모를 탐색한다
            boolean[] visit = new boolean[n + 1];
            Deque<Integer> dq = new ArrayDeque<>();
            dq.add(nodeA);
            while (!dq.isEmpty()) {
                int cur = dq.pollFirst();
                visit[cur] = true;
                for (Integer parent : node[cur]) {
                    dq.add(parent);
                }
            }

            dq.add(nodeB);
            while (!dq.isEmpty()) {
                int cur = dq.pollFirst();
                if (visit[cur]) {
                    sb.append(cur).append("\n");
                    break;
                }
                for (Integer parent : node[cur]) {
                    dq.add(parent);
                }
            }
        }
        System.out.println(sb);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}