
import java.util.*;
import java.io.*;

public class Main {


    private int first;
    private int last;
    private boolean[] visit;
    private ArrayList<Info>[] bridges;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        bridges = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            bridges[i] = new ArrayList<>();
        }
        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            bridges[start].add(new Info(end, time));
        }

        for (int i = 0; i < n; i++) {
            Collections.sort(bridges[i]);
        }

        st = new StringTokenizer(br.readLine());
        first = Integer.parseInt(st.nextToken());
        last = Integer.parseInt(st.nextToken());
        visit = new boolean[n + 1];
        dijkstra();

    }

    public void dijkstra() {
        Deque<SearchInfo> dq = new ArrayDeque<>();
        dq.add(new SearchInfo(first, 0, 0));
        visit[first] = true;
        while (!dq.isEmpty()) {
            SearchInfo si = dq.pollFirst();

            if (si.beforeStart == last) {
                System.out.println(si.totalCost);
                System.out.println(si.totalCount);
                break;
            }

            for (int i = 0; i < bridges[si.beforeStart].size(); i++) {
                Info info = bridges[si.beforeStart].get(i);
                if (visit[info.target]) continue;

                visit[info.target] = true;
                dq.add(new SearchInfo(info.target, si.totalCost + info.cost, si.totalCount + 1));

            }

        }
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

    public class SearchInfo {
        private int beforeStart;
        private int totalCost;
        private int totalCount;

        public SearchInfo(int beforeStart, int totalCost, int totalCount) {
            this.beforeStart = beforeStart;
            this.totalCost = totalCost;
            this.totalCount = totalCount;
        }
    }





    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}