// 처음에 '시간초과'가 발생했다. 이유는 모든 케이스에 대해 bfs를 진행했기 때문
// 처음 딱 1회 bfs를 통해 탐색 가능한 좌표들에 대해 count를 저장하면 답을 모두 찾아낼 수 있다.
import java.io.*;
import java.util.*;

public class Main {

    private int[][] dir = {{-1, -2}, {1, -2}, {-2, -1}, {2, -1}, {-2, 1}, {2, 1}, {-1, 2}, {1, 2}};
    private int n;
    private int m;
    private Chess knight;
    private int[][] cnt;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        knight = new Chess(y - 1, x - 1, 0);

        Chess[] enemies = new Chess[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int ex = Integer.parseInt(st.nextToken());
            int ey = Integer.parseInt(st.nextToken());
            enemies[i] = new Chess(ey - 1, ex - 1, 0);
        }

        // bfs로 탐색할 수 있는 좌표에 대해 최소 count를 저장한다.
        bfs();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            Chess target = enemies[i];
            sb.append(cnt[target.y][target.x]);
            if (i != m - 1) sb.append(" ");
        }
        System.out.println(sb);
    }

    public void bfs() {
        Deque<Chess> dq = new ArrayDeque<>();
        dq.add(knight);

        cnt = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cnt[i][j] = -1;
            }
        }
        cnt[knight.y][knight.x] = 0;

        while (!dq.isEmpty()) {
            Chess current = dq.pollFirst();

            for (int i = 0; i < 8; i++) {
                int ny = current.y + dir[i][0];
                int nx = current.x + dir[i][1];
                if (ny < 0 || ny >= n || nx < 0 || nx >= n || cnt[ny][nx] >= 0) continue;
                cnt[ny][nx] = current.count + 1;
                dq.add(new Chess(ny, nx, current.count + 1));
            }
        }
    }

    public class Chess {
        private int y;
        private int x;
        private int count;

        public Chess(int y, int x, int count) {
            this.y = y;
            this.x = x;
            this.count = count;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}