import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private ArrayList<ArrayList<Integer>> list;
    private boolean[] visit;
    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            list.get(n1).add(n2);
            list.get(n2).add(n1);
        }

        visit = new boolean[n];
        answer = 0;
        for (int i = 0; i < n; i++) {
            visit[i] = true;
            if (dfs(i, 0)) break;
            visit[i] = false;
        }

        System.out.println(answer);
    }

    private boolean dfs(int index, int depth) {
        if (depth >= 4) {
            answer = 1;
            return true;
        }
        for (int node : list.get(index)) {
            if (!visit[node]) {
                visit[node] = true;
                dfs(node, depth + 1);
                visit[node] = false;
            }

            if (answer == 1) return true; //백트래킹을 통해 '시간 초과' 막기
        }
        return false;
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}