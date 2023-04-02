//뱀을 타는게 더 이득일 수 있다는게 최고의 반례!
import java.util.*;
import java.io.*;


public class Main {


    private HashMap<Integer, Integer> move;
    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        move = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            move.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            move .put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        answer = 100;
        bfs();
        System.out.println(answer);
    }

    public void bfs() {
        boolean[] visit = new boolean[101];
        ArrayDeque<Info> dq = new ArrayDeque<>();
        dq.add(new Info(1, 0));
        while (!dq.isEmpty()) {
            Info info = dq.pollFirst();
            if (info.location > 100) continue;
            if (visit[info.location]) continue;
            visit[info.location] = true;
            if (info.location == 100) {
                answer = Math.min(answer, info.cnt);
                continue;
            }
            for (int i = 1; i <= 6; i++) {
                int next = info.location + i;
                if (move.containsKey(next)) {
                    dq.add(new Info(move.get(next), info.cnt + 1));
                } else {
                    dq.add(new Info(next, info.cnt + 1));
                }
            }
        }
    }

    public class Info {
        private int location;
        private int cnt;

        public Info(int location, int cnt) {
            this.location = location;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}