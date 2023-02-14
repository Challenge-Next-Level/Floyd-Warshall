import java.util.*;
import java.io.*;

public class Main {


    private String target;
    private int targetSize;
    private ArrayList<Integer> answer;
    private boolean[][] visit;
    private int n;
    private int[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = str.charAt(j) - '0';
            }
        }

        answer = new ArrayList<>();
        visit = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j] && board[i][j] == 1) answer.add(bfs(i, j));
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(answer.size() + "\n");
        answer.sort(((o1, o2) -> o1 - o2));
        for (int num : answer) {
            sb.append(num + "\n");
        }
        System.out.println(sb);
    }

    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int bfs(int y, int x) {
        Queue<Coordinate> queue = new ArrayDeque<>();
        queue.offer(new Coordinate(y, x));
        visit[y][x] = true;
        int cnt = 1;
        while (!queue.isEmpty()) {
            Coordinate c = queue.poll();
            for (int i = 0; i < dir.length; i++) {
                int ny = c.y + dir[i][0];
                int nx = c.x + dir[i][1];
                if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visit[ny][nx] && board[ny][nx] == 1) {
                    visit[ny][nx] = true;
                    cnt++;
                    queue.offer(new Coordinate(ny, nx));
                }
            }
        }
        return cnt;
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