import java.util.*;
import java.io.*;

public class Main {


    private ArrayList<Coordinate> route;
    private boolean[][] visit;
    private boolean[][] dp;
    private Character[][] board;
    private int answer;
    private int n;
    private int m;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new Character[n][m];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = str.charAt(j);
            }
        }

        visit = new boolean[n][m];
        dp = new boolean[n][m];
        answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j]) {
                    route = new ArrayList<>();
                    move(i, j);
                }
            }
        }

        System.out.println(answer);
    }

    public void move(int sy, int sx) {
        if (sy < 0 || sy >= n || sx < 0 || sx >= m) { //경로 탈출했다면
            for (int i = 0; i < route.size(); i++) { //경로에 대해 answer 추가
                dp[route.get(i).y][route.get(i).x] = true;
            }
            answer += route.size();
            return;
        }
        if (visit[sy][sx]) { //이미 방문했더라면
            if (dp[sy][sx]) { //dp를 보고 탈출 가능하면
                for (int i = 0; i < route.size(); i++) { //경로에 대해 answer 추가
                    dp[route.get(i).y][route.get(i).x] = true;
                }
                answer += route.size();
            }
            return;
        }

        visit[sy][sx] = true;
        route.add(new Coordinate(sy, sx));
        if (board[sy][sx] == 'U') {
            move(sy - 1, sx);
        } else if (board[sy][sx] == 'R') {
            move(sy, sx + 1);
        } else if (board[sy][sx] == 'D') {
            move(sy + 1, sx);
        } else if (board[sy][sx] == 'L') {
            move(sy, sx - 1);
        }
        return;
    }

    public class Coordinate {
        private int y;
        private int x;
        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}