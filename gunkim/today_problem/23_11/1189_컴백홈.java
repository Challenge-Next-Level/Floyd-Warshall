// 1 try 1 solve
// dfs 정석 문제이다.
import java.util.*;
import java.io.*;

public class Main {

    private int answer = 0;
    private int r;
    private int c;
    private int k;
    private boolean[][] visit;
    private char[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            String input = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = input.charAt(j);
            }
        }

        visit = new boolean[r][c];
        visit[r - 1][0] = true;
        dfs(r - 1, 0 ,1);


        System.out.println(answer);
    }


    private int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public void dfs(int y, int x, int count) {
        // dfs 탈출 조건
        if (count == k) {
            if (y == 0 && x == c - 1) answer++;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int ny = y + dir[i][0];
            int nx = x + dir[i][1];

            if(ny < 0 || ny >= r || nx < 0 || nx >= c || visit[ny][nx]) continue;
            if(board[ny][nx] == 'T') continue; // 벽으로 이동할 수는 없음

            visit[ny][nx] = true;
            dfs(ny, nx, count + 1);
            visit[ny][nx] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}