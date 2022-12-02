import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int test = Integer.parseInt(br.readLine());
        for (int i = 0; i < test; i++) {
            st = new StringTokenizer(br.readLine());
            int[] coordinate = new int[4]; // 좌표 배열
            for (int j = 0; j < 4; j++) { // i,j,x,y 저장
                coordinate[j] = Integer.parseInt(st.nextToken());
            }
            int answer = 0;
            for (int p = coordinate[0] - 1; p < coordinate[2]; p++) {
                for (int q = coordinate[1] - 1; q < coordinate[3]; q++) {
                    answer += board[p][q];
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}