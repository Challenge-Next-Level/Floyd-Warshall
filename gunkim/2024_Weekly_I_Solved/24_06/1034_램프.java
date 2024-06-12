// 애드 혹 문제
// 특별한 풀이 법을 알아내야 하는게 정말 곤욕이다
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int m;
    private int[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = str.charAt(j) -'0';
            }
        }

        int k = Integer.parseInt(br.readLine());

        int result = 0;

        for (int i = 0; i < n; i++) {
            int zeroCnt = 0;
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) zeroCnt++;
            }

            // 행에 있는 모든 전구가 켜질 수 있는 조건
            // 1. 켜야하는 전구의 수가 k보다 작아야 한다
            // 2. 켜야하는 전구의 수와 k는 똑같이 짝수거나 똑같이 홀수여야 한다
            if (zeroCnt <= k && zeroCnt % 2 == k % 2) {
                int samRowCnt = 1;
                // 같은 패턴의 행이 있는지 확인
                for (int j = i + 1; j < n; j++) {
                    if (isSameRowCnt(i, j)) samRowCnt++;
                }
                result = Math.max(result, samRowCnt);
            }
        }

        System.out.println(result);

    }

    private boolean isSameRowCnt(int row1, int row2) {
        for (int i = 0; i < m; i++) {
            if (board[row1][i] != board[row2][i]) return false;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}