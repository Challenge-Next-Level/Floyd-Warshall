import java.util.*;
import java.io.*;

public class Main {

    Character[][] board = new Character[12][6];
    boolean[][] visit;
    Boolean changed;

    public class Coordinate {
        private int y;
        private int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public void bfs(int y, int x) {//탐색 + 터트리기
        List<Coordinate> coordinates = new ArrayList<>();

        Deque<Coordinate> deque = new ArrayDeque<>();
        visit[y][x] = true;
        deque.add(new Coordinate(y, x));

        while (deque.peekFirst() != null) {//같은 색으로 연결된 뿌요찾기
            Coordinate c = deque.pollFirst();
            coordinates.add(new Coordinate(c.y, c.x));//방문했던 좌표 저장해두기
            for (int a = 0; a < 4; a++) {//4방향 탐색
                int ny = c.y + dir[a][0];
                int nx = c.x + dir[a][1];
                if (ny >= 0 && ny < 12 && nx >= 0 && nx < 6) {
                    if (board[y][x] == board[ny][nx] && !visit[ny][nx]) {
                        visit[ny][nx] = true;
                        deque.add(new Coordinate(ny, nx));
                    }
                }
            }
        }
        if (coordinates.size() >= 4) {//뿌요 터트리기
            changed = true;
            for (Coordinate c : coordinates) {
                board[c.y][c.x] = '.';
            }
        }
    }


    public void updateBoard() {//뿌요 보드 판 업데이트: 아래로 떨어져야 할 뿌요는 떨어 트리기
        for (int i = 11; i > 0; i--) {
            for (int j = 0; j < 6; j++) {
                if (board[i][j] == '.') {
                    for (int k = i - 1; k >= 0; k--) {
                        if (board[k][j] != '.') {
                            board[i][j] = board[k][j];
                            board[k][j] = '.';
                            break;
                        }
                    }
                }
            }
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String st;
        for (int i = 0; i < 12; i++) {
            st = new String(br.readLine());
            for (int j = 0; j < 6; j++) {
                board[i][j] = st.charAt(j);
            }
        }

        int count = 0;//연쇄 저장
        while (true) {
            //매 번 탐색 전에는 자료 초기화
            visit = new boolean[12][6];
            changed = false;
            for (int i = 0; i < 12; i++) {
                for (int j = 0; j < 6; j++) {
                    if (board[i][j] != '.' && !visit[i][j]) {
                        bfs(i, j);
                    }
                }
            }
            if (changed) {//연쇄가 발생했을 때
                count += 1;
                updateBoard();
            } else {//발생하지 않았을 때
                System.out.println(count);
                break;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}