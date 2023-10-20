// bfs + visit 아이디어와 함께 visit 관리는 4중 배열로 해도 되겠다는 것까지는 풀이가 좋았고
// 다만 구슬을 굴리면서 좌표 갱신을 좀 애먹었다. 구현을 하는 센스가 부족했다
// 구현 센스가 돋보였던 포인트는,
// 1. bfs의 깊이에 대한 카운트 체크
// 2. move 메서드를 이용할 때 현재 좌표에 대한 필드 값을 clone으로 만들어 매개변수로 이용한 것
// 3. 방향에 따라 빨간공이 더 앞서 있어야 한다는 점을 저장해두고 활용한 점(redFirst)
import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    private boolean[][][][] visit;
    private char[][] board;
    private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; // 남,북,동,서
    private int n;
    private int m;
    private int[][] newBoard;


    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new char[n][m];
        int ry = 0, rx = 0, by = 0, bx = 0;
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = input.charAt(j);
                if (input.charAt(j) == 'R') {
                    ry = i;
                    rx = j;
                }
                if (input.charAt(j) == 'B') {
                    by = i;
                    bx = j;
                }
            }
        }

        visit = new boolean[n][m][n][m];

        System.out.println(bfs(ry, rx, by, bx));


    }

    public int bfs(int ry, int rx, int by, int bx) {
        Deque<Info> dq = new ArrayDeque<>();
        dq.add(new Info(ry, rx, by, bx));
        visit[ry][rx][by][bx] = true;

        int cnt = 0;
        while (!dq.isEmpty() && cnt < 10) {
            int len = dq.size();

            for (int i = 0; i < len; i++) {
                Info info = dq.pollFirst();
                // 보드 판을 상하좌우로 기울인다
                for (int j = 0; j < 4; j++) { // 남,북,동,서
                    Info cur = new Info(info.redY, info.redX, info.blueY, info.blueX);
                    if (move(cur, j)) { // 파란공이 탈출하지 않고 두 개의 공이 이동을 잘 한경우
                        if (board[cur.redY][cur.redX] == 'O') return 1; // 빨간공이 탈출했다면

                        if (visit[cur.redY][cur.redX][cur.blueY][cur.blueX]) continue;
                        visit[cur.redY][cur.redX][cur.blueY][cur.blueX] = true;
                        dq.add(new Info(cur.redY, cur.redX, cur.blueY, cur.blueX));
                    }
                }
            }
            cnt++;
        }
        return 0;
    }


    public boolean move(Info info, int direction) {
        boolean redFirst = false;
        // 남,북,동,서
        if (direction == 0 && info.redY > info.blueY) redFirst = true;
        if (direction == 1 && info.redY < info.blueY) redFirst = true;
        if (direction == 2 && info.redX > info.blueX) redFirst = true;
        if (direction == 3 && info.redX < info.blueX) redFirst = true;

        // 빨간공부터 움직여보자
        int ny = info.redY;;
        int nx = info.redX;
        while (true) {
            ny += dir[direction][0];
            nx += dir[direction][1];
            if (board[ny][nx] == '#') break; // 벽으로는 이동 못해
            info.redY = ny;
            info.redX = nx;
            if (board[ny][nx] == 'O') break; // 출구일땐 좌표 갱신 후 break 한다
        }

        // 푸른공 움직여보자
        ny = info.blueY;;
        nx = info.blueX;
        while (true) {
            ny += dir[direction][0];
            nx += dir[direction][1];
            if (board[ny][nx] == '#') break; // 벽으로는 이동 못해
            info.blueY = ny;
            info.blueX = nx;
            if (board[ny][nx] == 'O') break; // 출구일땐 좌표 갱신 후 break 한다
        }

        // 푸른공이 탈출했다면 실패한 케이스
        if (board[info.blueY][info.blueX] == 'O') return false;

        // 움직인 두 개의 공 좌표가 같다면
        if (info.redY == info.blueY && info.redX == info.blueX) {
            switch (direction) {
                case 0:
                    if (redFirst) info.blueY--;
                    else info.redY--;
                    break;
                case 1:
                    if (redFirst) info.blueY++;
                    else info.redY++;
                    break;
                case 2:
                    if (redFirst) info.blueX--;
                    else info.redX--;
                    break;
                case 3:
                    if (redFirst) info.blueX++;
                    else info.redX++;
                    break;
            }
        }
        return true;
    }

    public class Info {
        private int redY;
        private int redX;
        private int blueY;
        private int blueX;

        public Info(int redY, int redX, int blueY, int blueX) {
            this.redY = redY;
            this.redX = redX;
            this.blueY = blueY;
            this.blueX = blueX;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}