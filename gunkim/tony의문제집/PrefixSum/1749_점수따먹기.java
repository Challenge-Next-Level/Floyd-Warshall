import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n + 1][m + 1];
        int[][] sum = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + board[i][j]; // 구간 합 저장하기
            }
        }

        long answer = Integer.MIN_VALUE; // 0으로 초기화를 하면 안됨.
        for (int a = 1; a <= n; a++) { // (a,b) ~ (c,d) 의 구간합을 전부 고려
            for (int b = 1; b <= m; b++) {
                for (int c = a; c <= n; c++) {
                    for (int d = b; d <= m; d++) {
                        int value = sum[c][d] - sum[a - 1][d] - sum[c][b - 1] + sum[a - 1][b - 1];
                        if (value > answer) answer = value;
                    }
                }
            }
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}