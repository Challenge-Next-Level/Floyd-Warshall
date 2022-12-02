import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public int[][] makeBoardAndSum(int size, int[][] board, BufferedReader bufferedReader, StringTokenizer stringTokenizer) throws IOException {
        int[][] sum = new int[size+1][size+1];
        for (int i = 0; i < size; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int j = 0; j < size; j++) {
                board[i][j] = Integer.parseInt(stringTokenizer.nextToken()); // board 만들기
                // sum 만들기
                if (i == 0 && j == 0) {
                    sum[i+1][j+1] = board[i][j];
                } else if (i == 0) {
                    sum[i+1][j+1] = sum[i+1][j] + board[i][j];
                } else if (j == 0) {
                    sum[i+1][j+1] = sum[i][j+1] + board[i][j];
                } else {
                    sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] - sum[i][j] + board[i][j];
                }
            }
        }
        return sum;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][n];
        int[][] sum = makeBoardAndSum(n, board, br, st);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) { // 구간 합 계산하기
            st = new StringTokenizer(br.readLine());
            int[] cd = new int[4]; // x1,y1,x2,y2 저장
            for (int j = 0; j < 4; j++) {
                cd[j] = Integer.parseInt(st.nextToken());
            }
            sb.append(sum[cd[2]][cd[3]] - sum[cd[2]][cd[1]-1] - sum[cd[0]-1][cd[3]] + sum[cd[0]-1][cd[1]-1]).append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}