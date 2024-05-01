// 그냥 막 구현..?
import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int m;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        if (m == 2) {
            for (int i = 0; i < n - 1; i++) {
                System.out.println(i + " " + (i + 1));
            }
        } else {
            for (int i = 1; i <= m; i++) {
                System.out.println(0 + " " + i);
            }
            for (int i = m + 1; i < n; i++) {
                System.out.println((i - 1) + " " + i);
            }
        }

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}