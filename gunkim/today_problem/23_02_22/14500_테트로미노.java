import java.util.*;
import java.io.*;

public class Main {

    static int max = Integer.MIN_VALUE;
    int[][] arr;
    boolean[][] visit;
    int n;
    int m;
    int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visit = new boolean[n][m];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                visit[i][j] = true;
                solve(i, j, arr[i][j], 1);
                visit[i][j] = false;
            }
        }

        System.out.println(max);

    }

    public void solve(int row, int col, int sum, int depth) {
        if(depth == 4) { // 4번 탐색을 했다면
            max = Math.max(max, sum);
            return;
        }

        for(int i = 0; i < dir.length; i++) {
            int curRow = row + dir[i][0];
            int curCol = col + dir[i][1];

            if(curRow < 0 || curRow >= n || curCol < 0 || curCol >= m) {
                continue;
            }

            if(!visit[curRow][curCol]) {
                if(depth == 2) { // ㅗ 모양의 테트로미노에 대한 탐색
                    visit[curRow][curCol] = true;
                    solve(row, col, sum + arr[curRow][curCol], depth + 1);
                    visit[curRow][curCol] = false;
                }
                visit[curRow][curCol] = true;
                solve(curRow, curCol, sum + arr[curRow][curCol], depth + 1);
                visit[curRow][curCol] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}