// bfs 탐색이 들어가지만 빡구현에 어울리는 문제다.
// 문제를 이해하는 것이 가장 어려웠음. 핵심은 땅에서 연결된 미네랄은 '떠있는 미네랄'이 아닌 것이다.
// 1. 미네랄을 부순다
// 2. 바닥에서 미네랄을 탐색한다
// 3. 탐색되지 않은 미네랄은 떠있는 미네랄이 되고 이것들을 이동시킨다
// 4. 미네랄 조각들이 떨어질 수 있는 최대 높이의 최솟값을 구한다
// 이때 주의! 미네랄 클러스터의 맨 아래 조각들에 대해서만 생각하면 안된다. ㄷ 자 모양의 미네랄 클러스터가 있다고 생각하자
// 그 사이에 떠있지 않는 미네랄이 있다면 'ㄷ' 자 모양의 미네랄은 떨어지다가 걸칠 것이다
import java.io.*;
import java.util.*;

public class Main {


    private char[][] board;
    private int r;
    private int c;
    private int[] heights;
    private boolean[][] visit;
    private boolean[][] newVisit;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            String input = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = input.charAt(j);
            }
        }
        int n = Integer.parseInt(br.readLine());
        heights = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        // 총 n 번 반복한다
        for (int i = 0; i < n; i++) {
            // 왼쪽 혹은 오른쪽 미네랄 제거
            breakMineral(i);

            // 바닥에서 미네랄 탐색
            visit = new boolean[r][c];
            for (int j = 0; j < c; j++) {
                if (board[r - 1][j] == 'x' && !visit[r - 1][j]) {
                    bfs(r - 1, j, visit);
                }
            }

            // 탐색되지 않은 미네랄은 공중에 떠있는 미네랄 클러스터. 미네랄을 이동시킨다
            moveMineral();

        }


        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                sb.append(board[i][j]);
            }
            if (i != r - 1) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    public void moveMineral() {
        // 탐색 되지 않은 미네랄 저장
        ArrayList<Coordinate> coordinates = new ArrayList<>();
        newVisit = new boolean[r][c];
        boolean flag = false;
        for (int i = r - 1; i >= 0; i--) { // 떨어지는 미네랄 클러스터는 단 하나 밖에 없음
            if (flag) break;
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 'x' && !visit[i][j]) {
                    coordinates = bfs(i, j, newVisit);
                    flag = true;
                    break;
                }
            }
        }

        // 최대 높이의 최솟값을 구한다
        int moved = Integer.MAX_VALUE;
        for (Coordinate coordinate : coordinates) {
            int sy = coordinate.y;
            int sx = coordinate.x;
            int count = 0;
            for (int i = sy + 1; i < r; i++) {
                if (board[i][sx] == 'x' && visit[i][sx]) break;
                count++;
            }

            moved = Math.min(moved, count);
        }

        // <주의!>미네랄을 이동시킬 때 아래 미네랄 부터 차근차근 이동시켜야 해서 정렬을 한다.
        Collections.sort(coordinates);

        for (Coordinate coordinate : coordinates) {
            board[coordinate.y][coordinate.x] = '.';
            board[coordinate.y + moved][coordinate.x] = 'x';
        }
    }

    private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public ArrayList<Coordinate> bfs(int y, int x, boolean[][] visited) {

        ArrayList<Coordinate> blockList = new ArrayList<>();

        Deque<Coordinate> dq = new ArrayDeque<>();
        dq.add(new Coordinate(y, x));
        visited[y][x] = true;
        blockList.add(new Coordinate(y, x));

        while (!dq.isEmpty()) {
            Coordinate current = dq.pollFirst();
            for (int j = 0; j < 4; j++) {
                int ny = current.y + dir[j][0];
                int nx = current.x + dir[j][1];
                if (ny < 0 || ny >= r || nx < 0 || nx >= c || visited[ny][nx] || board[ny][nx] == '.') continue;
                visited[ny][nx] = true;
                dq.add(new Coordinate(ny, nx));
                blockList.add(new Coordinate(ny, nx));
            }
        }

        return blockList;
    }

    public class Coordinate implements Comparable<Coordinate> {
        private int y;
        private int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public int compareTo(Coordinate o) {
            return o.y - this.y;
        }
    }

    public void breakMineral(int idx) {
        int height = r - heights[idx];
        if (idx % 2 == 0) { // 왼쪽에서 제거
            for (int i = 0; i < c; i++) {
                if (board[height][i] == 'x') {
                    board[height][i] = '.';
                    return;
                }
            }
        } else { // 오른쪽에서 제거
            for (int i = c - 1; i >= 0; i--) {
                if (board[height][i] == 'x') {
                    board[height][i] = '.';
                    return;
                }
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}