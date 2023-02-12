import java.util.*;
import java.io.*;

public class Main {

    private int wolf;
    private int sheep;
    private boolean[][] visit;
    private int r;
    private int c;
    private char[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        board = new char[r][c];
        ArrayList<Coordinate> location = new ArrayList<>();
        wolf = 0;
        sheep = 0;
        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = str.charAt(j);
                if (board[i][j] == 'v' || board[i][j] == 'o') location.add(new Coordinate(i, j));
                if (board[i][j] == 'v') wolf++;
                if (board[i][j] == 'o') sheep++;
            }
        }

        visit = new boolean[r][c];

        for (Coordinate coordinate : location) {
            int sy = coordinate.y;
            int sx = coordinate.x;
            if (!visit[sy][sx]) {
                bfs(sy, sx);
            }
        }
        System.out.println(sheep + " " + wolf);
    }

    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private void bfs(int sy, int sx) {
        Queue<Coordinate> q = new ArrayDeque<>();
        q.offer(new Coordinate(sy, sx));
        visit[sy][sx] = true;
        int w = 0;
        int s = 0;
        if (board[sy][sx] == 'v') w++;
        else s ++;
        while (!q.isEmpty()) {
            Coordinate co = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = co.y + dir[i][0];
                int nx = co.x + dir[i][1];
                if (ny >= 0 && ny < r && nx >= 0 && nx < c && !visit[ny][nx] && board[ny][nx] != '#') {
                    visit[ny][nx] = true;
                    if (board[ny][nx] == 'v') w++;
                    if (board[ny][nx] == 'o') s++;
                    q.offer(new Coordinate(ny, nx));
                }
            }
        }
        if (s > w) wolf -= w;
        else sheep -= s;
    }


    public class Coordinate{
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