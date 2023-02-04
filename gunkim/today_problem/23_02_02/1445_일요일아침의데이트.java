import java.util.*;
import java.io.*;

public class Main {

    private boolean[][] visit;
    private int n;
    private int m;
    private char[][] board;

    public class Coordinate {
        private int y;
        private int x;
        private int garbage;
        private int block;
        public Coordinate() {
        }
        public Coordinate(int y, int x, int garbage, int block) {
            this.y = y;
            this.x = x;
            this.garbage = garbage;
            this.block = block;
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new char[n][m];
        Coordinate start = new Coordinate();
        LinkedList<Coordinate> gList = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = str.charAt(j);//보드 초기화
                if (str.charAt(j) == 'S') start = new Coordinate(i, j, 0, 0);//시작 위치 저장
                if (str.charAt(j) == 'g') gList.add(new Coordinate(i, j, 0, 0));//쓰레기 위치 저장
            }
        }
        for (Coordinate c : gList) {//쓰레기 주변 일반 블록을 'b'로 초기화
            for (int i = 0; i < 4; i++) {
                int ny = c.y + dir[i][0];
                int nx = c.x + dir[i][1];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && board[ny][nx] == '.')
                    board[ny][nx] = 'b';
            }
        }
        visit = new boolean[n][m];
        Coordinate answer = bfs(start);//bfs로 최적의 동선 찾기
        System.out.println(answer.garbage + " " + answer.block);
    }

    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public Coordinate bfs(Coordinate coordinate) {
        //minHeap을 이용해 최적의 동선을 우선적으로 이용해 탐색
        PriorityQueue<Coordinate> pq = new PriorityQueue<>((o1, o2) ->
                o1.garbage == o2.garbage ? o1.block - o2.block : o1.garbage - o2.garbage);
        pq.offer(coordinate);
        visit[coordinate.y][coordinate.x] = true;
        while (!pq.isEmpty()) {
            Coordinate c = pq.poll();
            if (board[c.y][c.x] == 'F') return c;
            for (int i = 0; i < 4; i++) {
                int ny = c.y + dir[i][0];
                int nx = c.x + dir[i][1];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && !visit[ny][nx]) {
                    visit[ny][nx] = true;
                    if (board[ny][nx] == 'g') pq.add(new Coordinate(ny, nx, c.garbage + 1, c.block));
                    else if (board[ny][nx] == 'b') pq.add(new Coordinate(ny, nx, c.garbage, c.block + 1));
                    else pq.add(new Coordinate(ny, nx, c.garbage, c.block));
                }
            }
        }
        return null;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}