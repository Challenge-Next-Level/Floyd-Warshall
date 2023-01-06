//처음엔 모든 좌표를 계속 탐색해서 해결하려고 했으나 '시간 초과'가 발생
//결국 무너지는 모래성들에 대한 주변 탐색만을 통해 문제 해결
import java.util.*;
import java.io.*;

public class Main {

    public class Coordinate {
        private int y;
        private int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    int[][] dir = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    public boolean isDanger(int y, int x) {
        int limit = arr[y][x];
        for (int i = 0; i < 8; i++) {
            int ny = y + dir[i][0];
            int nx = x + dir[i][1];
            if (arr[ny][nx] == 0) limit -= 1;

            if (limit <= 0) return true;
        }
        return false;
    }

    int h;
    int w;
    int[][] arr;
    boolean[][] visit;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        arr = new int[h][w];
        visit = new boolean[h][w];//무너뜨린 모래성은 기억해둔다.
        for (int i = 0; i < h; i++) {//최외각 좌표는 배제
            String str = br.readLine();
            for (int j = 0; j < w; j++) {
                if (str.charAt(j) == '.') arr[i][j] = 0;
                else arr[i][j] = str.charAt(j) - '0';
            }
        }

        int answer = 0;

        //처음으로 부서지는 모래성 체크
        Deque<Coordinate> deque = new ArrayDeque<>();
        for (int i = 1; i < h - 1; i++) {
            for (int j = 1; j < w - 1; j++) {
                if (visit[i][j] || arr[i][j] == 0 || arr[i][j] >= 9) continue;
                if (isDanger(i, j)) {
                    deque.offer(new Coordinate(i, j));
                    visit[i][j] = true;
                }
            }
        }
        //부서지는 모래성의 연쇄작용으로 주변 모래성이 부서지는지 체크를 하면 된다.
        while (!deque.isEmpty()) {
            int size = deque.size();
            while (size > 0) {
                Coordinate c = deque.pollFirst();
                arr[c.y][c.x] = 0;//모래성 부수기
                for (int i = 0; i < 8; i++) {//주변에 연쇄작용으로 부서지는 모래성이 있는지 확인
                    int ny = c.y + dir[i][0];
                    int nx = c.x + dir[i][1];
                    if (visit[ny][nx] || arr[ny][nx] == 0 || arr[ny][nx] >= 9) continue;
                    if (isDanger(ny, nx)) {
                        deque.offer(new Coordinate(ny, nx));
                        visit[ny][nx] = true;
                    }
                }
                size -= 1;
            }
            answer += 1;
        }


        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}