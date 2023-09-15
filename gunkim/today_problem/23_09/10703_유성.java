// 문제 설명이 오히려 과해 이해의 어려움을 주었다.
// 단순하게 유성이 땅에 떨어지면 어떤 결과인지 보여주면 되었고 유성은 모양이 변하지 않으며 땅에 닿게 된다.
// 난이도가 낮은 이유는 유성은 무조건 땅 위에만 존재하기 때문에 예외 케이스 체크를 하지 않아도 되기 때문인 것 같다.
import java.util.*;
import java.io.*;

public class Main {


    private boolean[][] visit;
    private int r;
    private int s;
    private char[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());// 세로
        s = Integer.parseInt(st.nextToken());// 가로
        board = new char[r][s];
        for (int i = 0; i < r; i++) {
            String input = br.readLine();
            for (int j = 0; j < s; j++) {
                board[i][j] = input.charAt(j);
            }
        }

        // bfs로 유성을 체크한다
        visit = new boolean[r][s];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < s; j++) {
                bfs(i, j);
                break;
            }
        }

        // 체크한 유성이 땅을 만나는 거리 중 최솟값을 구한다
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < s; i++) {
            for (int j = r - 2; j >= 0; j--) {
                if (board[j][i] != 'X' || board[j + 1][i] != '.') continue;
                // 유성 아래로 떨어질 공간이 있다면 땅과의 거리 체크
                answer = Math.min(answer, distanceToFloor(j, i));
                break;
            }
        }

        // 유성을 answer 만큼 떨어트린다
        move(answer);

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < s; j++) {
                sb.append(board[i][j]);
            }
            if (i != r - 1) sb.append("\n");
        }
        System.out.println(sb);

    }

    public void move(int distance) {
        for (int i = 0; i < s; i++) { // 세로축
            for (int j = r - 1; j >= 0; j--) { // 가로축
                if (board[j][i] == 'X') {
                    board[j + distance][i] = 'X';
                    board[j][i] = '.';
                }
            }
        }
    }

    public int distanceToFloor(int y, int x) {
        int distance = 0;
        for (int i = y + 1; i < r; i++) {
            if (board[i][x] == '.') distance++;
            else break;
        }
        return distance;
    }

    public int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void bfs(int y, int x) {
        Deque<Coordinate> q = new ArrayDeque<>();
        q.offer(new Coordinate(y, x));
        visit[y][x] = true;

        while (!q.isEmpty()) {
            Coordinate c = q.pollFirst();
            for (int i = 0; i < 4; i++) {
                int ny = c.y + dir[i][0];
                int nx = c.x + dir[i][1];
                if (ny < 0 || ny >= r || nx < 0 || nx >= s || board[ny][nx] != 'X' || visit[ny][nx]) continue;
                visit[ny][nx] = true;
                q.offer(new Coordinate(ny, nx));
            }
        }
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