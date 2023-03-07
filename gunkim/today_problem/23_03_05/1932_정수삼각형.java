import java.util.*;
import java.io.*;

public class Main {

    private int[][] dp;
    private int n;
    private int[][] trees;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        trees = new int[n][n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j <= i; j++) {
                trees[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new int[n][n];
        for (int i = 0; i < n; i++) { //dp -1로 초기화
            for (int j = 0; j <= i; j++) {
                dp[i][j] = -1;
            }
        }

        int answer = search(0, 0);
        System.out.println(answer);
    }

    public int search(int y, int x) {
        if (dp[y][x] != -1) return dp[y][x]; //이미 방문했다면 dp값이 있을 거임
        if (y == n - 1) return trees[y][x]; //맨 아래 노드라면 해당 값 리턴
        int temp = Math.max(search(y + 1, x), search(y + 1, x + 1)); //왼쪽, 오른쪽 탐색
        dp[y][x] = temp + trees[y][x];
        return dp[y][x];
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}