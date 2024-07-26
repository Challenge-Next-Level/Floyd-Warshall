// 쉬운 재귀 문제?
import java.io.*;
import java.util.*;

public class Main {

    // 동남서북 진행
    public static final int[] DY = {0, 1, 0, -1};
    public static final int[] DX = {1, 0, -1, 0};
    static int N;
    static int M;
    static boolean[][] visit;
    static int result = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        visit = new boolean[M][N];

        go(0, 0, 0);

        System.out.println(result);
    }


    public static void go(int y, int x, int dir) {
        visit[y][x] = true;
        int ny = y + DY[dir];
        int nx = x + DX[dir];
        if (nx < 0 || ny < 0 || nx >= N || ny >= M || visit[ny][nx]) {
            ny = y + DY[(dir + 1) % 4];
            nx = x + DX[(dir + 1) % 4];
            if (visit[ny][nx]) return;
            result++;
            go(ny, nx, (dir + 1) % 4);
        } else {
            go(ny, nx, dir);
        }
    }

}