// 도전하지 못했다. dp를 이용한 bfs를 생각했는데 아니었다
// 이 문제는 bfs를 정말 크게 부풀려 풀게하는 문제인 것 같다
// 회전 구간을 생각해 일반 board를 4개의 경우로 미리 세팅한 뒤 푸는 것이 핵심
// bfs 알고리즘 그대로 사용하면 되기에 visit을 만들어 방문했던 곳은 다시 탐색하지 않게 한다
import java.util.*;
import java.io.*;

public class Main {


    private int n;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        // 4는 해당 구간이 돌아간 각도를 의미
        // 0: 0도, 1: 90도, 2: 180도, 3: 270도
        char[][][] arr = new char[4][n * 4][n * 4];
        Pos start = null;
        // board 입력 받기
        for (int i = 0; i < 4*n; i++) {
            String row = br.readLine();
            for (int j = 0; j < 4*n; j++) {
                char c = row.charAt(j);
                arr[0][i][j] = c;
                if (c == 'S') { // 시작점
                    start = new Pos(i, j, 0, 0);
                }

                // (i, j) 좌표를 입력 받으면서 동시에 회전한 위치도 저장한다
                int tmpI = i;
                int tmpJ = j;
                for (int x = 1; x <= 3; x++) {
                    int[] nextPos = getRotatedPos(tmpI, tmpJ);
                    tmpI = nextPos[0];
                    tmpJ = nextPos[1];
                    arr[x][tmpI][tmpJ] = c; // 회전한 좌표 저장
                }
            }
        }

        // 방문체크를 위한 배열을 만들고 bfs 탐색
        boolean[][][] v = new boolean[4][n*4][n*4];
        Queue<Pos> q = new ArrayDeque<>();
        q.add(start);
        v[0][start.r][start.c] = true;
        while (!q.isEmpty()) {
            Pos cur = q.poll();
            int r = cur.r;
            int c = cur.c;
            int d = cur.d;
            if (arr[d][r][c] == 'E') {
                System.out.println(cur.dist);
                return;
            }
            int cDiv = getDivision(r, c); // 현재 좌표의 구간
            for (int dir = 0; dir < 5; dir++) {
                int nr = r+DR[dir];
                int nc = c+DC[dir];
                int nDiv = getDivision(nr, nc); // 움직인 곳 좌표의 구간
                if (nDiv == -1) continue;

                // 구역 이동을 한 경우라면 첫 회전이니까 1고정이다
                // 같은 구역은 기존 방향 + 1
                int nd = cDiv == nDiv ? (d+1)%4 : 1;

                // 이동 후 구간 회전까지 해야 최종 좌표를 구하는 것
                int[] nrc = getRotatedPos(nr, nc);
                nr = nrc[0];
                nc = nrc[1];

                if (v[nd][nr][nc] || arr[nd][nr][nc] == '#') continue;
                v[nd][nr][nc] = true;
                q.add(new Pos(nr, nc, nd, cur.dist+1));
            }
        }
        System.out.println(-1);
    }


    class Pos{
        // 좌표, 구간의 회전 방향, 현재까지 이동한 거리
        int r, c, d, dist;
        public Pos(int r, int c, int d, int dist) {
            this.r = r;
            this.c = c;
            this.d = d;
            this.dist = dist;
        }
    }

    private static final int[] DR = {0, 1, -1, 0, 0};
    private static final int[] DC = {0, 0, 0, 1, -1};


    // 구간을 정의하는 메서드
    // 대신 문제에서 표현되는 0, 1, 2, 3... 같은 케이스로 나뉘어지지 않고 임의로 구간을 나누고 있다
    // 문제를 해결하는 과정에서 구간의 번호가 중요한 것이 아니고 같은 구간/다른 구간인지에 대한 판별만 필요하기 때문
    private int getDivision(int r, int c) {
        if (r<0 || c<0 || r>=4*n || c>=4*n) return -1;
        return r/4*4+c/4;
    }

    // 좌표를 90도 회전한 결과를 반환하는 메서드
    // 4 * 4사이즈의 보드에서 회전을 통해 나오는 값을 공식화하면 아래와 같이 나온다
    private int[] getRotatedPos(int r, int c) {
        int baseR = r/4*4;
        int baseC = c/4*4;
        r %= 4;
        c %= 4;
        return new int[]{baseR+c, baseC+3-r};
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}