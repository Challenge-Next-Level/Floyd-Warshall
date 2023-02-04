import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int test = Integer.parseInt(br.readLine());
        for (int t = 0; t < test; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[] rows = new int[n];
            int[] cols = new int[n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    rows[i] += num;
                    cols[j] += num;
                }
            }
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int r1 = Integer.parseInt(st.nextToken()) - 1;
                int c1 = Integer.parseInt(st.nextToken()) - 1;
                int r2 = Integer.parseInt(st.nextToken()) - 1;
                int c2 = Integer.parseInt(st.nextToken()) - 1;
                int v = Integer.parseInt(st.nextToken());
                for (int r = r1; r <= r2; r++) {
                    rows[r] += v * (c2 - c1 + 1);
                }
                for (int c = c1; c <= c2; c++) {
                    cols[c] += v * (r2 - r1 + 1);
                }
            }


            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                sb.append(rows[i] + " ");
            }
            sb.append("\n");
            for (int j = 0; j < n; j++) {
                sb.append(cols[j] + " ");
            }
            System.out.println(sb);
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}