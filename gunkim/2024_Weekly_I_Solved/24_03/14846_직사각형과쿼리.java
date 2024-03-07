import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        // 해당 구간 까지의 각 숫자의 누적 갯수를 저장
        int[][][] arr = new int[n + 1][n + 1][11];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                int num = Integer.parseInt(st.nextToken());
                for (int k = 1; k <= 10; k++) {
                    arr[i][j][k] = arr[i - 1][j][k] + arr[i][j - 1][k] - arr[i - 1][j - 1][k];
                }
                arr[i][j][num] += 1;
            }
        }


        int q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int[] result = new int[11];
            int count = 0;
            for (int j = 1; j <= 10; j++) {
                result[j] = arr[x2][y2][j] - arr[x2][y1 - 1][j] - arr[x1 - 1][y2][j] + arr[x1 - 1][y1 - 1][j];
                if (result[j] > 0) count++;
            }
            sb.append(count).append("\n");
        }

        System.out.println(sb);

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}