import java.util.*;
import java.io.*;

public class Main {

    public class Coordinate {
        public int y;
        public int x;
        public int dist;
        public Coordinate(int y, int x, int dist) {
            this.y = y;
            this.x = x;
            this.dist = dist;
        }
    }

    int[][] dir = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};//상하좌우 방향 좌표
    boolean[][] visit;//bfs 탐색시 방문 체크
    Deque<Coordinate> dq = new ArrayDeque<>();//bfs 탐색시 좌표를 담아둘 deque
    Deque<Coordinate> target = new ArrayDeque<>();//먹을 수 있는 물고기는 모두 담아둘 deque
    public boolean bfs() {
        dq.offer(shark);
        visit = new boolean[n][n];
        visit[shark.y][shark.x] = true;
        while (!dq.isEmpty()) {//bfs 탐색 시작
            Coordinate s = dq.pollFirst();
            if (board[s.y][s.x] != 0) { //물고기 발견
                if (board[s.y][s.x] < size) { //상어보다 작은지 확인
                    target.offer(new Coordinate(s.y, s.x, s.dist));//타겟 대상으로 담아두기
                }
            }
            for (int i = 0; i < 4; i++) {//상하좌우 탐색
                int ny = s.y + dir[i][0];
                int nx = s.x + dir[i][1];
                //중요: 나보다 큰 물고기가 있는 곳은 지나갈 수 없음
                if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visit[ny][nx] && size >= board[ny][nx]) {
                    visit[ny][nx] = true;//중요: 방문 처리를 이곳에서 해야 '메모리 초과'를 방지할 수 있음
                    dq.offer(new Coordinate(ny, nx, s.dist + 1));
                }
            }
        }
        if (!target.isEmpty()) {//담아둔 물고기들에 대해 조건에 맞는 물고기 탐색
            Coordinate realTarget = target.pollFirst();
            while (!target.isEmpty()) {
                Coordinate compTarget = target.pollFirst();
                if (realTarget.dist > compTarget.dist) {//1.거리 비교
                    realTarget = compTarget;
                } else if (realTarget.dist == compTarget.dist) {//2.y좌표 비교
                    if (realTarget.y > compTarget.y) realTarget = compTarget;
                    else if (realTarget.y == compTarget.y) {//3.x좌표 비교
                        if (realTarget.x > compTarget.x) realTarget = compTarget;
                    }
                }
            }
            answer += realTarget.dist;//시간 초 갱신
            //몸집이 커지는 타이밍인지 확인
            if (eatCount == size - 1){
                size += 1;
                eatCount = 0;
            } else {
                eatCount += 1;
            }
            shark.y = realTarget.y;
            shark.x = realTarget.x;
            board[realTarget.y][realTarget.x] = 0;//물고기 삭제
            return true;
        }
        return false;
    }
    int n;
    int[][] board;
    Coordinate shark;
    int answer = 0;
    int size = 2;
    int eatCount = 0;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 9){
                    shark = new Coordinate(i, j, 0);
                    board[i][j] = 0;
                }
            }
        }

        while (bfs()) {//물고기를 못 먹을 때 까지 탐색
            continue;
        }
        System.out.println(answer);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}