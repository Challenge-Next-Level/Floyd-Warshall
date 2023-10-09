// dp에 거울의 갯수를 저장하는 것이 핵심인데 이때 beforeDir에 따라 저장을 해야 한다는 점이다.
// 따라서 각 좌표에 4개의 방향에 대한 dp 값을 따로 저장했다.
// bfs 탐색에서 백 트래킹은 좌표를 벗어나거나, 벽을 만나거나, 거울 갯수를 더 사용했거나 조건이다.
import java.util.*;
import java.io.*;

public class Main {


    private int[][][] dp; // mirror 갯수 dp값. 이때 어느 방향에서 왔을 때인지 체크
    private int w;
    private int h;
    private char[][] board;
    private int sy;
    private int sx;
    private int dy;
    private int dx;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        board = new char[h][w];
        sy = -1;
        for (int i = 0; i < h; i++) {
            String input = br.readLine();
            for (int j = 0; j < w; j++) {
                board[i][j] = input.charAt(j);
                if (board[i][j] == 'C') {
                    if (sy == -1) {
                        sy = i;
                        sx = j;
                    } else {
                        dy = i;
                        dx = j;
                    }
                }
            }
        }

        dp = new int[h][w][4];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                for (int k = 0; k < 4; k++) {
                    dp[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        bfs();

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < 4; i++) {
            answer = Math.min(answer, dp[dy][dx][i]);
        }

        System.out.println(answer);
    }

    public int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; // 남(0), 북(1), 동(2), 서(3)
    public void bfs() {
        Deque<Go> dq = new ArrayDeque();
        dq.add(new Go(sy, sx, 0, -1));
        for (int i = 0; i < 4; i++) {
            dp[sy][sx][i] = -1;
        }

        while (!dq.isEmpty()) {
            Go go = dq.pollFirst();

            if (board[go.y][go.x] == 'C' && go.y == dy && go.x == dx) continue;

            for (int i = 0; i < 4; i++) { // 4방향 탐색. beforeDir는 i값이 될 것
                int ny = go.y + dir[i][0];
                int nx = go.x + dir[i][1];
                if (ny < 0 || ny >= h || nx < 0 || nx >= w || board[ny][nx] == '*') continue;

                // 해당 방향에서 거울 갯수에 대해 언제든 갱신이 가능하다. 그러니 갯수에 대한 조건만 걸어둔다.
                if (go.mirror >= dp[ny][nx][i]) continue;

                if (go.beforeDir == -1 || go.beforeDir == i) {
                    dp[ny][nx][i] = go.mirror;
                    dq.add(new Go(ny, nx, go.mirror, i));
                } else {
                    dp[ny][nx][i] = go.mirror + 1;
                    dq.add(new Go(ny, nx, go.mirror + 1, i));
                }
            }
        }
    }

    public class Go {
        private int y;
        private int x;
        private int mirror;
        private int beforeDir;

        public Go(int y, int x, int mirror, int beforeDir) {
            this.y = y;
            this.x = x;
            this.mirror = mirror;
            this.beforeDir = beforeDir;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}